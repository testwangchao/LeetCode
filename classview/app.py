from flask import Flask, views, jsonify

app = Flask(__name__)


# 类视图，将数据格式化
class JsonView(views.View):
    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data())


class ListView(JsonView):
    def get_data(self):
        return {"code": 200, "msg": "success"}


#  子视图中存在共同使用的数据
class BaseData(views.View):
    def __init__(self):
        self.base_data = {"category": "basedata"}


class UpdateBaseData(BaseData):
    def __init__(self):
        super().__init__()
        self.base_data.update({"name": "update"})

    def dispatch_request(self):
        return self.base_data.get("name")


class SecondUpdate(BaseData):
    def __init__(self):
        super().__init__()
        self.base_data.update({"name": "second"})

    def dispatch_request(self):
        return "second update data"


app.add_url_rule('/list/', endpoint='list', view_func=ListView.as_view(name='test'))
app.add_url_rule('/updatedata/', endpoint='update', view_func=UpdateBaseData.as_view(name="update"))
app.add_url_rule('/second/', endpoint='second', view_func=SecondUpdate.as_view(name="second"))


if __name__ == '__main__':
    app.run(debug=True)
