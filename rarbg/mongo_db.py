from pymongo import MongoClient

cluster = ""

client = MongoClient(cluster)

db = client.Torrent_Crawler

collection = db.rarbg
