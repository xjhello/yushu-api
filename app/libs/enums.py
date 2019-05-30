#枚举代表类型
from enum import Enum


class ClientTypeEnum(Enum): #客户端类型
    USER_EMAIL = 100 #以email方式登录
    USER_MOBILE = 101 #以mobile方式登录

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
