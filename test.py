import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor() # responsible for running the query and storing the result

create_table = "CREATE TABLE users (id int, username text, password text)" # make the query
cursor.execute(create_table) # run the query

user = (1, 'san', 'asdf')

insert_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(insert_query, user)

users = [
    (2, 'riley', 'zxcv'),
    (3, 'stan', 'qwer')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * from users"
for row in cursor.execute(select_query):
    print(row)

connection.commit() # save to disk
connection.close()
