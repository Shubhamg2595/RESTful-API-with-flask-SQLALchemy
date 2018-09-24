import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.Item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="this field cannot be left blank")

# '''instead of fetching items data in get() method, we will create a classmethod() to ' \
# 'do the same thing and then we will this class method in our get() ,post() and other methods as per requirement '''



    # @jwt_required()
    def get(self,name):
        item=ItemModel.findItemByName(name)
        if item:
            return item
        return {"message":"item not found"},404


    def post(self,name):
        if ItemModel.findItemByName(name):
            return {"message":"an item with name {} already exists in the itemList.".format(name)}

        data=Item.parser.parse_args()

        item={'name':name,'price':data['price']}
        try:
            ItemModel.insert(item)
        except:
            return {"message":"An error occured inserting the item"},500

        return item,201




    def delete(self,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "Delete from items where name=?"
        cursor.execute(query,(name,))

        connection.commit()
        connection.close()

        return {'message':'items deleted'}

#USING reqparse to make sure ,we can parse the input data in put() method properly.
    #reqparse also helps in making sure that only variable json can be passed and not any other value
    def put(self,name):
        #first we check if item exist or not
        data=Item.parser.parse_args()
        item=ItemModel.findItemByName(name)
        updated_item={'name':name,'price':data['price']}

        if item is None:
            try:
                updated_item.insert()
                ItemModel.insert(updated_item)
            except:
                return {"message":"an error occured while inserting the data"},500
        else:
            try:
                ItemModel.update(updated_item) #item is actually a dictionary that has an updated method...
            except:
                return {"message":"An error occured while updating the item"},500
        return updated_item




class ItemList(Resource):
    def get(self):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        fetchAll_query="select * from items"
        result=cursor.execute(fetchAll_query)

        items=[]
        for row in result:
            items.append({'name':row[0],'price':row[1]})

        connection.close()

        return {'ITEM_LIST':items}