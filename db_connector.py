import sqlite3
from models import Warehouse, Product

class DBConnector:
    def __init__(self, db_name='warehouse.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS warehouses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                address TEXT,
                created_at TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                category TEXT,
                price REAL,
                supplier TEXT,
                created_at TEXT
            )
        ''')

        self.conn.commit()

    def insert_warehouse(self, warehouse):
        self.cursor.execute('''
            INSERT INTO warehouses (name, description, address, created_at) 
            VALUES (?, ?, ?, ?)
        ''', (warehouse.name, warehouse.description, warehouse.address, warehouse.created_at))

        self.conn.commit()

    def insert_product(self, product):
        self.cursor.execute('''
            INSERT INTO products (name, description, category, price, supplier, created_at) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (product.name, product.description, product.category, product.price, product.supplier, product.created_at))

        self.conn.commit()

    def get_warehouses(self):
        self.cursor.execute('SELECT * FROM warehouses')
        rows = self.cursor.fetchall()
        return [Warehouse(*row[1:]) for row in rows]

    def get_products(self):
        self.cursor.execute('SELECT * FROM products')
        rows = self.cursor.fetchall()
        return [Product(*row[1:]) for row in rows]

    def get_warehouse_by_id(self, id):
        self.cursor.execute('SELECT * FROM warehouses WHERE id = ?', (id,))
        row = self.cursor.fetchone()
        return Warehouse(*row[1:])

    def get_product_by_id(self, id):
        self.cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
        row = self.cursor.fetchone()
        return Product(*row[1:])
