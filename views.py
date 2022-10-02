from hashlib import new
from socket import AI_NUMERICHOST
from flask import Blueprint,render_template
from recommend import Anime

views = Blueprint(__name__ ,"views")
test = Anime()

@views.route("/")
def home():
    return render_template("index.html",name = test.name, type = test.type, status = test.status,image = test.image)

@views.route("/refresh/", methods=['POST'])
def move_forward():
    test = Anime()
    return render_template("index.html",name = test.name, type = test.type, status = test.status,image = test.image)
