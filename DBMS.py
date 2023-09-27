import sqlite3

def get_specials():
    try:
        connection = sqlite3.connect('Ha-Chota.db')  # Replace with your database file path
        cursor = connection.cursor()

        # Retrieve items on special from the database
        cursor.execute('SELECT name, description, price, new_price, image_data FROM Item WHERE on_special = 1')
        special_items = cursor.fetchall()

        specials_list = []
        for item in special_items:
            item_dict = {
                'name': item[0],
                'description': item[1],
                'price': item[2],
                'new_price': item[3],  # Include the new price in the JSON
                'image_data': item[4],
            }
            specials_list.append(item_dict)

        return specials_list

    except sqlite3.Error as e:
        print("Database error:", e)
        return None

    finally:
        if connection:
            connection.close()


def get_new_arrivals():
    try:
        connection = sqlite3.connect('Ha-Chota.db')  # Replace with your database file path
        cursor = connection.cursor()

        # Retrieve new arrival items from the database
        cursor.execute('SELECT name, description, price, image_data FROM Item WHERE new_arrival = 1')
        new_arrival_items = cursor.fetchall()

        new_arrivals_list = []
        for item in new_arrival_items:
            item_dict = {
                'name': item[0],
                'description': item[1],
                'price': item[2],
                'image_data': item[3],
            }
            new_arrivals_list.append(item_dict)

        return new_arrivals_list

    except sqlite3.Error as e:
        print("Database error:", e)
        return None

    finally:
        if connection:
            connection.close()


def get_best_sellers():
    try:
        connection = sqlite3.connect('Ha-Chota.db')  # Replace with your database file path
        cursor = connection.cursor()

        # Retrieve best-selling items from the database
        cursor.execute('''
            SELECT i.name, i.description, i.price, i.image_data, b.best_seller_rank
            FROM Item AS i
            JOIN BestSellers AS b ON i.item_id = b.item_id
            ORDER BY b.best_seller_rank
        ''')
        best_seller_items = cursor.fetchall()

        best_sellers_list = []
        for item in best_seller_items:
            item_dict = {
                'name': item[0],
                'description': item[1],
                'price': item[2],
                'image_data': item[3],
                'best_seller_rank': item[4],  # Include the rank in the JSON
            }
            best_sellers_list.append(item_dict)

        return best_sellers_list

    except sqlite3.Error as e:
        print("Database error:", e)
        return None

    finally:
        if connection:
            connection.close()


def get_categories_and_items():
    try:
        connection = sqlite3.connect('Ha-Chota.db')  # Replace with your database file path
        cursor = connection.cursor()

        # Retrieve categories and items from the database
        cursor.execute('SELECT category_id, name FROM Category')
        categories = cursor.fetchall()

        categories_dict = {}
        for category_id, category_name in categories:
            cursor.execute('SELECT name, description, price, image_data FROM Item WHERE category_id = ?', (category_id,))
            items = cursor.fetchall()

            items_list = []
            for item in items:
                item_dict = {
                    'name': item[0],
                    'description': item[1],
                    'price': item[2],
                    'image_data': item[3],
                }
                items_list.append(item_dict)

            categories_dict[category_name] = items_list

        return categories_dict

    except sqlite3.Error as e:
        print("Database error:", e)
        return None

    finally:
        if connection:
            connection.close()