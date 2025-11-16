from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView

from flask_admin.theme import Bootstrap4Theme
from app import app,db
from models import Category
class CategoryModelView(ModelView):
    column_list = ['name','products']
    column_searchable_list = ['name']
class MyIndexView(AdminIndexView):
    @expose('/')
    def index(self) ->str:

        return self.render('admin/index.html')
admin = Admin(app=app, name="E-COMMERCE", theme=Bootstrap4Theme(),index_view=MyIndexView())





admin.add_view(CategoryModelView(Category,db.session))