# Parts Inventory Management System

Welcome to the Parts Inventory Management System! This application is designed to help engineering and maintenance teams track, manage, and organize parts, purchase orders, quotes, and company/vendor information. It features a user-friendly graphical interface and a robust backend using Python and SQLite.

---

## User Guide: How to Use This System

### Getting Started

1. **Install Python 3.8 or newer** on your computer.
2. **(Optional but recommended)** Create a virtual environment:

   ```pwsh
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. **Install required dependencies:**

   ```pwsh
   pip install -r requirements.txt
   ```

   This will install all necessary Python packages, including Pillow for image support.

4. **Run the graphical interface:**

   ```pwsh
   python user_interface.py
   ```

   The main menu will appear, allowing you to add purchase orders, parts, quotes, and companies.

### Using the GUI

- **Select an action** from the main menu (e.g., Add Purchase Order, Add Part to Inventory).
- **Fill in the form fields** in the window that opens. Required fields are marked with an asterisk (*), and guidance is provided for each field (e.g., date format, integer, unique).
- **Submit** the form to add the record to the database. You will see a confirmation message if successful.
- **Repeat** for other actions as needed.

### Command-Line Interface (Advanced)

You can also use the command-line interface for batch operations or automation:

```pwsh
python main.py <command> [options]
```

Examples:

- Add a part:

  ```pwsh
  python main.py add_parts --name "Widget" --model_number "W123" --qty 10
  ```

- List all parts:

  ```pwsh
  python main.py list_parts
  ```

- Update, get, or delete records for any table using the appropriate command.

---

## For Developers: Adapting This System for Your Company

If you want to use this system for your own organization, here’s how to get started:

1. **Clone or download this repository** to your local machine.
2. **Review the database structure** in `database-structure-only-250515-0744.html` or the included `.db` file. You can modify the schema using SQLite tools if needed.
3. **Customize the GUI:**
   - Update field labels, add/remove fields, or change validation in `user_interface.py`.
   - Replace the logo (`huhtamaki_logo_transparent_880x222.png`) with your own company’s logo (use the same filename or update the path in the code).
4. **Update business logic:**
   - Add new tables or relationships in `main.py` and `user_interface.py` as needed.
   - Adjust validation, required fields, or add new features.
5. **Test thoroughly** to ensure the system works for your workflow.
6. **Publish or share** with your team!

---

## Program Overview & File Structure

### What This Program Does

- Provides a minimalist, scalable inventory management system for parts, purchase orders, quotes, and companies.
- Supports both a graphical user interface (GUI) for everyday users and a command-line interface (CLI) for advanced users or automation.
- Maintains data integrity and relationships using SQLite, with clear validation and user guidance.
- Designed for easy customization and learning, with beginner-friendly comments and modular code.

### File Descriptions

- **`user_interface.py`**: The main graphical interface. Users can add records to any table using simple forms. Includes company branding and field guidance.
- **`main.py`**: The command-line interface and core database logic. Supports CRUD operations for all tables. Useful for automation, scripting, or advanced users.
- **`parts_inventory.db`**: The SQLite database file where all records are stored. Can be opened with SQLite tools for direct inspection or backup.
- **`requirements.txt`**: Lists all Python dependencies needed to run the program (install with `pip install -r requirements.txt`).
- **`huhtamaki_logo_transparent_880x222.png`**: The default company logo used in the GUI. Replace with your own logo as needed.
- **`database-structure-only-250515-0744.html`**: An HTML export of the current database schema for easy reference.
- **`submit_order.py`**: (Optional) Example script for submitting a purchase order via a simple Tkinter form.
- **`README.md`**: This guide and documentation.

### Structure & Extensibility

- All code follows PEP 8 and is modular for easy updates.
- Adding new tables or fields is straightforward—update the schema and add corresponding form fields.
- The GUI and CLI are kept separate for clarity and maintainability.
- All file paths are handled as absolute paths for reliability.

---

## License

MIT License

---

If you have any questions or want to contribute, feel free to open an issue or pull request. Enjoy managing your parts inventory!
