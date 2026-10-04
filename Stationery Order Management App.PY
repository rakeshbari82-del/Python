# 📚 STATIONERY SHOP MANAGEMENT APP
# Python + Tkinter

import tkinter as tk
from tkinter import ttk, messagebox


class StationeryShop:

    def __init__(self, root):
        self.root = root
        self.root.title("📚 Smart Stationery Shop")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Stationery items and prices in USD
        self.items = {
            "Notebook": 3,
            "Pencil Pack": 2,
            "Pen Set": 4,
            "Eraser": 1,
            "Geometry Box": 6,
            "Colour Pencils": 5
        }

        # USD to INR exchange rate
        self.exchange_rate = 82

        # ---------------- BACKGROUND ----------------
        self.canvas = tk.Canvas(
            root,
            width=800,
            height=600,
            bg="#e8f4ff"
        )
        self.canvas.pack()

        # Main frame
        frame = ttk.Frame(root, padding=15)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # ---------------- TITLE ----------------
        ttk.Label(
            frame,
            text="📚 SMART STATIONERY SHOP ✏️",
            font=("Arial", 22, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=3,
            pady=10
        )

        ttk.Label(
            frame,
            text="Choose your stationery and place your order!",
            font=("Arial", 11)
        ).grid(
            row=1,
            column=0,
            columnspan=3,
            pady=5
        )

        # Store quantity entries
        self.quantity_entries = {}

        # ---------------- ITEMS ----------------
        row_number = 2

        for item, price in self.items.items():

            ttk.Label(
                frame,
                text=f"{item} (${price})",
                font=("Arial", 12)
            ).grid(
                row=row_number,
                column=0,
                padx=10,
                pady=6,
                sticky="w"
            )

            entry = ttk.Entry(
                frame,
                width=8
            )

            entry.grid(
                row=row_number,
                column=1,
                padx=10,
                pady=6
            )

            self.quantity_entries[item] = entry

            row_number += 1

        # ---------------- CURRENCY ----------------
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12, "bold")
        ).grid(
            row=row_number,
            column=0,
            padx=10,
            pady=10
        )

        self.currency_var = tk.StringVar(value="USD")

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            values=("USD", "INR"),
            width=15
        )

        currency_dropdown.grid(
            row=row_number,
            column=1,
            padx=10,
            pady=10
        )

        row_number += 1

        # ---------------- DISCOUNT ----------------
        ttk.Label(
            frame,
            text="Discount:",
            font=("Arial", 12, "bold")
        ).grid(
            row=row_number,
            column=0,
            padx=10,
            pady=5
        )

        self.discount_var = tk.StringVar(value="0%")

        discount_dropdown = ttk.Combobox(
            frame,
            textvariable=self.discount_var,
            state="readonly",
            values=("0%", "5%", "10%", "15%", "20%"),
            width=15
        )

        discount_dropdown.grid(
            row=row_number,
            column=1,
            padx=10,
            pady=5
        )

        row_number += 1

        # ---------------- BUTTONS ----------------
        ttk.Button(
            frame,
            text="🛒 PLACE ORDER",
            command=self.place_order
        ).grid(
            row=row_number,
            column=0,
            columnspan=3,
            pady=10
        )

        row_number += 1

        ttk.Button(
            frame,
            text="🗑️ CLEAR ALL",
            command=self.clear_all
        ).grid(
            row=row_number,
            column=0,
            columnspan=3,
            pady=5
        )

    # ------------------------------------------------
    # PLACE ORDER
    # ------------------------------------------------

    def place_order(self):

        total_cost = 0
        order_summary = "🧾 STATIONERY ORDER RECEIPT\n"
        order_summary += "-----------------------------\n"

        currency = self.currency_var.get()

        # Ternary operator
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        ordered_items = 0

        # Read quantities
        for item, entry in self.quantity_entries.items():

            quantity = entry.get()

            # Check if quantity is a number
            if quantity == "":
                continue

            if not quantity.isdigit():

                messagebox.showerror(
                    "Invalid Quantity",
                    f"Please enter a valid number for {item}."
                )
                return

            quantity = int(quantity)

            if quantity > 0:

                price = self.items[item] * rate
                cost = quantity * price

                total_cost += cost
                ordered_items += quantity

                order_summary += (
                    f"{item}: {quantity} × "
                    f"{symbol}{price} = "
                    f"{symbol}{cost}\n"
                )

        # Check whether anything was ordered
        if total_cost == 0:

            messagebox.showwarning(
                "No Order",
                "Please select at least one stationery item."
            )
            return

        # ---------------- DISCOUNT ----------------

        discount_text = self.discount_var.get()

        discount_percent = int(
            discount_text.replace("%", "")
        )

        discount_amount = (
            total_cost * discount_percent / 100
        )

        final_cost = total_cost - discount_amount

        # ---------------- RECEIPT ----------------

        order_summary += "-----------------------------\n"

        order_summary += (
            f"Subtotal: {symbol}{total_cost}\n"
        )

        order_summary += (
            f"Discount: {discount_percent}%\n"
        )

        order_summary += (
            f"Discount Amount: {symbol}{discount_amount:.2f}\n"
        )

        order_summary += "-----------------------------\n"

        order_summary += (
            f"TOTAL: {symbol}{final_cost:.2f}\n"
        )

        order_summary += (
            f"Total Items: {ordered_items}"
        )

        messagebox.showinfo(
            "🎉 Order Successful!",
            order_summary
        )

    # ------------------------------------------------
    # CLEAR ALL
    # ------------------------------------------------

    def clear_all(self):

        for entry in self.quantity_entries.values():
            entry.delete(0, tk.END)

        self.currency_var.set("USD")
        self.discount_var.set("0%")

        messagebox.showinfo(
            "Cleared",
            "All quantities have been cleared."
        )


# ====================================================
# MAIN PROGRAM
# ====================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = StationeryShop(root)

    root.mainloop()