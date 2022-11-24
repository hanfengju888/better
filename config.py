import os

class Config(object):
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT,'log','better.log')

    GUEST = 1

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

    #项目列表图片
    PROJECT_IMG_LIST = [
                        "https://t7.baidu.com/it/u=2621658848,3952322712&fm=193&f=GIF","https://image.baidu.com/search/detail?tn=baiduimagedetail&word=%E8%88%AA%E6%8B%8D%E5%9C%B0%E7%90%83%E7%B3%BB%E5%88%97&album_tab=%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90&album_id=312&ie=utf-8&fr=albumsdetail&cs=1856946436,1599379154&pi=120716&pn=12&ic=0&objurl=https%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1856946436%2C1599379154%26fm%3D193%26f%3DGIF",
                        "https://t7.baidu.com/it/u=931123624,502354944&fm=193&f=GIF","https://t7.baidu.com/it/u=4113083086,1494496387&fm=193&f=GIF",
                        "https://t7.baidu.com/it/u=407688855,3169248799&fm=193&f=GIF","https://t7.baidu.com/it/u=1723458001,3671360301&fm=193&f=GIF",
                        "https://t7.baidu.com/it/u=1577112734,4159784366&fm=193&f=GIF","https://t7.baidu.com/it/u=2359570649,2574326109&fm=193&f=GIF",
                        "https://t7.baidu.com/it/u=3357675082,868315873&fm=193&f=GIF","https://t7.baidu.com/it/u=2363269992,3614579621&fm=193&f=GIF",
                        "https://t7.baidu.com/it/u=3326728979,3352004316&fm=193&f=GIF","https://t7.baidu.com/it/u=2063845375,2992423749&fm=193&f=GIF",
                        "https://t7.baidu.com/it/u=2646899128,380997184&fm=193&f=GIF","https://t7.baidu.com/it/u=2749898014,3398644511&fm=193&f=GIF",
                        "https://t7.baidu.com/it/u=3813927488,1739778909&fm=193&f=GIF","https://t7.baidu.com/it/u=3985596329,30052956&fm=193&f=GIF","https://t7.baidu.com/it/u=1502566028,3589000199&fm=193&f=GIF",
                        "https://t7.baidu.com/it/u=2177360828,736658999&fm=193&f=GIF","https://t7.baidu.com/it/u=2179558408,1225199077&fm=193&f=GIF",
                        "https://t7.baidu.com/it/u=290885915,3406281522&fm=193&f=GIF","https://t7.baidu.com/it/u=836228418,3299829885&fm=193&f=GIF","https://t7.baidu.com/it/u=1811223786,2017754440&fm=193&f=GIF",
                        "https://t7.baidu.com/it/u=2783075563,3362558456&fm=193&f=GIF","https://t7.baidu.com/it/u=3355440349,3059059541&fm=193&f=GIF"]




