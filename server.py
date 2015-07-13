import threading

import tornado.ioloop
import tornado.web

from twitter import TwitterListener

from server import WebHandler, MessageHandler


# Tornado handlers list
handlers = [
    (r"/", WebHandler),
    (r"/ws", MessageHandler),
]

application = tornado.web.Application(handlers)

if __name__ == '__main__':
    # listening Twitter stream in a new thread
    threading.Thread(target=TwitterListener).start()

    # starting tornado
    application.listen(8080)
    print("Server is running on port :8080")
    tornado.ioloop.IOLoop.current().start()
