from .app import Flask


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    # app.register_blueprint(user)
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')  # 注册蓝图，url_prefix蓝图URL前缀


def register_plugin(app):  # 注册SQLAlchemy插件
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    register_plugin(app)
    return app
