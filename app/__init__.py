from flask import Flask
from config import Config
from flask_cors import CORS

better = Flask(__name__,template_folder="../templates",static_folder="../static",static_url_path="")

CORS(better,supports_credentials=True)

#引入配置文件
better.config.from_object(Config)
