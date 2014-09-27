from tornado.web import RequestHandler

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello world")

class LoginHandler(RequestHandler):
    def get(self):
        self.render("login.html", message="Please login.", error="")

    def post(self):
        user = self.get_argument("username", "")
        password = self.get_argument("password", "")
        if user == 'admin' and password == 'password':
            self.render("login.html", message="succ", error="")
        else:
            self.render("login.html", message="", error="fail")

class GreetHandler(RequestHandler):
    def get(self, name=None):
        if not name:
            name = "huhu"
        self.write("Belat ka %s" % name)
