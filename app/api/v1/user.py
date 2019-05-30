from flask import jsonify, g

from app.libs.error_code import DeleteSuccess
from app.libs.token_auth import auth
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.user import User

api = Redprint('user')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required   #被保护的接口
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.id
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

# 管理员
@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    pass

@api.route('/create')
def create_user():
    return 'create user'

@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()