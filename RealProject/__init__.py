# coding:utf-8
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .setting import BASE_PATH
import pymysql
from flask_mongoengine import MongoEngine
from flask_redis import FlaskRedis
from flask_mail import Mail,Message
import secrets



pymysql.install_as_MySQLdb()
db = SQLAlchemy()
mongo = MongoEngine()
migrate = Migrate()
# rds = Cache()
fds = FlaskRedis()
mail=Mail()

def create_app(test_config=None):
    # create and configure the app
    ## instance_relative_config设置为True则代表开启从文件加载配置，默认为False
    app = Flask(__name__, instance_relative_config=True)
    cx = app.app_context()
    cx.push()
    a = current_app
    # app.secret_key = str(datetime.datetime.now())
    app.secret_key = secrets.token_hex(16)
    # app.permanent_session_lifetime = timedelta(days=7)
    # app=Flask(__name__)
    # 这里做了判断是否运行时传入了测试配置
    if test_config is None:
        # 如果没有传入，则从py文件加载配置，silent=True代表文件，文件加载成功则返回True
        CONFIG_PATH = BASE_PATH / 'RealProject/setting.py'
        app.config.from_pyfile(CONFIG_PATH, silent=True)
    else:
        # 和最开始的配置意思一致
        app.config.from_mapping(test_config)

    # for item in app.config:
    #     print(str(item)+':'+str(app.config[item]))
    logger.add("./logs/mongo_link.log")
    mongo.init_app(app)
    db.init_app(app)
    # rds.init_app(app)
    fds.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    from app.employee import views
    app.register_blueprint(views.bp)
    from app.employee import models

    return app
