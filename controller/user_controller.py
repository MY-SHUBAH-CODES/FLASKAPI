from app import app
from model.user import User
obj=User()

@app.route("/user/signup/<string:name>")
def signup(name):
    return obj.createuser(username=name)