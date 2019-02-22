from flask import *
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)
items = []

class Item(Resource):
    def get(self,name):
        # for i in items:
        #     if i['name']==name:
        #         return i
        item = next(filter(lambda i:i["name"]==name,items),None)
        #if item != None:
        return {'item':item}, 200 if item else 404

    def post(self,name):
        if next(filter(lambda x:x["name"]==name,items),None):
            return {"message":"item with {0} as name already exists".format(name)}, 400
        data = request.get_json()
        item = {'name':name,'price':data["price"]}
        items.append(item)
        return item, 201

class Itemlist(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Itemlist,'/items')
app.run(port=5000,debug=True)

