from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello")

handlers = [
    (r'/', MainHandler),
]
settings = {}

application = Application(handlers, **settings)

if __name__ == '__main__':
    application.listen(8888)
    IOLoop.instance().start()