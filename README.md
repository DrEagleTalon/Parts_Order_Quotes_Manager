# Parts Inventory Management System

This project is a Python-based inventory management system for tracking parts related to Purchase Orders and Requisitions. It uses SQLite for data storage and is designed to help manage parts for builds and machines, including handling returns, upgrades, and detailed part tracking.

## Features

- Store and manage information about each part:
  - Name
  - Model number
  - Model name
  - Manufacturer
  - Serial number
  - Quantity
  - Price per unit
  - Our part number
  - Other identifying numbers or names
  - Job number
  - Description
  - Order number
  - Order date
  - Shipment received date
  - (and more as needed)
- Support for CRUD operations (Create, Read, Update, Delete)
- Command-line interface

## Getting Started

1. Ensure you have Python 3.8+ installed.
2. (Optional) Create a virtual environment:

   ```pwsh
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```pwsh
   pip install -r requirements.txt
   ```

4. Run the main script:

   ```pwsh
   python main.py <command> [options]
   ```

## Usage Examples

### Add a Part

```pwsh
python main.py add --name "Widget" --model_number "W123" --model_name "Widget Pro" --manufacturer "Acme" --serial_number "SN001" --quantity 10 --price_per_unit 25.50 --our_part_number "OPN-001" --other_identifying "Alt-123" --job_number "J1001" --description "Standard widget" --order_number "PO12345" --order_date "2025-05-14" --shipment_received_date "2025-05-15"
```

### List All Parts

```pwsh
python main.py list
```

### Get a Part by ID

```pwsh
python main.py get 1
```

### Update a Part

```pwsh
python main.py update 1 --quantity 15 --description "Updated widget description"
```

### Delete a Part

```pwsh
python main.py delete 1
```

## Notes

- All fields are optional except for the command and, where required, the part ID (for get, update, delete).
- Dates should be in `YYYY-MM-DD` format.
- You can add or update any field by specifying it as an argument.
- The database file `parts_inventory.db` will be created in the project directory.

## License

MIT Licens

"primary_key" INTEGER,
"name" TEXT,
"model_number" TEXT,
"description" NUMERIC,
"other_identifying" TEXT,
"quantity" INTEGER,
"quantity_difference" TEXT,
"job_number" TEXT,
"manufacturer" TEXT,
"model_name" TEXT,
"serial_number" TEXT,
"price_per_unit" REAL,
"our_part_number" TEXT,
"order_number" TEXT,
"order_date" TEXT,
"shipment_received_date" TEXT,
PRIMARY KEY("primary_key")
