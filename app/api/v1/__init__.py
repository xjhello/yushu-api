from flask import Blueprint
from app.api.v1 import book, token, user, client


def create_blueprint_v1():
    # from app.api.v1.book import api as book
    # from app.api.v1.user import api as user
    bp_v1 = Blueprint('v1', __name__) #实例化蓝图
    user.api.register(bp_v1) #红图向蓝图注册，url_prefix红图URL前缀
    book.api.register(bp_v1) #省去了url_prefix,使用了__name__代替 实现在红图代码中
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    return bp_v1