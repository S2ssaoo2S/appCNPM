from functools import wraps

from flask import redirect
from sqlalchemy.sql.functions import current_user


def anonymous_required(f):
   @wraps(f)
   def decorated_func(*args,**kwargs):
       if current_user.is_authenticated:
           return redirect("/")
       return f(*args,**kwargs)
   return decorated_func()