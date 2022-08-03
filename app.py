from flask import Flask
from controller.coin_controller import coin
from controller.lunacrush_controller import luna
from flask_mongoengine import MongoEngine
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'CacheDb',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

app.register_blueprint(coin, url_prefix='/api/v1/gecko')
app.register_blueprint(luna, url_prefix='/api/v1/luna')
app.run(debug=True, port=5000)
