from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager, LoginManager
import  cloudinary ,os

app = Flask(__name__)
# database
app.secret_key = "your_secret_key"  # cần để session hoạt động
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 2

cloudinary.config(cloud_name ='djtoqsdpb',
                  api_key='882576756217423',
                 api_secret='tFpl8dCrW_IpCTpsBHRpYlcKV3Y')

db = SQLAlchemy(app)
login=LoginManager(app)

