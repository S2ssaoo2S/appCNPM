import hashlib
from enum import  Enum as  UserEnum
from sqlalchemy.orm import relationship
import json
from app import db,app
from sqlalchemy import Integer, String, Float, Column, ForeignKey, Boolean, DateTime, Enum,TEXT
import datetime
from flask_login import  UserMixin

class UserRole(UserEnum):
       Admin = 2
       User = 1

class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    # tostring
    def __str__(self):
        return self.name

class User(Base,UserMixin):
     email = Column(String(50),default="##")
     username = Column(String(150),nullable=False,unique=True)
     password = Column(String(150),nullable=False)
     active = Column(Boolean,default=True)
     avatar = Column(String(150),default="https://cdn.vectorstock.com/i/1000v/44/73/boy-avatar-in-round-web-button-isolated-on-white-vector-20694473.jpg")
     joined_date = Column(DateTime, default=datetime.datetime.now())
     UserRole = Column(Enum(UserRole),default=UserRole.User)

class Category(Base):

    products = relationship("Product",backref="category",lazy=True)
    #




class Product(Base):
    price =  Column(Float,default=0.0)
    image =  Column(String(300),default="https://res.cloudinary.com/dy1unykph/image/upload/v1729842193/iPhone_15_Pro_Natural_1_ltf9vr.webp")
    cate_id = Column(Integer, ForeignKey(Category.id),nullable=False)
    description = Column(TEXT)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        password = "123"
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        c1=Category(name="laptop")
        c2=Category(name="Mobile")
        c3=Category(name="Taplet")
        user = User(username="user",name="nhan",password=password)
        db.session.add_all([c1,c2,c3])
        with open("data/product.json", encoding="utf-8") as f:
            products = json.load(f)
            for p in products:
                db.session.add(Product(**p))
        db.session.add(user)
        db.session.commit()