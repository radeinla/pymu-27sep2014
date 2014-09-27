from tornado.ioloop import IOLoop
from tornado.web import Application

from app.handlers import GreetHandler, LoginHandler, MainHandler

handlers = [
    (r'/', MainHandler),
    (r'/login', LoginHandler),
    (r'/greet', GreetHandler),
    (r'/greet/(.*)', GreetHandler),
]

settings = {
    "static_url_prefix": "/static/",

    #for dev only
    "debug": True,
    "static_path": "static",
    "template_path": "templates",
    "cookie_secret": "asdasdasdq12e",
    "login_url": "/login"
}

db = None # Dummy

application = Application(handlers, **settings)

if __name__ == '__main__':
    application.listen(8888)
    IOLoop.instance().start()