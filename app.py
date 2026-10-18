from flask import Flask, render_template, request
app = Flask(__name__)

from authentication import *
from posts import *
from friends import *
from users import *
import random
from json_helper import * 
Username = False
Login = False
Password = False
database = load_database()
posts = load_posts()
admin_password = "Admin123!"

@app.route("/")
def home():
    return render_template("dashboard.html")
    
@app.route("/register", methods=["POST", "GET"])
def register():
    # get the username from the input from the html
    # generate the password  
    # add this username & password to database 
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password()
        admin_password = "Admin123!"
        ask_admin = request.form["admin"]

        if ask_admin == "yes":
            database[username] = {"password": password, "admin": ask_admin, "admin_password": admin_password}
            
            save_database(database)
        else:
            database[username] = {"password": password, "admin": ask_admin} 
            save_database(database)        
        return render_template("register.html", password=password, username=username, admin=ask_admin)
    
    return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])

def login():
    global Login
    global Username
    global Password
    # get the inputs coming in from the html input boxes 
    # check those username/password combo against our database 
    # add success/failure messaging 
        # if username is not found in database, print username not found 
        # if username is in database, but password is wrong, print wrong password
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # a = True
        # b = True 
        # if a == True and b == False:
        #     something  

        # Something w/ the Login and Password
        # Change something in both html and .py 
        # change something about the if statements but not the values 

        if username in database:
            Username = True
            if database[username]["password"] == password:
                Login = True
                Password = True
            else:
                Login = False
                Password = False
        else:
            Username = False
        return render_template("login.html", password=password, username=username, Login=Login, Username=Username,Password=Password)

    return render_template("login.html")

@app.route("/admin", methods=["POST"])
def admin():
    global admin_setting_options
    global database
    if request.method == "POST":
        delete_account = request.form["account_delete"]
    admin_setting_options_delete_function(database, save_database, delete_account)
    return render_template("admin.html", admin_setting_options= admin_setting_options, database = database, admin_setting_options_delete_function = admin_setting_options_delete_function)

@app.route("/friends", methods=["POST"])
def friends():
    return render_template("friends.html")

@app.route("/users", methods=["POST"])
def users():
    return render_template("users.html")

if __name__ == "__main__":
    app.run(debug=True)