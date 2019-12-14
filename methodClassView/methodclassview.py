from flask import Flask, views, render_template, request

app = Flask(__name__)


class LoginView(views.MethodView):

    def __render(self, error_msg=None):
        return render_template("login.html", error=error_msg)

    def get(self):
        return self.__render()

    def post(self):
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "wangchao" and password == "123456":
            return "登录成功"
        else:
            return self.__render(error_msg="用户名或密码错误")


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))


if __name__ == '__main__':
    app.run(debug=True)
