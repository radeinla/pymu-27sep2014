from tornado.web import RequestHandler

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello world")

class LoginHandler(RequestHandler):
    def get(self):
        self.write("""
<form method="POST" action="/login">
    User: <input name="username"><br>
    Pass: <input name="password" type="password"><br>
    <input type="submit">
</form>""")

    def post(self):
        user = self.get_argument("username", "")
        password = self.get_argument("password", "")
        if user == 'admin' and password == 'password':
            self.write("succ")
        else:
            self.write("fail")