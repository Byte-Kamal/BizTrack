# pylint: disable=missing-docstring

from tkinter import messagebox

import mysql.connector
from database import Database


class Shop:
    def __init__(self):
        try:
            self.db = Database("localhost", "root", "")
            self.db.create_database()
            self.db.create_table()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def add_item_to_inventory(self, name, price, quantity):
        try:
            self.db.execute_query(
                "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)",
                (name, price, quantity),
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def sell_item(self, product_name, quantity):
        try:
            item = self.db.fetch_one(
                "SELECT id, price, quantity FROM products WHERE name = %s",
                (product_name,),
            )
            if item is None:
                messagebox.showerror("Error", "Product not found")
                return False

            item_id, price, current_quantity = item
            if current_quantity < quantity:
                messagebox.showerror("Error", "Not enough stock")
                return False

            new_quantity = current_quantity - quantity
            self.db.execute_query(
                "UPDATE products SET quantity = %s WHERE id = %s",
                (new_quantity, item_id),
            )
            total_price = price * quantity
            self.db.execute_query(
                "INSERT INTO sales (product_name, quantity, total_price) VALUES (%s, %s, %s)",
                (product_name, quantity, total_price),
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def view_sales_report(self):
        return self.db.fetch_all("SELECT * FROM sales")

    def display_inventory(self):
        return self.db.fetch_all("SELECT * FROM products")
