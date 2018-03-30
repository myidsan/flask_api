import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be left blank"
    )
    parser.add_argument('store_id',
            type=int,
            required=True,
            help="every item needs a store id"
    )
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {'message': 'item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
           return {'message': "item with name '{}' already exists".format(name)}, 400

        # since price is the only argument other args will be deleted by the next line
        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save_to_db()
        except:
            return {'message': 'an error occurred inserting the item'}, 500

        return item.json(), 201 # 201 is for created

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json() # still need to return in json format as an api


class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * from items"
        # result = cursor.execute(query)
        #
        # items = []
        # for row in result:
        #     items.append({'name': row[0], 'price': row[1]})
        #
        # connection.close()

        # return {'items': [item.json() for item in ItemModel.query.all()]} # python list comprehension
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))} # familiar in other language such as javascript
