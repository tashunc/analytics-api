# from mongoengine import connect
# from pymongo import ReadPreference
# #
# # Bar.objects().read_preference(ReadPreference.PRIMARY)
# # Bar.objects(read_preference=ReadPreference.PRIMARY)
# connect(
#     db='test',
#     username='user',
#     password='12345',
#     host='mongodb://admin:qwerty@localhost/production'
# )
# connect(alias='user-db-alias', db='user-db')
# connect(alias='book-db-alias', db='book-db')
# connect(alias='users-books-db-alias', db='users-books-db')
#
# class User(Document):
#     name = StringField()
#
#     meta = {'db_alias': 'user-db-alias'}
#
# class Book(Document):
#     name = StringField()
#
#     meta = {'db_alias': 'book-db-alias'}
#
# class AuthorBooks(Document):
#     author = ReferenceField(User)
#     book = ReferenceField(Book)
#
#     meta = {'db_alias': 'users-books-db-alias'}
# disconnect(alias='db1')


# from mongoengine.context_managers import switch_db
#
# class User(Document):
#     name = StringField()
#
#     meta = {'db_alias': 'user-db'}
#
# with switch_db(User, 'archive-user-db') as User:
#     User(name='Ross').save()  # Saves the 'archive-user-db'


# from mongoengine.context_managers import switch_collection
#
# class Group(Document):
#     name = StringField()
#
# Group(name='test').save()  # Saves in the default db
#
# with switch_collection(Group, 'group2000') as Group:
#     Group(name='hello Group 2000 collection!').save()  # Saves in group2000 collection


# from pymongo import Connection
from bson import ObjectId
# from itertools import imap


# class Model(dict):
#     """
#     A simple model that wraps mongodb document
#     """
#     __getattr__ = dict.get
#     __delattr__ = dict.__delitem__
#     __setattr__ = dict.__setitem__
#
#     def save(self):
#         if not self._id:
#             self.collection.insert(self)
#         else:
#             self.collection.update(
#                 { "_id": ObjectId(self._id) }, self)
#
#     def reload(self):
#         if self._id:
#             self.update(self.collection\
#                     .find_one({"_id": ObjectId(self._id)}))
#
#     def remove(self):
#         if self._id:
#             self.collection.remove({"_id": ObjectId(self._id)})
#             self.clear()
from pymongo import MongoClient

CACHE_DB = 'CacheDB'
COLLECTION_LUNA_TIME_SERIES = 'LunaTimeSeries'


# Create connection to MongoDB


# def getClient():
#     return MongoClient('localhost', 27017)
#
#
# def getDb(client, db_name):
#     return client[db_name]
#
#
# def getTimeSeriesCollection(db, collection_name):
#     return db[collection_name]
#
#
# def getLunaTimeSeriesCollection():
#     return getTimeSeriesCollection(
#         getDb(getClient(), CACHE_DB), COLLECTION_LUNA_TIME_SERIES)
def getLunaTimeSeriesCollection():
    return MongoConnection(db_name=CACHE_DB, collection_name=COLLECTION_LUNA_TIME_SERIES).getConnection()


def getClient():
    return MongoClient('localhost', 27017)


def isExists(collection, _id):
    # this next line is where I'm running into trouble
    if collection.count_documents({'_id': _id}) > 0:
        return True
    else:
        return False


def isAllIdExist(collection, _ids, ):
    collection.count_documents({'_id': {"$in": _ids}})


class Model(dict):

    def insertTimeSeriesData(self, collection):
        if self['_id'] is None:
            if self['time'] is not None:
                self['_id'] = self['time']
        collection.insert(self)

    def updateTimeSeriesData(self, collection):
        if self['_id'] is None:
            if self['time'] is not None:
                self['_id'] = self['time']
        collection.insert(self)


class MongoConnection:

    def __init__(self, db_name, collection_name):
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = getClient()
        self.collection = getClient()[self.db_name][self.collection_name]

    def closeConnection(self):
        self.client.close()

    def getConnection(self):
        return self.collection
