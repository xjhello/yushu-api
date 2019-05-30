from flask import Blueprint

from app.libs.redprint import Redprint

# book = Blueprint('book', __name__)
api = Redprint('book')

@api.route('/get')  #视图函数像红图注册
def get_book():
    #RESTFUL地址不包含动词（get。。）
    return 'get book'

@api.route('/create')
def create_book():
    return 'get book'