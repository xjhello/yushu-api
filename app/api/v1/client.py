from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum


api = Redprint('client')

@api.route('/register', methods=['POST']) #用户注册
def create_client():
    form = ClientForm().validate_for_api()
    promise = {  # 字典的方式处理不同的客户端注册
        ClientTypeEnum.USER_EMAIL: __register_user_by_email  # 邮箱登录方式
    }
    promise[form.type.data]()  # 调用
    return Success()


def __register_user_by_email(): #注册方法
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data,  form.secret.data)
