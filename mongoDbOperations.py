import mongoConnect as mongo
import configuration as cfg
from pprint import pprint

database = mongo.connect()

class tweetObject:
    def __init__(self, username, created_at, tweet, retweet_count, place, location):
        self.username = username
        self.created_at = created_at
        self.tweet = tweet
        self.retweet_count = retweet_count
        self.place = place
        self.location = location
    
def insertTweets(username, created_at, tweet, retweet_count, place, location):
    try:
        collection = database[cfg.MONGO_COLLECTION_NAME]
        singleTweet = tweetObject(username, created_at, tweet, retweet_count, place, location)
        collection.insert_one(singleTweet.__dict__)
    except Exception as e:
        print("Error in inserting tweet into mongo :\n",e)
