from flask import Blueprint

# url_prefix添加前缀,/user/profile  /user/settings,定义此参数的时候需要注意斜杆
user_bp = Blueprint(name="user", import_name=__name__, url_prefix='/user',)


# 个人中心
@user_bp.route('/profile/')
def profile():
    return "个人中心界面"


# 用户设置
@user_bp.route('/settings')
def setting():
    return "设置界面"
