# ============================================
# Python
# Author: Saloni Tiwari
# Topic: Pharmacy Billing System (GUI Advanced)
# Description: Multi-medicine billing + reward system + redeem
# ============================================

import tkinter as tk
from tkinter import messagebox

# Loyalty rules
POINTS_PER_100_RUPEES = 1
RUPEES_PER_POINT = 25
MIN_POINTS_TO_REDEEM = 10


class PharmacyBillingApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Pharmacy Billing System")
        self.root.geometry("520x650")

        # state
        self.points = 0
        self.medicines = []  # list of dicts: {name, qty, cost, total}
        self.bill_generated = False
        self.last_total = 0.0
        self.last_earned_points = 0

        self._build_ui()
        self._refresh_summary()

    # ----------------------
    # UI
    # ----------------------
    def _build_ui(self):
        tk.Label(self.root, text="Pharmacy Billing System", font=("Arial", 16, "bold")).pack(pady=10)

        # Inputs
        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        tk.Label(frame, text="Medicine Name").grid(row=0, column=0, sticky="w")
        self.entry_name = tk.Entry(frame, width=30)
        self.entry_name.grid(row=0, column=1, padx=8)

        tk.Label(frame, text="Quantity").grid(row=1, column=0, sticky="w")
        self.entry_qty = tk.Entry(frame, width=30)
        self.entry_qty.grid(row=1, column=1, padx=8)

        tk.Label(frame, text="Cost (₹)").grid(row=2, column=0, sticky="w")
        self.entry_cost = tk.Entry(frame, width=30)
        self.entry_cost.grid(row=2, column=1, padx=8)

        tk.Button(self.root, text="Add Medicine", command=self.add_medicine).pack(pady=6)

        # Listbox
        tk.Label(self.root, text="Cart").pack()
        self.listbox = tk.Listbox(self.root, width=62)
        self.listbox.pack(pady=8)

        # Buttons
        btns = tk.Frame(self.root)
        btns.pack(pady=6)

        tk.Button(btns, text="Generate Bill", command=self.generate_bill, width=16).grid(row=0, column=0, padx=6)
        tk.Button(btns, text="Clear Cart", command=self.clear_cart, width=16).grid(row=0, column=1, padx=6)
        tk.Button(btns, text="New Visit", command=self.new_visit, width=16).grid(row=0, column=2, padx=6)

        # Redeem
        redeem_frame = tk.Frame(self.root)
        redeem_frame.pack(pady=8)

        tk.Label(redeem_frame, text="Redeem Points").grid(row=0, column=0, sticky="w")
        self.entry_redeem = tk.Entry(redeem_frame, width=20)
        self.entry_redeem.grid(row=0, column=1, padx=8)
        tk.Button(redeem_frame, text="Redeem", command=self.redeem).grid(row=0, column=2)

        # Output
        self.bill_text = tk.StringVar(value="")
        self.points_text = tk.StringVar(value="")

        tk.Label(self.root, textvariable=self.bill_text, fg="blue", justify="left", anchor="w").pack(pady=10, fill="x", padx=10)
        tk.Label(self.root, textvariable=self.points_text, fg="green").pack()

    # ----------------------
    # Helpers
    # ----------------------
    def _cart_total(self) -> float:
        return sum(item["total"] for item in self.medicines)

    def _refresh_cart_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in self.medicines:
            self.listbox.insert(
                tk.END,
                f"{item['name']} | Qty:{item['qty']} | Cost:₹{item['cost']} | Total:₹{item['total']}"
            )

    def _refresh_summary(self):
        self.points_text.set(f"Total Points: {self.points}")

    def _reset_bill_state(self):
        self.bill_generated = False
        self.last_total = 0.0
        self.last_earned_points = 0
        self.bill_text.set("")

    # ----------------------
    # Actions
    # ----------------------
    def add_medicine(self):
        try:
            name = self.entry_name.get().strip()
            qty = int(self.entry_qty.get().strip())
            cost = float(self.entry_cost.get().strip())

            if not name or qty <= 0 or cost <= 0:
                messagebox.showerror("Error", "Invalid input. Name must not be empty and Quantity/Cost must be > 0.")
                return

            total = qty * cost
            self.medicines.append({"name": name, "qty": qty, "cost": cost, "total": total})

            self._refresh_cart_listbox()
            self._reset_bill_state()

            self.entry_name.delete(0, tk.END)
            self.entry_qty.delete(0, tk.END)
            self.entry_cost.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Quantity must be an integer and Cost must be a number.")

    def generate_bill(self):
        if not self.medicines:
            messagebox.showerror("Error", "No medicines added.")
            return

        total = self._cart_total()
        earned_points = int(total // 100) * POINTS_PER_100_RUPEES
        self.points += earned_points

        bill_lines = ["------ BILL ------"]
        for item in self.medicines:
            bill_lines.append(f"{item['name']} x{item['qty']} = ₹{item['total']}")

        bill_lines.append("")
        bill_lines.append(f"Total: ₹{total}")
        bill_lines.append(f"Points Earned (this visit): {earned_points}")

        self.bill_text.set("
".join(bill_lines))
        self._refresh_summary()

        self.bill_generated = True
        self.last_total = total
        self.last_earned_points = earned_points

    def redeem(self):
        if not self.medicines:
            messagebox.showerror("Error", "No medicines added.")
            return

        # Enforce normal flow: generate bill first
        if not self.bill_generated:
            messagebox.showinfo("Info", "Please click 'Generate Bill' before redeeming points.")
            return

        if self.points < MIN_POINTS_TO_REDEEM:
            messagebox.showinfo("Info", f"Not enough points to redeem. Minimum required: {MIN_POINTS_TO_REDEEM}.")
            return

        try:
            redeem_points = int(self.entry_redeem.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Redeem points must be an integer.")
            return

        if redeem_points <= 0:
            messagebox.showerror("Error", "Redeem points must be > 0.")
            return

        total = self.last_total
        max_by_bill = int(total // RUPEES_PER_POINT)
        max_redeemable = min(self.points, max_by_bill)

        if max_redeemable <= 0:
            messagebox.showinfo("Info", "This bill is too small to redeem any points.")
            return

        if redeem_points > max_redeemable:
            messagebox.showerror(
                "Error",
                f"You can redeem at most {max_redeemable} points for this bill (Available: {self.points})."
            )
            return

        discount = redeem_points * RUPEES_PER_POINT
        final = total - discount

        self.points -= redeem_points
        self._refresh_summary()

        self.bill_text.set(
            self.bill_text.get()
            + "\n"
            + f"Redeemed Points: {redeem_points} (₹{discount} discount)\n"
            + f"Final Bill after redeem: ₹{final}"
        )

        # After redeeming, start fresh cart to avoid double counting
        self.clear_cart()

    def clear_cart(self):
        self.medicines.clear()
        self._refresh_cart_listbox()
        self.entry_redeem.delete(0, tk.END)
        self._reset_bill_state()

    def new_visit(self):
        # New visit = clear cart and bill view, points remain (loyalty points persist)
        self.clear_cart()
        messagebox.showinfo("Info", "New visit started. Points are carried forward.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacyBillingApp(root)
    root.mainloop()