from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_session import Session

# Config文件暂存区
from config import config_dict


def create_app(config_name):

    app = Flask(__name__)
    config_class = config_dict[config_name]
    app.config.from_object(config_class)
    db = SQLAlchemy(app)
    redis_store = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT, db=config_class.REDIS_NUM)
    csrf = CSRFProtect(app)
    Session(app)
    return app





# TODO 等待開啓csrf_token验证