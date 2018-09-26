from db import db

class StoreModel(db.Model):

    __tablename__='stores'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))

    items=db.relationship('ItemModel',lazy='dynamic')

    '''
    what this line does is that, when this code is encountered,
    it tells us that a store  contain number of items
    and the two tables have been joined
    if we have many stores and many items,
    thus if a  store  has 5 items,
    than 5 itemModel object will be created
    but this problem can be countered using
    lazy=dynamic,what it does is that self.items
    does not actually create a list of items 
    but actually acts like a query builder,which fetches data directly from
    database 
    
    '''

    def __init__(self,name,price):
        self.name=name

    def json(self):
        return {'name':self.name,'items':[item.json() for item in  self.items.all()]}

    @classmethod
    def findItemByName(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

