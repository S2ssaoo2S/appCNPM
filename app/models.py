from sqlalchemy.orm import relationship
import json
from app import db,app
from sqlalchemy import column, Integer, String, Float, Column, true, ForeignKey


class Category(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),unique=True,nullable=False)
    products = relationship("Product",backref="Category",lazy=True)
    #
    # tostring
    def __str__(self):
        return self.name



class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    price =  Column(Float,default=0.0)
    image =  Column(String(300),default="https://res.cloudinary.com/dy1unykph/image/upload/v1729842193/iPhone_15_Pro_Natural_1_ltf9vr.webp")
    cate_id = Column(Integer, ForeignKey(Category.id),nullable=False)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        #
        # c1=Category(name="laptop")
        # c2=Category(name="Mobile")
        # c3=Category(name="Taplet")
        with open("data/product.json", encoding="utf-8") as f:
            products = json.load(f)
            for p in products:
                db.session.add(Product(**p))

        db.session.commit()