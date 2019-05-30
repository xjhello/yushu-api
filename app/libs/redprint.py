#自定义红图模块
class Redprint:
    def __init__(self, name): #构造函数
        self.name = name
        self.mound = []

    def route(self, rule, **options): #**options是URL规则，把视图函数注册到蓝图中，红图的route代替蓝图的route
        def decorator(f):
            self.mound.append((f, rule, options)) #把f, rule, options添加到mound
            return f
        return decorator

    def register(self, bp, url_prefix=None): #红图注册到蓝图
        if url_prefix is None:  #url_prefix优化用名称填充URL
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            endpoint = self.name + '+' + \
                       options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options) #模仿蓝图注册到app，注册到蓝图