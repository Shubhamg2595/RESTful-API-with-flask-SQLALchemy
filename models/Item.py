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

    @classmethod
    def findItemByName(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "select * from items where name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row :
            return cls(*row)


    def insert(self):
        print('in insert()',self.name)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "insert into items values(?,?)"
        cursor.execute(query, (self.name,self.price))

        connection.commit()
        connection.close()


    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        upd_query = "update items set price=? where name=?"
        cursor.execute(upd_query, (self.price, self.name))
