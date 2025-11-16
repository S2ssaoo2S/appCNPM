
from flask import render_template, request, redirect
from flask_login import login_user, logout_user, current_user
import dao

from app import app,login,admin


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    page = int(request.args.get("page",1))
    pages = dao.Product_count()/app.config["PAGE_SIZE"]
    return render_template("index.html",  products=dao.load_product(q,cate_id,page),pages=int(pages))



@app.route('/login',methods=['GET','POST'])
def login_my_user():
    err_msg = None
    if current_user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = dao.auth_user(username,password)
        if user:
            login_user(user)
            return redirect("/")
        else:
            err_msg = "Invalid username or password."
    return render_template("login.html",err_msg=err_msg)

@login.user_loader
def load_user(id):
    return dao.get_user_by_id(id)

@app.route('/admin',methods=['POST'])
def admin_login():
    err_msg = None
    if current_user.is_authenticated:
        return redirect("/admin")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = dao.auth_user(username,password)
        if user:
            login_user(user)
            return redirect("/admin")
        else:
            err_msg = "Invalid username or password."
    return render_template("login.html",err_msg=err_msg)

@app.route('/logout')
def logout():
    logout_user()

    return redirect("/")

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
