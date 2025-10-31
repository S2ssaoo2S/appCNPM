import json

from app import app
from models import Category,Product

def load_catagories():
    # with open("data/catagory.json", encoding="utf-8") as f:
    #     return json.load(f)
    return Category.query.all()


def load_product(q=None, cate_id=None,page=None ):

    # with open("data/product.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #     if q:
    #         products = [p for p in products if p["name"].find(q) >= 0]
    #     if cate_id:
    #         products = [p for p in products if p["cate_id"].__eq__(int(cate_id))]
    #     return products
    query = Product.query
    page = int(page)
    if q:
        query=query.filter(Product.name.contains(q))
    if cate_id:
        query = query.filter(Product.cate_id.__eq__(cate_id))
    if page:
        size = app.config["PAGE_SIZE"]
        start = int((page-1)*size)

        query= query.slice(start,start+size)
    return query


def load_product_by_id(id):
    # with open("data/product.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #     for p in products:
    #         if p["id"].__eq__(id):
    #             return p
    return Product.query.get(id)


def Product_count():
    return Product.query.count()

if __name__ == "__main__":
    print(load_product_by_id(2))
