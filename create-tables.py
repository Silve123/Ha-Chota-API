import sqlite3

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

        items = [
            ('Power Drill', 'High-speed power drill with accessories', 1, 149.99, None, True, 139.99, False),
            ('Lumber Set', 'Assorted lumber for construction projects', 2, 299.99, None, False, 0, False),
            ('Wire and Cable Kit', 'Electrical wiring and cable set', 3, 89.99, None, False, 0, False),
            ('Faucet Kit', 'Complete plumbing faucet set', 4, 39.99, None, False, 0, False),
            ('Screwdriver Set', 'Multi-purpose screwdriver set', 1, 19.99, None, False, 0, False),
            ('Concrete Mix', 'Bag of ready-mix concrete', 2, 49.99, None, False, 0, False),
            ('Maxi Bricks', 'Pallet of Maxi Bricks', 2, 799.99, None, False, 0, False),
            ('Face Bricks', 'Pallet of Face Bricks', 2, 1499.99, None, False, 0, False),
            ('Icon Cement', 'Cement', 2, 99.99, None, False, 0, False),
            ('Circular Saw', 'Powerful circular saw for cutting wood', 1, 249.99, None, False, 0, False),
            ('Tiles', 'Box of ceramic tiles for flooring', 2, 39.99, None, True, 29.99, False),
            ('Light Bulbs', 'Pack of energy-efficient light bulbs', 3, 19.99, None, False, 0, False),
            ('Sink Faucet', 'Single-handle sink faucet', 4, 49.99, None, False, 0, False),
            ('Paint Rollers', 'Set of paint rollers for home projects', 5, 14.99, None, False, 0, False),
            ('Garden Hose', '50-foot garden hose with nozzle', 6, 29.99, None, False, 0, False),
            ('Door Lock', 'High-security door lock with keys', 7, 24.99, None, True, 19.99, False),
            ('Safety Glasses', 'Protective safety glasses', 8, 9.99, None, False, 0, False),
            ('Refrigerator', 'Stainless steel refrigerator', 9, 799.99, None, True, 699.99, False),
            ('Car Battery', 'Automotive battery for cars', 10, 69.99, None, False, 0, False),
            ('Hammer', '16 oz. claw hammer', 1, 12.99, None, False, 0, False),
            ('Plywood Sheets', 'Bundle of plywood sheets', 2, 199.99, None, True, 189.99, False),
            ('Electrical Tape', 'Roll of electrical tape', 3, 4.99, None, False, 0, True),
            ('Shower Head', 'Rainfall shower head', 4, 29.99, None, False, 0, True),
            ('Paint Brushes', 'Set of paint brushes for detail work', 5, 8.99, None, False, 0, True),
            ('Lawn Mower', 'Gas-powered lawn mower', 6, 299.99, None, False, 0, True),
            ('Cabinet Knobs', 'Set of decorative cabinet knobs', 7, 7.99, None, False, 0, True),
            ('Hard Hat', 'Safety hard hat for construction', 8, 14.99, None, False, 0, True),
            ('Microwave Oven', 'Countertop microwave oven', 9, 69.99, None, True, 54.99, True),
            ('Motor Oil', 'Engine oil for vehicles', 10, 12.99, None, False, 0, True),
        ]


        insert_item_query = 'INSERT INTO Item (name, description, category_id, price, image_data, on_special, new_price, new_arrival) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        self.cursor.executemany(insert_item_query, items)

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
