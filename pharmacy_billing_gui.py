# ============================================
# Python
# Author: Saloni Tiwari
# Topic: Pharmacy Billing System (GUI Advanced)
# Description: Multi-medicine billing + reward system + redeem
# ============================================

import tkinter as tk
from tkinter import messagebox

points = 0
medicines = []

# ========================================
# Add Medicine
# ========================================
def add_medicine():
    try:
        name = entry_name.get()
        qty = int(entry_qty.get())
        cost = float(entry_cost.get())

        if name == "" or qty <= 0 or cost <= 0:
            messagebox.showerror("Error", "Invalid Input")
            return

        total = qty * cost
        medicines.append((name, qty, cost, total))

        listbox.insert(tk.END, f"{name} | Qty:{qty} | ₹{total}")

        entry_name.delete(0, tk.END)
        entry_qty.delete(0, tk.END)
        entry_cost.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Invalid Input")


# ========================================
# Generate Bill
# ========================================
def generate_bill():
    global points

    if not medicines:
        messagebox.showerror("Error", "No medicines added")
        return

    total = sum(item[3] for item in medicines)
    cur_points = total // 100
    points += cur_points

    bill = "------ BILL ------\n"
    for m in medicines:
        bill += f"{m[0]} x{m[1]} = ₹{m[3]}\n"

    bill += f"\nTotal: ₹{total}\n"
    bill += f"Points Earned: {cur_points}\n"

    bill_text.set(bill)
    points_text.set(f"Total Points: {points}")


# ========================================
# Redeem Points
# ========================================
def redeem():
    global points

    try:
        total = sum(item[3] for item in medicines)

        if points < 10:
            messagebox.showinfo("Info", "Not enough points")
            return

        redeem_points = int(entry_redeem.get())

        if redeem_points > points:
            messagebox.showerror("Error", "Not enough points")
            return

        discount = redeem_points * 25

        if discount > total:
            messagebox.showerror("Error", "Discount too high")
            return

        final = total - discount
        points -= redeem_points

        bill_text.set(f"Final Bill after redeem: ₹{final}")
        points_text.set(f"Remaining Points: {points}")

    except:
        messagebox.showerror("Error", "Invalid Input")


# ========================================
# Clear All
# ========================================
def clear_all():
    medicines.clear()
    listbox.delete(0, tk.END)
    bill_text.set("")
    

# ========================================
# GUI Setup
# ========================================
root = tk.Tk()
root.title("Pharmacy Billing System")
root.geometry("500x600")

tk.Label(root, text="Pharmacy Billing System", font=("Arial", 16, "bold")).pack(pady=10)

# Inputs
tk.Label(root, text="Medicine Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Quantity").pack()
entry_qty = tk.Entry(root)
entry_qty.pack()

tk.Label(root, text="Cost").pack()
entry_cost = tk.Entry(root)
entry_cost.pack()

tk.Button(root, text="Add Medicine", command=add_medicine).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Buttons
tk.Button(root, text="Generate Bill", command=generate_bill).pack(pady=5)

tk.Label(root, text="Redeem Points").pack()
entry_redeem = tk.Entry(root)
entry_redeem.pack()

tk.Button(root, text="Redeem", command=redeem).pack(pady=5)

tk.Button(root, text="Clear", command=clear_all).pack(pady=5)

# Output
bill_text = tk.StringVar()
points_text = tk.StringVar()

tk.Label(root, textvariable=bill_text, fg="blue", justify="left").pack(pady=10)
tk.Label(root, textvariable=points_text, fg="green").pack()

root.mainloop()