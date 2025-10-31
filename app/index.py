from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    page = (request.args.get("page"))
    pages = dao.Product_count()/app.config["PAGE_SIZE"]
    return render_template("index.html",  products=dao.load_product(q,cate_id,page),pages=int(pages))


@app.route('/login')
def login():
    return render_template(("login.html"))



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
