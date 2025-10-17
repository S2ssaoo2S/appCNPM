from itertools import product
from flask import Flask, render_template, request
import dao

app = Flask(__name__)


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    print(dao.load_product(q, cate_id))
    return render_template("index.html",  products=dao.load_product(q, cate_id))


@app.route("/products/<int:id>")
def product_details(id):
    return render_template("products.html",details=dao.load_product_by_id(id))
@app.context_processor
def context_processor():
    return {
        "cate": dao.load_catagories()
    }

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
