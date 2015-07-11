import json
import threading

import config

from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

from tweepy import OAuthHandler, API, Stream, api
from tweepy.streaming import StreamListener


# loading consumer key and access token
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

consumer_key = environ.get("consumer_key")
consumer_secret = environ.get("consumer_secret")

access_token = environ.get("access_token")
access_token_secret = environ.get("access_token_secret")


class WebHandler(tornado.web.RequestHandler):
    """
    Renders a simple web page
    """
    def get(self):
        self.render("index.html")


class MessageHandler(tornado.websocket.WebSocketHandler):
    """
    Manages websocket connections
    """
    connections = []

    def open(self):
        self.connections.append(self)

    def on_close(self):
        self.connections.remove(self)


handlers = [
    (r"/", WebHandler),
    (r"/ws", MessageHandler),
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
            if hashtag in config.HASHTAGS:
                # sends a websocket message with the appropriate hashtag
                for connection in MessageHandler.connections:
                    connection.write_message(hashtag)
                return True
        return True

    def on_error(self, status):
        print(status)


def TwitterListener():
    """
    Initializes the twitter listener
    """
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    api = API(auth_handler=auth)
    config.HASHTAGS = [ x['name'] for x in api.trends_place(id=44418)[0]['trends'] ]

    print("Stream listener is up and running")
    stream.filter(track=config.HASHTAGS)


if __name__ == '__main__':
    # listening Twitter stream in a new thread
    threading.Thread(target=TwitterListener).start()

    # starting tornado
    application.listen(8080)
    print("Server is running on port :8080")
    tornado.ioloop.IOLoop.current().start()
