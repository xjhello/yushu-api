
class Scope:  # 定义基类
    allow_api = []
    allow_module = []   # 通过输入模块名字实现能访问模块下所有的视图函数
    forbidden = []    # 排除的视图函数

    def __add__(self, other):  # 运算符重载：实现AdminScop+UserScope
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))  # 使用集合去除重复的元素

        self.allow_module = self.allow_module + \
                            other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


# class SuperScope(Scope): #管理员
#     allow_module = ['v1.user']
#
#     def __init__(self):
#         pass
#         # self + UserScope()


class AdminScope(Scope):  # 管理员权限
    # allow_api = ['v1.user+super_get_user',
    #              'v1.user+super_delete_user']
    allow_module = ['v1.user']   # 整个user模块下的视图函数

    def __init__(self):
        # 排除：模块下列外的不能访问的视图函数
        pass
        # self + UserScope()


class UserScope(Scope):
    allow_module = ['v1.gift']
    forbidden = ['v1.user+super_get_user',   # 排除的视图函数
                 'v1.user+super_delete_user']

    def __init__(self):
        self + AdminScope()
    # allow_api = ['v1.user+get_user', 'v1.user+delete_user']


def is_in_scope(scope, endpoint):  # 判断能不能访问视图函数
    # globals 根据类名字动态创建对象
    # v1.view_func   v1.module_name+view_func
    # v1.red_name+view_func
    scope = globals()[scope]()   # 根据类名字实例化对象
    splits = endpoint.split('+')  # 模块名下所有视图函数
    red_name = splits[0]
    if endpoint in scope.forbidden:  # 排除函数
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
