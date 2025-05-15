import os
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Get absolute path to the database file
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parts_inventory.db")

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create the main window
root = tk.Tk()
root.title("Parts Inventory Management - Main Menu")
tk.Label(root, text="Select an action:").pack(pady=10)

def add_banner(win):
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "huhtamaki_logo_transparent_880x222.png")
    if os.path.exists(logo_path):
        img = Image.open(logo_path)
        img = img.resize((220, 55))  # Resize as needed for window
        photo = ImageTk.PhotoImage(img)
        logo_label = tk.Label(win, image=photo)
        logo_label.image = photo  # Keep a reference!
        logo_label.pack(pady=(10, 0))
    tk.Label(win, text="Huhtamaki", font=("Arial", 18, "bold")).pack(pady=(5, 15))

def open_purchase_order_window():
    win = tk.Toplevel(root)
    win.title("Add Purchase Order")
    add_banner(win)
    form_frame = tk.Frame(win)
    form_frame.pack(padx=10, pady=10)
    fields = [
        ("PO Number* (unique, e.g. PO1234)", "purchase_order_number"),
        ("Quote Number (e.g. Q5678)", "quote_number"),
        ("Company*", "company"),
        ("Project Name", "project_name"),
        ("Date Purchased (YYYY-MM-DD)", "date_purchased"),
        ("Requested By*", "requested_by"),
        ("Agent", "agent"),
        ("Total Cost (real, e.g. 1234.56)", "total_cost"),
        ("Shipping Method", "shipping_method"),
        ("Expected Delivery (YYYY-MM-DD)", "expected_delivery"),
        ("Payment Terms", "payment_terms"),
        ("Status*", "status"),
    ]
    entries = {}
    for i, (label, key) in enumerate(fields):
        tk.Label(form_frame, text=label).grid(row=i, column=0, sticky='e')
        entry = tk.Entry(form_frame)
        entry.grid(row=i, column=1)
        entries[key] = entry
    def submit():
        values = {k: entries[k].get() for _, k in fields}
        required = ["purchase_order_number", "company", "requested_by", "status"]
        if not all(values[k] for k in required):
            messagebox.showerror("Error", "Fields marked with * are required!")
            return
        try:
            if values['total_cost']:
                float(values['total_cost'])
            if values['date_purchased']:
                assert len(values['date_purchased']) == 10
            if values['expected_delivery']:
                assert len(values['expected_delivery']) == 10
        except Exception:
            messagebox.showerror("Error", "Check number/date formats!")
            return
        cursor.execute("""
            INSERT INTO purchase_orders (
                purchase_order_number, quote_number, company, project_name, date_purchased, requested_by, agent, total_cost, shipping_method, expected_delivery, payment_terms, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [values[k] for _, k in fields])
        conn.commit()
        messagebox.showinfo("Success", "Purchase Order Added!")
        win.destroy()
    tk.Button(form_frame, text="Submit", command=submit).grid(row=len(fields), column=0, columnspan=2)

def open_parts_window():
    win = tk.Toplevel(root)
    win.title("Add Part to Inventory")
    add_banner(win)
    form_frame = tk.Frame(win)
    form_frame.pack(padx=10, pady=10)
    fields = [
        ("Name*", "name"),
        ("Model Number* (unique)", "model_number"),
        ("Description", "description"),
        ("Other Identifying", "other_identifying"),
        ("Qty* (integer, e.g. 5)", "qty"),
        ("Quantity Difference", "quantity_difference"),
        ("Job Number", "job_number"),
        ("Manufacturer", "manufacturer"),
        ("Model Name", "model_name"),
        ("Serial Number", "serial_number"),
        ("Price Per Unit (real, e.g. 12.34)", "price_per_unit"),
        ("Our Part Number", "our_part_number"),
        ("Purchase Order Number", "purchase_order_number"),
        ("Order Date (YYYY-MM-DD)", "order_date"),
        ("Shipment Received Date (YYYY-MM-DD)", "shipment_received_date"),
    ]
    entries = {}
    for i, (label, key) in enumerate(fields):
        tk.Label(form_frame, text=label).grid(row=i, column=0, sticky='e')
        entry = tk.Entry(form_frame)
        entry.grid(row=i, column=1)
        entries[key] = entry
    def submit():
        values = {k: entries[k].get() for _, k in fields}
        required = ["name", "model_number", "qty"]
        if not all(values[k] for k in required):
            messagebox.showerror("Error", "Fields marked with * are required!")
            return
        try:
            int(values['qty'])
            if values['price_per_unit']:
                float(values['price_per_unit'])
        except Exception:
            messagebox.showerror("Error", "Qty must be integer, price must be real!")
            return
        cursor.execute("""
            INSERT INTO parts (
                name, model_number, description, other_identifying, qty, quantity_difference, job_number, manufacturer, model_name, serial_number, price_per_unit, our_part_number, purchase_order_number, order_date, shipment_received_date
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [values[k] for _, k in fields])
        conn.commit()
        messagebox.showinfo("Success", "Part Added!")
        win.destroy()
    tk.Button(form_frame, text="Submit", command=submit).grid(row=len(fields), column=0, columnspan=2)

def open_quote_window():
    win = tk.Toplevel(root)
    win.title("Add Quote")
    add_banner(win)
    form_frame = tk.Frame(win)
    form_frame.pack(padx=10, pady=10)
    fields = [
        ("Quote Number* (unique)", "quote_number"),
        ("Company*", "company"),
        ("Project Name", "project_name"),
        ("Date Quoted (YYYY-MM-DD)", "date_quoted"),
        ("Requested By", "requested_by"),
        ("Agent", "agent"),
        ("Estimated Total Cost (real, e.g. 123.45)", "estimated_total_cost"),
        ("Expiration Date (YYYY-MM-DD)", "expiration_date"),
        ("Status", "status"),
    ]
    entries = {}
    for i, (label, key) in enumerate(fields):
        tk.Label(form_frame, text=label).grid(row=i, column=0, sticky='e')
        entry = tk.Entry(form_frame)
        entry.grid(row=i, column=1)
        entries[key] = entry
    def submit():
        values = {k: entries[k].get() for _, k in fields}
        required = ["quote_number", "company"]
        if not all(values[k] for k in required):
            messagebox.showerror("Error", "Fields marked with * are required!")
            return
        try:
            if values['estimated_total_cost']:
                float(values['estimated_total_cost'])
        except Exception:
            messagebox.showerror("Error", "Estimated Total Cost must be a number!")
            return
        cursor.execute("""
            INSERT INTO quotes (
                quote_number, company, project_name, date_quoted, requested_by, agent, estimated_total_cost, expiration_date, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [values[k] for _, k in fields])
        conn.commit()
        messagebox.showinfo("Success", "Quote Added!")
        win.destroy()
    tk.Button(form_frame, text="Submit", command=submit).grid(row=len(fields), column=0, columnspan=2)

def open_company_window():
    win = tk.Toplevel(root)
    win.title("Add Company")
    add_banner(win)
    form_frame = tk.Frame(win)
    form_frame.pack(padx=10, pady=10)
    fields = [
        ("Company Name* (unique)", "company_name"),
        ("Address", "address"),
        ("Contact Email", "contact_email"),
        ("Support Email", "support_email"),
        ("Phone", "phone"),
        ("Field of Service", "field_of_service"),
        ("Website", "website"),
    ]
    entries = {}
    for i, (label, key) in enumerate(fields):
        tk.Label(form_frame, text=label).grid(row=i, column=0, sticky='e')
        entry = tk.Entry(form_frame)
        entry.grid(row=i, column=1)
        entries[key] = entry
    def submit():
        values = {k: entries[k].get() for _, k in fields}
        if not values['company_name']:
            messagebox.showerror("Error", "Company Name is required!")
            return
        cursor.execute("""
            INSERT INTO companies (
                company_name, address, contact_email, support_email, phone, field_of_service, website
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [values[k] for _, k in fields])
        conn.commit()
        messagebox.showinfo("Success", "Company Added!")
        win.destroy()
    tk.Button(form_frame, text="Submit", command=submit).grid(row=len(fields), column=0, columnspan=2)

actions = [
    ("Add Purchase Order", open_purchase_order_window),
    ("Add Part to Inventory", open_parts_window),
    ("Add Quote", open_quote_window),
    ("Add Company", open_company_window),
]
for text, command in actions:
    tk.Button(root, text=text, width=30, command=command).pack(pady=5)

root.mainloop()