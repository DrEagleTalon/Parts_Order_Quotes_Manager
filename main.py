import sqlite3
from typing import Dict, Any

DB_NAME = 'parts_inventory.db'

def get_table_fields() -> Dict[str, Dict[str, str]]:
    return {
        'parts': {
            'primary_key': 'INTEGER PRIMARY KEY',
            'name': 'TEXT',
            'model_number': 'TEXT',
            'description': 'NUMERIC',
            'other_identifying': 'TEXT',
            'qty': 'INTEGER',
            'quantity_difference': 'TEXT',
            'job_number': 'TEXT',
            'manufacturer': 'TEXT',
            'model_name': 'TEXT',
            'serial_number': 'TEXT',
            'price_per_unit': 'REAL',
            'our_part_number': 'TEXT',
            'purchase_order_number': 'TEXT',
            'order_date': 'TEXT',
            'shipment_received_date': 'TEXT',
        },
        'companies': {
            'company_name': 'TEXT PRIMARY KEY',
            'address': 'TEXT',
            'contact_email': 'TEXT',
            'support_email': 'TEXT',
            'phone': 'TEXT',
            'field_of_service': 'TEXT',
            'website': 'TEXT',
        },
        'projects': {
            'job_number': 'TEXT',
            'project_name': 'TEXT',
            'description': 'TEXT',
            'start_date': 'DATE',
            'end_date': 'DATE',
            'lead': 'TEXT',
            'area': 'TEXT',
            'status': 'TEXT',
        },
        'purchase_orders': {
            'purchase_order_number': 'TEXT PRIMARY KEY',
            'quote_number': 'TEXT',
            'company': 'TEXT',
            'project_name': 'TEXT',
            'date_purchased': 'DATE',
            'requested_by': 'TEXT',
            'agent': 'TEXT',
            'total_cost': 'REAL',
            'shipping_method': 'TEXT',
            'expected_delivery': 'DATE',
            'payment_terms': 'TEXT',
            'status': 'TEXT',
        },
        'parts_orders': {
            'model_number': 'TEXT',
            'id': 'INTEGER PRIMARY KEY',
            'status': 'TEXT',
            'reference_number': 'TEXT',
            'job': 'TEXT',
            'purchase_order_number': 'TEXT',
            'description': 'TEXT',
            'quantity': 'INTEGER',
            'cost_per_unit': 'REAL',
        },
        'quotes': {
            'quote_number': 'TEXT PRIMARY KEY',
            'company': 'TEXT',
            'project_name': 'TEXT',
            'date_quoted': 'DATE',
            'requested_by': 'TEXT',
            'agent': 'TEXT',
            'estimated_total_cost': 'REAL',
            'expiration_date': 'DATE',
            'status': 'TEXT',
        },
    }

def init_db():
    tables = get_table_fields()
    with sqlite3.connect(DB_NAME) as conn:
        for table, fields in tables.items():
            columns = ', '.join([f'{k} {v}' for k, v in fields.items()])
            conn.execute(f'CREATE TABLE IF NOT EXISTS {table} ({columns})')
        conn.commit()

def add_row(table: str, data: Dict[str, Any]):
    fields = get_table_fields()[table]
    keys = ', '.join(fields.keys())
    placeholders = ', '.join(['?' for _ in fields])
    values = [data.get(k) for k in fields]
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(f'INSERT INTO {table} ({keys}) VALUES ({placeholders})', values)
        conn.commit()

def list_rows(table: str):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(f'SELECT * FROM {table}')
        return cursor.fetchall()

def get_row(table: str, pk_value: Any):
    fields = get_table_fields()[table]
    pk = next((k for k, v in fields.items() if 'PRIMARY KEY' in v), list(fields.keys())[0])
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(f'SELECT * FROM {table} WHERE {pk} = ?', (pk_value,))
        return cursor.fetchone()

def update_row(table: str, pk_value: Any, data: Dict[str, Any]):
    fields = get_table_fields()[table]
    pk = next((k for k, v in fields.items() if 'PRIMARY KEY' in v), list(fields.keys())[0])
    set_clause = ', '.join([f'{k} = ?' for k in fields if k != pk])
    values = [data.get(k) for k in fields if k != pk]
    values.append(pk_value)
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(f'UPDATE {table} SET {set_clause} WHERE {pk} = ?', values)
        conn.commit()

def delete_row(table: str, pk_value: Any):
    fields = get_table_fields()[table]
    pk = next((k for k, v in fields.items() if 'PRIMARY KEY' in v), list(fields.keys())[0])
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(f'DELETE FROM {table} WHERE {pk} = ?', (pk_value,))
        conn.commit()

if __name__ == '__main__':
    import argparse
    init_db()
    parser = argparse.ArgumentParser(description='Parts Inventory Management')
    subparsers = parser.add_subparsers(dest='command')

    tables = get_table_fields().keys()
    for table in tables:
        # Add
        add_parser = subparsers.add_parser(f'add_{table}')
        for field in get_table_fields()[table]:
            add_parser.add_argument(f'--{field}', required=False)
        # List
        subparsers.add_parser(f'list_{table}')
        # Get
        get_parser = subparsers.add_parser(f'get_{table}')
        pk = next((k for k, v in get_table_fields()[table].items() if 'PRIMARY KEY' in v), list(get_table_fields()[table].keys())[0])
        get_parser.add_argument(pk)
        # Update
        update_parser = subparsers.add_parser(f'update_{table}')
        update_parser.add_argument(pk)
        for field in get_table_fields()[table]:
            if field != pk:
                update_parser.add_argument(f'--{field}', required=False)
        # Delete
        delete_parser = subparsers.add_parser(f'delete_{table}')
        delete_parser.add_argument(pk)

    args = parser.parse_args()
    for table in tables:
        pk = next((k for k, v in get_table_fields()[table].items() if 'PRIMARY KEY' in v), list(get_table_fields()[table].keys())[0])
        if args.command == f'add_{table}':
            data = {k: getattr(args, k) for k in get_table_fields()[table]}
            add_row(table, data)
            print(f'{table.capitalize()} row added.')
        elif args.command == f'list_{table}':
            for row in list_rows(table):
                print(row)
        elif args.command == f'get_{table}':
            pk_value = getattr(args, pk)
            row = get_row(table, pk_value)
            print(row)
        elif args.command == f'update_{table}':
            pk_value = getattr(args, pk)
            data = {k: getattr(args, k) for k in get_table_fields()[table] if k != pk}
            update_row(table, pk_value, data)
            print(f'{table.capitalize()} row updated.')
        elif args.command == f'delete_{table}':
            pk_value = getattr(args, pk)
            delete_row(table, pk_value)
            print(f'{table.capitalize()} row deleted.')
    else:
        if not args.command:
            parser.print_help()
