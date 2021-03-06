"""
Этот учебный проект построен на стеке python/flask/flask-RESTful/SQLAlchemy.

Система представляет собой REST API сервис, который готов к интеграции с фронтэндом.
Фронтэнд может быть написан на шаблонах Jinja2 или на полноценном JS рфеймворке (например, vue.js).

Автор: С.Кишкурно
08 2020

Ссылка на курс:
https://www.udemy.com/course/rest-api-flask-and-python/


"""
import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from .security import authenticate, identity
from .resources.user import UserRegister
from .resources.item import Item, ItemList
from .resources.store import Store, StoreList


app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get ("DATABASE_URL", "sqlite:///data.db") # Второй параметр - default
app.config['SQLALCHEMY_TRAK_MODIFICATIONS'] = False
app.secret_key = 'Sergey'
api = Api(app)


jwt = JWT(app, authenticate, identity) # implements a special endpoint /auth


# ------------------------------------------------------------
# Resources
# ------------------------------------------------------------

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from .db import db
    db.init_app(app)
    app.run(port=5000, debug = True)

