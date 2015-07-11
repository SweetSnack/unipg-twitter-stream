import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web


class WebHandler(tornado.web.RequestHandler):
    """
    Renders a simple web page
    """
    def get(self):
        self.render("static/websocket.html")


class MessageHandler(tornado.websocket.WebSocketHandler):
    """
    Manages websocket connections
    """
    connections = []

    def open(self):
        self.connections.append(self)

    def on_close(self):
        self.connections.remove(self)
