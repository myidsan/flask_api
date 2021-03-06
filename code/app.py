from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items = []

# class Student(Resource):
#     # this resource is accessibile via get 
#     def get(self, name):
#         return {'student': name}

# api.add_resource(Student, '/student/<string:name>')

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be left blank"
    )
    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        item = next(filter(lambda x: x['name'] == name, items), None) # return first item found in the filter object
        return {'item': item}, 200 if item else 404
     
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
           return {'message': "item with name '{}' already exists".format(name)}, 400

        # since price is the only argument other args will be deleted by the next line      
        data = Item.parser.parse_args() 

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 #201 is for created
    
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}
    

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)