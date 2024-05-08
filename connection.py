import pymongo

def get_mongo_client():
    conn_str = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn_str)
    return client
