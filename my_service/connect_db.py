import pymongo

def connectMongoDB():
    conn = pymongo.MongoClient("mongodb+srv://chutipas:TaTent591220306@cluster0-94rnq.mongodb.net/test?retryWrites=true&w=majority")
    db = conn.get_database("python_Project_MongoDB")
    return (db)
