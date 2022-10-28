import os

class Config(object):
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT,'log','better.log')

    #mysql连接信息
    MYSQL_HOST = "82.157.253.247"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PWD = "1qaz#EDC"
    DBNAME = "better"

    #sqlalchemy
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(MYSQL_USER,MYSQL_PWD,MYSQL_HOST,MYSQL_PORT,DBNAME)
    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s:%d/%s" %(MYSQL_USER,MYSQL_PWD,MYSQL_HOST,MYSQL_PORT,DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False



