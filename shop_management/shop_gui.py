# pylint: disable=missing-docstring

import tkinter as tk
from tkinter import messagebox

from shop import Shop


class ShopGUI:
    def __init__(self, main_window):
        self.shop = Shop()
        self.main_window = main_window
        self.main_window.title("Shop Management System")

        self.button_frame = tk.Frame(main_window)
        self.button_frame.pack(side=tk.TOP, fill=tk.X)

        self.add_item_button = tk.Button(
            self.button_frame, text="Add Item", command=self.show_add_item
        )
        self.add_item_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.sell_item_button = tk.Button(
            self.button_frame, text="Sell Item", command=self.show_sell_item
        )
        self.sell_item_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.view_report_button = tk.Button(
            self.button_frame, text="View Report", command=self.show_view_report
        )
        self.view_report_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.content_frame = tk.Frame(main_window)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        self.add_item_panel = tk.Frame(self.content_frame)
        self.sell_item_panel = tk.Frame(self.content_frame)
        self.view_report_panel = tk.Frame(self.content_frame)

        self.create_add_item_panel()
        self.create_sell_item_panel()
        self.create_view_report_panel()

        self.show_add_item()

    def create_add_item_panel(self):
        tk.Label(self.add_item_panel, text="Name:").grid(
            row=0, column=0, padx=5, pady=5
        )
        self.item_name_entry = tk.Entry(self.add_item_panel)
        self.item_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.add_item_panel, text="Price:").grid(
            row=1, column=0, padx=5, pady=5
        )
        self.item_price_entry = tk.Entry(self.add_item_panel)
        self.item_price_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.add_item_panel, text="Quantity:").grid(
            row=2, column=0, padx=5, pady=5
        )
        self.item_quantity_entry = tk.Entry(self.add_item_panel)
        self.item_quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.add_item_panel, text="Add Item", command=self.add_item).grid(
            row=3, columnspan=2, pady=5
        )

    def create_sell_item_panel(self):
        tk.Label(self.sell_item_panel, text="Product Name:").grid(
            row=0, column=0, padx=5, pady=5
        )
        self.sell_product_name_entry = tk.Entry(self.sell_item_panel)
        self.sell_product_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.sell_item_panel, text="Quantity:").grid(
            row=1, column=0, padx=5, pady=5
        )
        self.sell_quantity_entry = tk.Entry(self.sell_item_panel)
        self.sell_quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.sell_item_panel, text="Sell Item", command=self.sell_item).grid(
            row=2, columnspan=2, pady=5
        )

    def create_view_report_panel(self):
        tk.Button(
            self.view_report_panel,
            text="View Sales Report",
            command=self.view_sales_report,
        ).pack(pady=5)
        tk.Button(
            self.view_report_panel,
            text="Display Inventory",
            command=self.display_inventory,
        ).pack(pady=5)

    def show_add_item(self):
        self._show_panel(self.add_item_panel)

    def show_sell_item(self):
        self._show_panel(self.sell_item_panel)

    def show_view_report(self):
        self._show_panel(self.view_report_panel)

    def _show_panel(self, panel):
        # Hide all panels
        for p in [self.add_item_panel, self.sell_item_panel, self.view_report_panel]:
            p.pack_forget()

        # Show the selected panel
        panel.pack(fill=tk.BOTH, expand=True)

    def add_item(self):
        name = self.item_name_entry.get()
        price = float(self.item_price_entry.get())
        quantity = int(self.item_quantity_entry.get())

        if name and quantity > 0 and price > 0:
            self.shop.add_item_to_inventory(name, price, quantity)
            messagebox.showinfo("Success", "Item added to inventory")
            self.item_name_entry.delete(0, tk.END)
            self.item_price_entry.delete(0, tk.END)
            self.item_quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter valid item name and quantity.")

    def sell_item(self):
        product_name = self.sell_product_name_entry.get()
        quantity = int(self.sell_quantity_entry.get())
        if product_name and quantity > 0:
            self.shop.sell_item(product_name, quantity)
            messagebox.showinfo("Success", "Item sold successfully.")
            self.sell_product_name_entry.delete(0, tk.END)
            self.sell_quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror(
                "Error", "Please enter valid product name and quantity."
            )

    def view_sales_report(self):
        sales = self.shop.view_sales_report()

        if sales:
            try:
                report = "\n".join(
                    [
                        f"Name: {row[1]}, Quantity: {row[2]}, Total Price: {row[3]}"
                        for row in sales
                    ]
                )
                messagebox.showinfo("Sales Report", report)
            except IndexError as e:
                print(f"Error accessing sales data: {e}")
                messagebox.showerror(
                    "Error", "Sales data is not in the expected format."
                )
        else:
            messagebox.showinfo("Sales Report", "No sales have been made.")

    def display_inventory(self):
        inventory = self.shop.display_inventory()

        if inventory:
            try:
                inventory_list = "\n".join(
                    [
                        f"Name: {row[1]}, Price: {row[2]}, Quantity: {row[3]}"
                        for row in inventory
                    ]
                )
                messagebox.showinfo("Inventory", inventory_list)
            except IndexError as e:
                print(f"Error accessing inventory data: {e}")
                messagebox.showerror(
                    "Error", "Inventory data is not in the expected format."
                )
        else:
            messagebox.showinfo("Inventory", "Inventory is empty.")
