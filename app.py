from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
import uuid
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
for post in posts:
    if "post_id" not in post:
        post["post_id"] = str(uuid.uuid4())

save_posts(posts)
admin_password = "Admin123!"

@app.route("/")
def index():
    if Login == True:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("register"))

@app.route("/dashboard", methods=["POST", "GET"])
def home():
    # add all of the features available from dashboard in main.py
    # display all the posts
    # creatin a post 
    # liking a post 
    # commenting a post 
    # edit/delete post
    global ask_username
    ask_username = "aubs"
    if request.method == "POST":
        action = request.form["action"]
        post_id = request.form["post_id"]
    
        if action == "like":
            # increase the like value for the post by 1
            # posts is a list of dictionaries 
            # each post contains a like int, comments list, and post string
            like_post_function(posts, save_posts, post_id)
        if action == "comment":
            comment = request.form["comment"]
            comment_post_function(posts, ask_username, save_posts, post_id, comment)
        if action == "delete":
            delete_post_function(posts, ask_username, save_posts, post_id)
        if action == "edit":
            return redirect(url_for("edit_post", post_id=post_id))
    return render_template("dashboard.html", posts=posts)
    
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
                return redirect(url_for("home"))
            else:
                Login = False
                Password = False
        else:
            Username = False
        return render_template("login.html", password=password, username=username, Login=Login, Username=Username,Password=Password)

    return render_template("login.html")

@app.route("/admin", methods=["POST", "GET"])
def admin():
    global admin_setting_options
    global database
    if request.method == "POST":
        delete_account = request.form["account_delete"]
    admin_setting_options_delete_function(database, save_database, delete_account)
    return render_template("admin.html", admin_setting_options= admin_setting_options, database = database, admin_setting_options_delete_function = admin_setting_options_delete_function)

@app.route("/create", methods=["POST", "GET"])
def create():
    # all things related to creating a post 
    # Creating a single post 
    
    # "username": whoever is currently signed in (aubs)
    # "post": content (coming from the html)
    # "likes": 0 
    # "comments": [] 

    ask_username = "aubs"
    if request.method == "POST":
        content = request.form["content"]
        posts.append({"username": ask_username, "post": content, "likes": 0, "comments": [], "post_id": str(uuid.uuid4())})
        save_posts(posts)
        return render_template("create.html", message="Post created successfully!") 
    
    return render_template("create.html")
@app.route("/edit/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    print(post_id)
    post = None

    for p in posts:
        if p["post_id"] == post_id:
            post = p
            break

    if post is None:
        return "Post not found"

    if request.method == "POST":
        post["post"] = request.form["content"]
        save_posts(posts)
        return redirect(url_for("home"))

    return render_template(
        "edit.html",
        content=post["post"],
        post_id=post_id
    )
    



@app.route("/friends", methods=["POST"])
def friends():
    return render_template("friends.html")

@app.route("/users", methods=["POST"])
def users():
    return render_template("users.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)