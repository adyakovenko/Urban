import sqlite3


def clear_db(name):
    connection = sqlite3.connect(f'{name}.db')
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM {name}')
    connection.commit()
    connection.close()


def initiate_dbs():
    initiate_db_products()
    clear_db('Products')
    initiate_db_products()
    initiate_db_users()
    clear_db('Users')
    initiate_db_users()



def initiate_db_products():
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


def initiate_db_users():
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )''')
    connection.commit()
    connection.close()


# functions for products
def add_product(title, description, price):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Products (title, description, price) VALUES ((?), (?), (?))', (title, description, price,))
    connection.commit()
    connection.close()


def add_products(products):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    for product in products:
        cursor.execute('INSERT INTO Products (title, description, price) VALUES ((?), (?), (?))', (product.name, product.description, product.price))
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


def get_products_names():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    names = []
    for p in products:
        names.append(p[1])
    connection.close()
    return names


# functions for users
def add_user(username, email, age):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES ((?), (?), (?), 1000)', (username, email, age))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    if cursor.execute(('SELECT COUNT(*) FROM Users')).fetchone()[0] == 0:
        connection.close()
        return False
    users = cursor.execute('SELECT * FROM Users').fetchall()
    connection.close()
    for user in users:
        if user[1] == username:
            return True
    return False
