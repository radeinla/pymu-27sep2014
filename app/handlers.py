from tornado.web import authenticated, RequestHandler

class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    @authenticated
    def get(self):
        self.write("Hello world")

class LoginHandler(BaseHandler):
    def get(self):
        message = self.get_argument("message", "Please login.")
        self.render("login.html", message=message)

    def post(self):
        user = self.get_argument("username", "")
        password = self.get_argument("password", "")
        if user == 'admin' and password == 'password':
            self.set_secure_cookie("user", user)
            self.redirect("/")
        else:
            self.redirect("/login?message=fail")

class GreetHandler(BaseHandler):
    @authenticated
    def get(self, name=None):
        if not name:
            name = "huhu"
        self.write("Belat ka %s" % name)
