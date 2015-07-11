import json

from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, API
from tweepy import Stream, api


# loading consumer key and access token
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")

access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")


class WebHandler(tornado.web.RequestHandler):
    """
    Renders a simple web page
    """
    def get(self):
        self.render("index.html")


class WebSocketHandler(tornado.web.WebSocketHandler):
    """
    Manages websocket connections
    """
    def open(self):
        pass

    def on_close(self):
        pass


handlers = [
    (r"/", WebHandler),
    (r"/ws", WebSocketHandler),
]

application = tornado.web.Application(handlers)


class StdOutListener(StreamListener):
    """
    Handles tweets from the received Twitter stream.
    """
    def on_data(self, data):
        data = json.loads(data)
        data_hashtags = data['entities']['hashtags']
        for i in data_hashtags:
            hashtag = '#{}'.format(i['text'])
            if hashtag in hashtags:
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
    hashtags = [i['name'] for i in api.trends_place(id=44418)[0]['trends']]
    stream.filter(track=hashtags)
