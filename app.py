from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello")

application = Application([
    (r'/', MainHandler),
])

if __name__ == '__main__':
    application.listen(8888)
    IOLoop.instance().start()