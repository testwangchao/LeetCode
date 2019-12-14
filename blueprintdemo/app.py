from flask import Flask
import sys
sys.path.append("../")
from blueprintdemo.blueprints.user import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)


if __name__ == '__main__':
    app.run(debug=True)

