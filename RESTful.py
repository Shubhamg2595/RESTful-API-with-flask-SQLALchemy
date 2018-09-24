from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegistration
from resources.Item import Item,ItemList
app=Flask(__name__)
'create a secret key for your app'
app.secret_key='shubham:)'
api=Api(app)

jwt=JWT(app,authenticate,identity)


'''
in this commit,
i will make the entire item class storage and retrieval process with database
'''



api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegistration,'/register')
if __name__ == '__main__':
    app.run(port=5000,debug=True)