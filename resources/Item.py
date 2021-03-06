import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.Item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="this field cannot be left blank")
    parser.add_argument('store_id', type=int, required=True, help="tvery item needs a store_id")

    # '''instead of fetching items data in get() method, we will create a classmethod() to ' \
# 'do the same thing and then we will this class method in our get() ,post() and other methods as per requirement '''



    # @jwt_required()
    def get(self,name):
        item=ItemModel.findItemByName(name)
        if item:
            return item.json()
        return {"message":"item not found"},404


    def post(self,name):
        if ItemModel.findItemByName(name):
            return {"message":"an item with name {} already exists in the itemList.".format(name)}

        data=Item.parser.parse_args()

        # item=ItemModel(name,data['price'],data['store_id'])
        '''way2'''
        item = ItemModel(name, **data)
        # print(item.name)
        try:
            # print(item.name)
            item.save_to_db()
        except:
            return {"message":"An error occured inserting the item"},500

        return item.json(),201




    def delete(self,name):
        item = Item.findItemByName(name)
        if item:
            item.delete_from_db()

        return {'message':'item deleted'}

    def put(self,name):
        data=Item.parser.parse_args()

        item=ItemModel.findItemByName(name)

        if item is None:
            # item=ItemModel(name,data['price'],data['store_id'])
            '''way2'''
            item=ItemModel(name,**data)
        else:
            item.price=data['price']

        item.save_to_db()

        return item.json()



class ItemList(Resource):
    def get(self):
        return {'items':list(map(lambda x:x.json(),ItemModel.query.all()))}