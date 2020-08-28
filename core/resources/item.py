import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from core.models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()  # to create a special object to parse json
    parser.add_argument('price',  # selecting the argument to parse^  with  type and other parameters
                        type=float,
                        required=True,
                        help="This field cannot be left blanc!"
                        )

    parser.add_argument('store_id',  # was added after adding the stores!
                        type=int,
                        required=True,
                        help="Every item needs a store id!"
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': "Item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f"An item with {name} is already exists!"}, 400

        data = Item.parser.parse_args()
        #item = ItemModel(name, data['price'], data['store_id'])
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {'message': f"An error occured while inserting the item {item} in the DB!"}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': f"Item deleted: {name}."}

    def put(self, name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            #item = ItemModel(name, data['price'], data['store_id'])
            item = ItemModel(name, **data)

            # return {'message': f"An error occured while inserting the item {updated_item} in the DB!"}, 500
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [x.json() for x in ItemModel.query.all()]}