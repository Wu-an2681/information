from redis import StrictRedis


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
    SESSION_USE_SIGNER = True  # 是否加密
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 3600 * 72

    """
                if config['SESSION_TYPE'] == 'redis':
            session_interface = RedisSessionInterface(
                config['SESSION_REDIS'], config['SESSION_KEY_PREFIX'],
                config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])
                interface 实力对象
                 SIGNER 签名
    """


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = ""

# 接口
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}