'''

in this model class,
 i will add methods,that do not actually belong to the Resource class: ITEM



'''

import sqlite3


class ItemModel():

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def json(self):
        return {'name':self.name,'price':self.price}


    def findItemByName(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "select * from items where name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row is not None:
            return {"item": {'name': row[0], 'price': row[1]}}


    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "insert into items values (?,?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()


    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        upd_query = "update items set price=? where name=?"
        cursor.execute(upd_query, (item['price'], item['name']))
