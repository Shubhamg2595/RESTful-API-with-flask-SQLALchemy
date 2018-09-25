'''
REASON I AM EXTENDING ITEMMODEL WITH DB.MODEL AND
SAME WITH USERMODEL IS TO TELL SQLALCHEMY ENTITY
TO CREATE A MAPPING BETWEEN OBJECTS OF ITEMMODEL
AND USERMODEL AND THE DATABASE

in simply way, i am simply telling ORM SQLALCHEMY
that objects of itemmodel and usermodel are the one
that should be mapped to the database.
'''

from db import db

class ItemModel(db.Model):

    __tablename__='items'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    price=db.Column(db.Float(precision=2))

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod
    def findItemByName(cls,name):
        # ''''NEW CODE USING SQL ALCHEMY'''
        return cls.query.filter_by(name=name).first()

        # 'above code simply returns a itemModel Object'

        # '''CODE BEFORE SQL ALCHEMY'''
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "select * from items where name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        #
        # if row :
        #     return cls(*row)


    def save_to_db(self):
        # ''''NEW CODE USING SQL ALCHEMY'''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        # '''ONE MAJOR ADVANTAGE OF ABOVE LINE IS THAT
        # SQL ALCHEMY IS ACTUALLY PERFORMING UPSERTING
        # WHAT THIS MEANS IS THAT IF DATA IS  NOT PRESENT
        # IN DB,ALCHEMY WILL INSERT IT,OTHERWISE IT WILL UPDATE THE EXISTING
        # DATA
        #
        # WHAT THIS MEANS IS THAT  WE DONT ACTUALLY NEED A UPDATE()
        # METHOD SEPARATELY....
        # '''
        #
        # '''what above code means is that
        #  using alchemy we are dealing directly with
        #  ITEMMMODEL object, we  can simply insert that
        #  object in the database....
        #  '''
        # 'INSERTION CODE BEFORE SQLALCHEMY'
        # print('in insert()',self.name)
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "insert into items values(?,?)"
        # cursor.execute(query, (self.name,self.price))
        #
        # connection.commit()
        # connection.close()

