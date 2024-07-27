from pymongo import MongoClient
import uuid

client = MongoClient('localhost', 27017, userName='cadastro', password='cadastro')
db = client['cadastro']
collection = db['estoque']


def save(data):
    data['_id'] = str(uuid.uuid4())
    collection.insert_one(data)
    return data


def update(data):
    collection.update_one({'_id': data['_id']}, {'$set': data})
    return data


def delete(id):
    collection.delete_one({'_id': id})
    return id


def find_by_name(name):
    data = collection.find_one({'nome': name})
    return data
