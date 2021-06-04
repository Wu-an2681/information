from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_session import Session


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information17"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_NUM = 7
    SECRET_KEY = "9JyG24ruWzCdwzF7LTt4M8t9R+f4kppwk60q1JdlCFiaBohkTqB9EFWZ+UCztvLPpIfDfG5zWfYID8fopwIU1Q=="
    SESSION_TYPE = "redis"
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_NUM)
    SESSION_USE_SIGNER = True # 是否加密
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 3600*72

    """
                if config['SESSION_TYPE'] == 'redis':
            session_interface = RedisSessionInterface(
                config['SESSION_REDIS'], config['SESSION_KEY_PREFIX'],
                config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])
                interface 实力对象
                 SIGNER 签名
    """
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_NUM)
csrf = CSRFProtect(app)
Session(app)

# TODO 等待開啓csrf_token验证

@app.route('/')
def index():
    session["name"] = "curry"
    return 'hello world'


if __name__ == '__main__':
    app.run()
