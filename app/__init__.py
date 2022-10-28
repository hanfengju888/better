from flask import Flask
from config import Config

better = Flask(__name__)

#引入配置文件
better.config.from_object(Config)
