document.addEventListener("DOMContentLoaded", function () {
    function setDefaultValues() {
        let welcomeText = document.querySelector(".welcome");
        if (welcomeText && (welcomeText.innerHTML.includes("{{") || welcomeText.innerText.trim() === "")) {
            welcomeText.innerText = "Welcome Guest!";
        }

        document.querySelectorAll(".homepage-p1").forEach(el => {
            if (!el.innerHTML.trim() || el.innerHTML.includes("{{")) {
                let defaultValues = {
                    "Medicines Sold": 50,
                    "Total Stock": 100,
                    "Low Stock": 10,
                    "Employees": 5,
                    "Revenue": "$0.00"
                };

                let label = el.previousElementSibling.innerText.trim();
                el.innerText = defaultValues[label] || "N/A";
            }
        });
    }

    setDefaultValues();
});
