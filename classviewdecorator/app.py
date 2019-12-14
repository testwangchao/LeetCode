from flask import Flask, request, views
from functools import wraps

app = Flask(__name__)


def login_required(f_name):
    @wraps(f_name)
    def decorator(*args, **kwargs):
        # /login?username=wangchao
        username = request.args.get("username")
        if username == "wangchao":
            return f_name(*args, **kwargs)
        else:
            return "请登录"

    return decorator


@app.route('/settings/')
@login_required
def settings():
    return "这是设置界面"


class ProfileView(views.View):
    decorators = [login_required]

    def dispatch_request(self):
        return "这是个人中心界面"


app.add_url_rule('/profile/', view_func=ProfileView.as_view(name="profile"))

if __name__ == '__main__':
    app.run(debug=True)
