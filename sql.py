import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE posts")
    c.execute("CREATE TABLE posts(title TEXT, description TEXT)")
    c.execute('INSERT INTO posts VALUES("GOod", "I am good!")')
    c.execute('INSERT INTO posts VALUES("Well", "I am well!")')
    c.execute('INSERT INTO posts VALUES("Not Well", "I am Not well!")')