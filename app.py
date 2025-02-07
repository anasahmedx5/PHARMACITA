import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = "your_secret_key" 

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session: 
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated_function


def get_db_connection():
    conn = sqlite3.connect("my.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=["GET", "POST"])
def index():
    session.clear()
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
    
        if not username or not password:
            return "Please enter a username or password", 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM employee WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session["emp_id"] = user["emp_id"]
            session["name"] = user["name"]
            session["username"] = user["username"]
            session["password"] = user["password"]
            session["pharm_id"] = user["pharm_id"] 
            return redirect(url_for("homepage"))
        
        else:
            return "Invalid username or password", 401    
    
    return render_template("login.html")
    

@app.route("/homepage", methods=["GET", "POST"])
@login_required
def homepage():
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) AS employee_count FROM employee")
    employees = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT COUNT(*) AS repeated
        FROM (
            SELECT name
            FROM medicine 
            GROUP BY name
            HAVING COUNT(*) <= 5
        ) AS filtered_medicines;
    """)
    low_stock = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT COUNT(*) AS repeated
        FROM (
            SELECT name
            FROM medicine 
            GROUP BY name
        ) AS filtered_medicines;
    """)
    stock = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT total 
        FROM medicinesold;
    """)
    total = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT amount 
        FROM medicinesold;
    """)
    amount = cursor.fetchone()[0]
    
    conn.commit()
    conn.close()
    
    return render_template("homepage.html", emp_name=session.get("name"), employees=employees, 
                           low_stock=low_stock, stock=stock, total=total, amount=amount)



@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    
    if request.method == "POST":
        medicine_n = request.form.get("medicine_n")
        price = request.form.get("price")
        
        if not medicine_n or not price:
            return "Please enter valid inputs", 401
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO medicine (name, price) VALUES (?, ?)", (medicine_n, price)) 
        
            # cursor.execute("UPDATE medicine SET quantity = quantity + ? WHERE name = ?", (quantity, medicine_n))

        conn.commit()
        conn.close()
                  
    return render_template("add.html", emp_name=session["name"])



@app.route("/remove", methods=["GET", "POST"])
@login_required
def remove():
    if request.method == "POST":
        medicine_n = request.form.get("medicine_n")
        
        if not medicine_n:
            return "Please enter valid inputs", 401
        
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT rowid, price FROM medicine WHERE name = ? ORDER BY rowid ASC LIMIT 1", (medicine_n,))
        row = cursor.fetchone()
        
        if row is None:
            return "Medicine not found", 401
        else:
            rowid = row[0]
            price = row["price"]
            
            cursor.execute("DELETE FROM medicine WHERE rowid = ?", (rowid,))
            
            cursor.execute("UPDATE medicinesold SET amount = amount + 1, total = total + ? WHERE rowid = 1", (price,))  # Assuming you're updating a specific record
            
        conn.commit()
        conn.close()
    
    return render_template("remove.html", emp_name=session["name"])




@app.route("/stock", methods=["GET", "POST"])
@login_required
def stock():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, COUNT(*) AS quantity FROM medicine GROUP BY name;")
    rows = cursor.fetchall()

    conn.close()

    return render_template("stock.html", emp_name=session["name"], rows=rows)



if __name__ == "__main__":
    app.run(debug=True)
 
