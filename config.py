class Config:
    SECRET_KEY = 'g8f6d9j5h7k3l1m2n4p6q9r7s5t8u6v1w2x'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'mavec_store'


config={
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}