"""
项目的基本配置
1.Config类
2.SQLAlchemy数据库扩展
3.redis存储对象
4.CSRF
5.flask-session
6.数据库迁移flask-script
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate


app = Flask(__name__)


class Config(object):
    """配置类"""
    DEBUG = True

    # 数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/news"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    #flask-session的配置
    SECRET_KEY = "HAHAH"
    # 指定 session 保存到 redis 中
    SESSION_TYPE = "redis"
    # 让 cookie 中的 session_id 被加密签名处理
    SESSION_USE_SIGNER = True
    # 使用 redis 的实例
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # session 的有效期，单位是秒
    PERMANENT_SESSION_LIFETIME = 86400


app.config.from_object(Config)
db = SQLAlchemy(app)
redis_srore = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 只做验证工作
CSRFProtect(app)
Session(app)
# 数据库迁移
manger = Manager(app)
Migrate(app, db)
manger.add_command('db', MigrateCommand)


@app.route('/')
def index():

    return '/index'


if __name__ == "__main__":
    app.run()