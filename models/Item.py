from db import db

class ItemModel(db.Model):

    __tablename__='items'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    price=db.Column(db.Float(precision=2))

    store_id=db.Column(db.Integer,db.ForeignKey('stores.id'))
    '''above line is simple concept of foreign key as we use
    in our rdbms
    
    store_id is actually the id column of stores table
    '''
    store = db.relationship('StoreModel')
    '''
    what this lines does is that it tells  each and every
    ItemModel Object,that  table 'items' has a property store_id
    that belongs to some other table and therefore we can find a
    find a  store in database,that matches this id.
    
     alchemy way of joining two tables
    '''

    def __init__(self,name,price,store_id):
        self.name=name
        self.price=price
        self.store_id=store_id

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod
    def findItemByName(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

