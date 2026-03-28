💊 Pharmacy Billing System

A beginner-friendly Python project that simulates a real-world pharmacy billing system.
It includes both a **Command Line (CLI)** version and a **Graphical User Interface (GUI)** version.

---

## 📌 Project Overview

This project is designed to practice Python programming by building a real-world billing system used in medical stores.

It calculates medicine bills, assigns loyalty points, and allows customers to redeem points in future visits.

---

## ⚙️ Features

- Multiple customer visits (loyalty points carry forward)
- Multiple medicines per visit
- Automatic bill calculation
- Loyalty points system (earn + redeem)
- Discount calculation using points
- Input validation (CLI + GUI)

---

## 🎁 Loyalty Points Logic

- **₹100 bill = 1 point**
- Example: ₹560 bill ⇒ `560 // 100 = 5` points

---

## 🔄 Redemption Rules

- **1 point = ₹25 discount**
- **Minimum 10 points required** to redeem
- Cannot redeem more than available points
- Cannot redeem more than what the bill allows

---

## ▶️ How to Run

### ✅ CLI Version
```bash
python pharmacy_billing_system.py
```

### ✅ GUI Version (Tkinter)
```bash
python pharmacy_billing_gui.py
```

---

## 🖥️ GUI Notes

- **Add Medicine**: Adds medicines to the cart.
- **Generate Bill**: Generates bill and adds earned points.
- **Redeem**: Redeems points (only after generating bill, and only if points ≥ 10).
- **Clear Cart**: Clears current cart items.
- **New Visit**: Starts a new visit (cart clears, points carry forward).

---

## 📁 Project Structure

pharmacy-billing-system/
│
├── pharmacy_billing_system.py   # CLI version
├── pharmacy_billing_gui.py      # GUI version (Tkinter)
├── README.md
└── sample-output.txt

---

## 🛠 Technologies Used

- Python 3
- Tkinter (GUI)

---

## 👨‍💻 Author

Saloni Tiwari  
Python & Data Science Student

---

⭐ If you like this project, feel free to star the repository!
