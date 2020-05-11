import mongoConnect as mongo
import configuration as cfg
from pprint import pprint

database = mongo.connect()

def insertTweets(username, created_at, tweet, retweet_count, place, location):
    try:
        collection = database[cfg.MONGO_COLLECTION_NAME]
        insertDict = {"username" : username, "created_at" : created_at, "tweet" : tweet, "retweet_count": retweet_count, "place": place, "location" : location}
        insertStatus = collection.insert_one(insertDict)
    except Exception as e:
        print("Error in inserting tweet into mongo :\n",e)