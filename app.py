from tornado.ioloop import IOLoop
from tornado.web import Application

from app.handlers import LoginHandler, MainHandler

handlers = [
    (r'/', MainHandler),
    (r'/login', LoginHandler),
]
settings = {
    "static_url_prefix": "/static/",

    #for dev only
    "debug": True,
    "static_path": "static",
    "template_path": "templates"
}

application = Application(handlers, **settings)

if __name__ == '__main__':
    application.listen(8888)
    IOLoop.instance().start()