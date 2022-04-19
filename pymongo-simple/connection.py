from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
# Alternative Connection Method - MongoURL Format
# client = MongoClient('mongodb://10.10.10.59:27017')
print(client.server_info())
print(client.list_database_names())
