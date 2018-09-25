import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel

'creating a class to addd new users directly'

'this method will be called,when we POST some data to the user register'
class UserRegistration(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="this field cannot be left blank")
    parser.add_argument('password', type=str, required=True, help="password field cannot be left blank")

    def post(self):
        data=UserRegistration.parser.parse_args()

        if UserModel.findByUsername(data['username']):
            return {"message":"User Already Exists"},400

        # user=UserModel(data['username'],data['password'])
        '''modifying above code'''
        user=UserModel(**data)
        user.save_to_db()

        # since data is actually working as a
        # dictionary, we  simply unpacked it

        return {"message":"user created successfully"}
