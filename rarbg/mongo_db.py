from pymongo import MongoClient

cluster = "mongodb+srv://saif_ahmad:LtQDYX4BnfopWsis@cluster0.91n6xte.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(cluster)

db = client.Torrent_Crawler

collection = db.rarbg
