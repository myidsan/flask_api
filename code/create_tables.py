import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# INTEGER is for auto increment columns
create_table = "CREATE TABLE if not EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE if not EXISTS items (name text, price real)"
cursor.execute(create_table)

# cursor.execute("INSERT INTO items values ('test', 10.99)")


connection.commit()
connection.close()
