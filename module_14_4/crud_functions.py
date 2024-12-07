import sqlite3

def clear_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Products')
    connection.commit()
    connection.close()

def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    )''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    prints = []
    for p in products:
        prints.append(f'Название: {p[1]} | Описание: {p[2]} | Цена: {p[3]}')
    connection.close()
    return prints

def add_product(title, description, price):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Products (title, description, price) VALUES ((?), (?), (?))', (title, description, price,))
    connection.commit()
    connection.close()

