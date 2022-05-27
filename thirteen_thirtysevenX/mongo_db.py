from pymongo import MongoClient

cluster = ""


client = MongoClient(cluster)

db = client.Torrent_Crawler

collection = db.thirteen_thirtysevenX

# print(client.list_database_names())