from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp
from wtforms import ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form): #客户端form数据验证
    account = StringField(validators=[DataRequired(message='不允许为空'), length(  #用户名
        min=5, max=32
    )])
    secret = StringField() #密码
    type = IntegerField(validators=[DataRequired()]) #类型

    def validate_type(self, value): #检测type
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm): #检测email
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    def validate_account(self, value): #检测账号是否注册过
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()


# class BookSearchForm(Form):
#     q = StringField(validators=[DataRequired()])
#
#
# class TokenForm(Form):
#     token = StringField(validators=[DataRequired()])
