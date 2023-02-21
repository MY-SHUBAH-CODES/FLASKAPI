from flask import request
from app import app
from model.usermodel import User
obj=User()

@app.route("/user")
def alluser():
    return obj.getalluser()

@app.route("/user/one", methods=['POST'])
def oneuser():
    return obj.getoneuser(request.form)

@app.route("/user/create",methods=['POST'])
def create():
    return obj.createuser(request.form)

@app.route("/user/delete",methods=['POST'])
def delete():
    print()
    return obj.deleteuser(request.form)

