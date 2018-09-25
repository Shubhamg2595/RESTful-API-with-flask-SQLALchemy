import sqlite3
from db import db

class UserModel(db.Model):
    """next thing we need to do is tell SQLALchemy
    the tablenames ,where these models are going to
    be stored
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    # '''
    # we also need to tell sqlalchemy about the columns
    # that our table will contain/or contains
    # '''

    def __init__(self,username,password):
        self.username=username
        self.password=password
    # REASON I REMOvED ID from init method is bcoz
    # id is autoincrementing and so whenever a new object
    # of user is created,id is automatically assigned to that
    # id

    @classmethod
    def findByUsername(cls,username):
        # '''NEW CODE USING SQL ALCHEMY'''
        return cls.query.filter_by(username=username).first()

    @classmethod
    def findByUseId(cls,_id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


