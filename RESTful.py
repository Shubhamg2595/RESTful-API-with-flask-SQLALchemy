from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegistration
from resources.Item import Item,ItemList
app=Flask(__name__)
'create a secret key for your app'
'''
'important to specify this property for sqlAlchemy' \
'as sqlalchemy is always tracking the changes that' \
'we make to our database, but that consumes a lot' \
'of resources' 
'''
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.secret_key='shubham:)'
api=Api(app)

jwt=JWT(app,authenticate,identity)


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegistration,'/register')
'''REASON I IMPORTED THE 'db' here is because of
    circular imports
    '''
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

