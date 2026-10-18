# Password Generator: 
# Takes an input of username and password 

# Enter a username 

# Requirement for the password: 
# 8 characters long 
# at least 1 uppercase letter, 1 number, and 1 special case (!, @, #, $, %, ^, &, *) 
# Save the user-entered username and the generated password into a 'database' 


# database = (username, password) # tuple 



# dictionary[username] -> password



# Ask the user to log in 

# Enter your username: 
# Enter your password: 

# Check if the password matches the password in the database 
# If it does, say login successful
# If not, say password incorrect, and ask them to enter their password again 

# Save the users and posts in a separate file -> storing this info in a .json file 
# Pull in those file contents and load them onto the app at start 
# So we don't have to create new users and new posts every time 


from authentication import *
from posts import *
from friends import *
from users import *
import random
from json_helper import * 

database = load_database()
posts = load_posts()

Running = True
Login = False
AdminLogin = False
admin_password = "Admin123!"

while Running == True:
    create_or_login = input("Do you want to create an account or login? ")
    if create_or_login == "create":
        create_function(database, save_database, admin_password)
    if create_or_login == "login":
        ask_username = input("Enter your username: ")
        ask_password = input("Enter password: ")

        if ask_username in database: # rewrite this using the database's username/password values 
            if database[ask_username]["password"] == ask_password:
                print("Login Sucessful!")
                Login = True
                save_database(database)
            else:
                print("Login Unsucessful! Password Wrong!")
                Login = False
        else:
            print("Login Unsucessful! Username doesn't exsit!")
    if Login == False:
        continue
    while Login == True:
        # if they have any pending friend requests, print a notification message 
        # You have 3 pending friend requests! 
        if "friend_requests" in database[ask_username] and len(database[ask_username]["friend_requests"]) > 0:
            print("You have" , len(database[ask_username]["friend_requests"]), "pending friend requests!")
        login_options = input("Do you want to view your profile, settings, log out, sign into an admin, friends, or view dashboard? ")
        if login_options == "admin":
            if database[ask_username]["admin"] == "yes":
                AdminLogin = admin_login_function(database, save_database, admin_password, ask_username, login_options)
            if AdminLogin == True:
                admin_setting_options = input("Do you want to view database, delete accounts, or exit Admin? ")
                if admin_setting_options == "view":
                    print(database)
                if admin_setting_options == "delete":
                    admin_setting_options_delete_function(database, save_database)
                if admin_setting_options == "exit":
                    AdminLogin = False
                    Login = True
                    print("You have logged out from Admin!")
                    continue
        if login_options == "view" or login_options == "profile":
            view_profile_function(database, ask_username, save_posts, posts)
        if login_options == "bio":
            write_bio_function(database, ask_username, save_database)
        dashboard = False
        if login_options == "dashboard":
            dashboard = True
            while dashboard == True:
                display_posts_function(posts, save_posts)
                dashboard_options = input("What would you like to do? ")
                if dashboard_options == "like":
                    like_post_function(posts, ask_username, save_posts)
                if dashboard_options == "create post":
                    creating_post_function(posts, ask_username, save_posts)
                if dashboard_options == "comment":
                    comment_post_function(posts, ask_username, save_posts)
                if dashboard_options == "leave":
                    continue
                if dashboard_options == "delete":
                    delete_post_function(posts, ask_username, save_posts)
                if dashboard_options == "edit":
                    edit_post_function(posts, ask_username, save_posts)
        friends = False 
        if login_options == "friends":
            friends = True
            while friends == True:
                friend_options = input("Do you want to send a friend requests, view friend requests, view friends list, remove friend, or leave? ")

                if friend_options == "send":
                    send_friend_request_function(ask_username, database, save_database)
                if friend_options == "view requests":
                    view_friend_requests_function(database, ask_username, save_database)
                if friend_options == "view friends list":
                    view_friends_list_function(database, ask_username)
                if friend_options == "leave":
                    friends = False
                    continue
                if friend_options == "remove":
                    remove_friend_function(database, ask_username, save_database)

        if login_options == "settings":
            setting_options = input("Do you want to change you password, change the username, or delete your account? ")
            if setting_options == "password":
                change_password_function_settings(database, ask_username, save_database)
            if setting_options == "username":
                change_username_function_settings(database, ask_username, save_database)
            if setting_options == "delete":
                delete_account_function_settings(database, ask_username, save_database)
        if login_options == "log out":
            Login = False
            print("You have logged out!")
            continue
# Check if the username exists in the database 
# If it does, check if the password matches the database's username's password


