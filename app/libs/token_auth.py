from collections import namedtuple
from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer \
    as Serializer, BadSignature, SignatureExpired
from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope

#自定义装饰器
auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])

@auth.verify_password
def verify_password(token, password): #获取token
    pass
    # token
    # HTTP 传输账号密码，放在header（键值对）
    # header key:value
    # account  qiyue
    # 123456
    # key=Authorization
    # value =basic base64(qiyue:123456)
    user_info = verify_auth_token(token) #token就是account
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token): #验证token
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)  #解密token
    except BadSignature:       #捕捉特点异常（是否合法）
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    except SignatureExpired:   #捕捉特点异常（是否过期）
        raise AuthFailed(msg='token is expired',
                         error_code=1003)
    uid = data['uid']    #返回token的信息
    ac_type = data['type']
    scope = data['scope']
    # request 视图函数
    allow = is_in_scope(scope, request.endpoint)  #判断是否可以访问视图函数（request.endpoint表示当前要访问的视图函数）
    if not allow:
        raise Forbidden()
    return User(uid, ac_type, scope)
