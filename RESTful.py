from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegistration
from resources.Item import Item,ItemList

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.secret_key='shubham:)'
api=Api(app)

'''
# remove create_table and db script from the
database....

USE OF BEFORE_FIRST_REQUEST:
now i dont need the create_tables script and 
data.db as 
.db file will be created automatically 
by sqlalchemy now,when the first response is given
by our api.


that is the sole purpose of below annotation..



d'''
@app.before_first_request
def create_tables():
    db.create_all()


jwt=JWT(app,authenticate,identity)


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegistration,'/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

