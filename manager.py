from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_session import Session
from flask_script import Manager

# Config文件暂存区
from config import config_dict

# config_dict

app = Flask(__name__)
config_class = config_dict["development"]
app.config.from_object(config_class)
db = SQLAlchemy(app)
redis_store = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT, db=config_class.REDIS_NUM)
csrf = CSRFProtect(app)
Session(app)
manager = Manager(app)


# TODO 等待開啓csrf_token验证

@app.route('/')
def index():
    session["name"] = "curry"
    return 'hello world'


if __name__ == '__main__':
    manager.run()
