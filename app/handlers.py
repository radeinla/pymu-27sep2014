from tornado.web import RequestHandler

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello world")

class LoginHandler(RequestHandler):
    def get(self):
        message = self.get_argument("message", "Please login.")
        self.render("login.html", message=message)

    def post(self):
        user = self.get_argument("username", "")
        password = self.get_argument("password", "")
        if user == 'admin' and password == 'password':
            self.redirect("/")
        else:
            self.redirect("/login?message=fail")

class GreetHandler(RequestHandler):
    def get(self, name=None):
        if not name:
            name = "huhu"
        self.write("Belat ka %s" % name)
