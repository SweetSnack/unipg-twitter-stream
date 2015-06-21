from sys import stdout
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, API
from tweepy import Stream, api

import json
import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")

access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")

class StdOutListener(StreamListener):
    """
    A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        data = json.loads(data)
        data_hashtags = data['entities']['hashtags']
        for i in data_hashtags:
            hashtag = '#{}'.format(i['text'])
            if hashtag in hashtags:
                print(hashtag)
                # DON'T FORGET TO FLUSH!!!!
                stdout.flush()
                return True
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    api = API(auth_handler=auth)
    hashtags = [i['name'] for i in api.trends_place(id=23424853)[0]['trends']]
    stream.filter(track=hashtags)
