from datetime import timedelta

from flask import Flask
from config import Config
from flask_cors import CORS
from flask import session

better = Flask(__name__,template_folder="../templates",static_folder="../static",static_url_path="")

CORS(better,supports_credentials=True)

#引入配置文件
better.config.from_object(Config)

#session时使用
better.config['SECRET_KEY'] = "FDJIOJ2klkdsjoOIJF(&&*^%^&&*"
better.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) # 配置7天有效 ,session有效期
