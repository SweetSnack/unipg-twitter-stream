import json
import config

from tweepy import OAuthHandler, API, Stream
from tweepy.streaming import StreamListener

from server import MessageHandler


class StdOutListener(StreamListener):
    """
    Handles tweets from the received Twitter stream.
    """
    def on_data(self, data):
        data = json.loads(data)
        if 'entities' in data and 'hashtags' in data.get('entities'):
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
    auth = OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, l)
    api = API(auth_handler=auth)
    config.HASHTAGS = [x['name'] for x in api.trends_place(id=44418)[0]['trends']]

    print("Stream listener is up and running")
    stream.filter(track=config.HASHTAGS)
