# submit_order.py - Simple Purchase Order Submission GUI
# This script provides a minimal Tkinter GUI for submitting a new purchase order to the database.
# All code follows PEP 8 standards and is commented for beginner-level users.

import os
import sqlite3
import tkinter as tk
from tkinter import messagebox

# Get absolute path to the database file for reliability
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parts_inventory.db")

# Connect to SQLite Database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Function to submit a purchase order to the database
# This function is called when the user clicks the Submit button
# Tip: Always validate user input before inserting into the database

def submit_order():
    purchase_order_number = entry_po.get()
    company = entry_company.get()
    requested_by = entry_requester.get()
    status = entry_status.get()

    # Insert the new purchase order into the database
    cursor.execute(
        "INSERT INTO purchase_orders (purchase_order_number, company, requested_by, status) VALUES (?, ?, ?, ?)",
        (purchase_order_number, company, requested_by, status)
    )
    conn.commit()
    messagebox.showinfo("Success", "Purchase Order Added!")

# GUI Setup
# This section creates the main window and entry fields for the form

root = tk.Tk()
root.title("New Purchase Order")

# Entry fields for purchase order details
# Tip: Add more fields as needed for your workflow

tk.Label(root, text="PO Number:").grid(row=0, column=0)
entry_po = tk.Entry(root)
entry_po.grid(row=0, column=1)

tk.Label(root, text="Company:").grid(row=1, column=0)
entry_company = tk.Entry(root)
entry_company.grid(row=1, column=1)

tk.Label(root, text="Requested By:").grid(row=2, column=0)
entry_requester = tk.Entry(root)
entry_requester.grid(row=2, column=1)

tk.Label(root, text="Status:").grid(row=3, column=0)
entry_status = tk.Entry(root)
entry_status.grid(row=3, column=1)

# Submit button to send the order to the database
# Tip: Consider adding a Cancel button to clear the form or exit

tk.Button(root, text="Submit", command=submit_order).grid(row=4, column=0, columnspan=2)

# Start the GUI event loop
# This line is essential for the window to appear and respond to user actions

root.mainloop()