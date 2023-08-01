# coding:utf-8
from urllib.parse import quote
from pathlib import Path

BASE_PATH = Path().resolve()
CONFIG_PATH = BASE_PATH / 'RealProject/setting.py'
DEBUG = True
# print(BASE_PATH)
'''mysql配置参数'''
HOSTNAME = '192.168.223.128'
PORT = '3306'
DATABASE = 'flask'
USERNAME = 'root'
PASSWORD = 'abc@123'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, quote(PASSWORD), HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

'''mongodb配置'''
MONGODB_SETTINGS = {
    'db': 'flask',
    'host': '192.168.223.128',
    'port': 27017,
    'connect': True,
    'username': 'root',
    'password': '123456',
    'authentication_source': 'admin'
}

'''redis配置'''
CACHE_TYPE = 'RedisCache'
CACHE_REDIS_HOST = '192.168.223.128'
CACHE_REDIS_PORT: 6379
CACHE_REDIS_DB: ''
CACHE_REDIS_PASSWORD = ''
REDIS_URL = 'redis://:@192.168.223.128:6379/0'

'''邮箱配置'''
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USERNAME = 'alphonse9317@163.com'
MAIL_PASSWORD = 'ODXEQUSVPUIFAVDC'
MAIL_USE_TLS = False
MAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'alphonse9317@163.com'

DATABASE_DJANGO = 'test_django'
SQLALCHEMY_BINDS = {
    'mysql': 'mysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, quote(PASSWORD), HOSTNAME, PORT, DATABASE),
    'other': 'mysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, quote(PASSWORD), HOSTNAME, PORT, DATABASE_DJANGO)
}
