import sqlite3
from getImageBase24 import get_items

class ECommerceDatabase:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        # Create the `Client` table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Client (
                client_id INTEGER PRIMARY KEY,
                name TEXT,
                surname TEXT,
                address TEXT,
                email TEXT,
                phone TEXT
            )
        ''')

        # Create the `Order` table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS `Order` (
                order_id INTEGER PRIMARY KEY,
                client_id INTEGER,
                items TEXT,
                notes TEXT,
                FOREIGN KEY (client_id) REFERENCES Client(client_id)
            )
        ''')

        # Create the `Category` table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Category (
                category_id INTEGER PRIMARY KEY,
                name TEXT
            )
        ''')

        # Create the `Item` table with new columns
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Item (
                item_id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                category_id INTEGER,
                price REAL,
                image_data BLOB,
                on_special BOOLEAN DEFAULT 0,
                new_price REAL DEFAULT 0,
                new_arrival BOOLEAN DEFAULT 0,
                FOREIGN KEY (category_id) REFERENCES Category(category_id)
            )
        ''')

        # Create the BestSellers table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS BestSellers (
                best_seller_id INTEGER PRIMARY KEY,
                best_seller_rank INTEGER,
                item_id INTEGER,
                FOREIGN KEY (item_id) REFERENCES Item(item_id)
            )
        ''')

        self.connection.commit()

    def populate_category_and_items(self):
        # Dummy data for Category and Item tables (hardware-related)
        categories = [
            ('Tools',),
            ('Building Materials',),
            ('Electrical Supplies',),
            ('Plumbing',),
            ('Paint',),
            ('Garden',),
            ('Hardware',),
            ('Safety Equipment',),
            ('Appliances',),
            ('Automotive',),
        ]

        items = get_items()


        insert_item_query = 'INSERT INTO Item (name, description, category_id, price, image_data, on_special, new_price, new_arrival) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        self.cursor.executemany(insert_item_query, items)
        print("populated table")

        # Insert data into BestSellers table
        best_sellers = [
            (1, 1),
            (2, 2),
            (3, 3),
        ]

        insert_best_sellers_query = 'INSERT INTO BestSellers (best_seller_rank, item_id) VALUES (?, ?)'
        self.cursor.executemany(insert_best_sellers_query, best_sellers)

        # Insert data into Category table
        insert_category_query = 'INSERT INTO Category (name) VALUES (?)'
        self.cursor.executemany(insert_category_query, categories)

        self.connection.commit()


    def close_connection(self):
        self.cursor.close()
        self.connection.close()

if __name__ == '__main__':
    database_file = 'Ha-Chota.db'  # Name of the SQLite database file

    db = ECommerceDatabase(database_file)

    db.create_tables()
    db.populate_category_and_items()
    db.close_connection()
