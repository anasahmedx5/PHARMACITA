# Pharmacy Inventory Management System

This project is a web-based application built with **Flask**, **SQLite**, and **HTML/CSS**. It is designed to streamline the management of a pharmacy's inventory system. The application allows employees to log in, manage medicines, track sales, and monitor stock levels efficiently.

## Features

1. **User Authentication**: 
   - Employees can log in with a username and password.
   - A secure session management system ensures only authenticated users can access the internal pages.
   - **Password Hashing:** The application now uses **Argon2**, a secure password hashing algorithm, to store and verify passwords securely.

2. **Dashboard (Homepage)**: 
   - Displays essential statistics such as:
     - Total number of employees.
     - Number of low-stock medicines (medicines with a quantity of 5 or fewer).
     - Total number of medicines in stock.
     - Total amount of medicines sold and their total revenue.

3. **Medicine Management**: 
   - **Add Medicine**: Employees can add new medicines to the inventory, including specifying their price and name.
   - **Remove Medicine**: Employees can remove medicines from the inventory. Upon removal, the quantity and revenue for the sold medicine are updated.
   - **Error Message Display**: If a user enters invalid or incomplete inputs when adding or removing a medicine, an error message is displayed above the input field instead of redirecting them to a new page.

4. **Stock Overview**: 
   - The **Stock** page provides an overview of the current inventory, showing each medicine's name and its available quantity.

5. **Sales Tracking**: 
   - The application keeps track of the total amount of medicines sold and the revenue generated from those sales.

## Database Structure

The system uses a **SQLite** database with the following tables:

- **pharmacy**: Contains details about the pharmacy location.
- **employee**: Stores employee information, linking them to a specific pharmacy.
- **medicine**: Stores information about the medicines in stock, including their name, price, and pharmacy association.
- **medicinesold**: Tracks the quantity and total revenue for each medicine sold.

## Technologies Used

- **Flask**: For building the web application.
- **SQLite**: For the database.
- **HTML/CSS**: For front-end development.
- **Python**: For back-end logic and database interactions.
- **Argon2**: For secure password hashing.

## **Installation Guide**

### **Prerequisites**
Before installing, make sure you have the following installed on your system:
- **Python** (version 3.7 or higher)
- **pip** (Python package manager)
- **Git** (to clone the repository)

### **Steps to Install and Run the Project**

#### **1. Clone the Repository**
```sh
git clone https://github.com/anasahmedx5/pharmacita.git
cd pharmacita
```

#### **2. Run the Application**
```sh
python -m flask --app .\app.py run
```

#### **3. Access the Admin Panel**
Default Admin Credentials:
 - Username: `anas`
 - Password: `1`

## Future Enhancements
1. **Tracking Medicines Expiry Dates:**
   - Feature Description: Medicines will now have an expiry date, and the system will allow employees to set and track these expiry dates.
   - Purpose: This will help the pharmacy stay on top of expiring stock and prevent selling expired medicines.

2. **Messaging System Between Employees:**
   - Feature Description: A messaging system will be implemented to allow employees to send and receive messages. This will help with internal communication within the pharmacy, particularly in areas like stock management and sales tracking.
