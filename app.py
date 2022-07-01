import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db
from security import authenticate
from security import identity
from resources.user import UserRegister
from resources.items import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
db_url = os.environ.get('DATABASE_URL_NEW')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("://", "ql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
    app.config['PROPAGATE_EXCEPTIONS'] = True
