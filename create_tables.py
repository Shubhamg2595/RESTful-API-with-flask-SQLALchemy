import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()


create_table= "create table if not exists users(id INTEGER PRIMARY KEY,username text,password text)"
cursor.execute(create_table)

create_item_table="create table if not exists items(id INTEGER PRIMARY KEY,name text,price real)"
cursor.execute(create_item_table)

# 'inserting a sample item'
# cursor.execute("insert into items values ('sample item',10.99)")

connection.commit()
connection.close()


