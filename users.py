def change_password_function_settings(database, ask_username, save_database):
    change_password = input("What is your new password? ")
    if len(change_password) < 8:
        print("Password must be at least 8 charecters long!")
    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_cases = ["!", "@", "#", "$", "%", "^", "&", "*"]
    u = False
    for letter in uppercase:
        if letter in change_password:
            u = True
            break
    if u == False:
        print("Need an uppercase!")
    l = False
    for letter in lower_case:
        if letter in change_password:
            l = True
            break
    if l == False:
        print("Need an lowercase!")
    n = False
    for number in numbers:
        if number in change_password:
            n = True
            break
    if n == False:
        print("Need an number!")
    s = False
    for letter in special_cases:
        if letter in change_password:
            s = True
            break
    if s == False:
        print("Need an special case!")
    # If all four of the conditions pass, then we want to change the password 
    if u == True and l == True and n == True and s == True:
        # TODO: Pick up from here
        #Change only password not admin
        database[ask_username]["password"] = change_password
        save_database(database)
        print("View profile to see changes")

def change_username_function_settings(database, ask_username, save_database):
    change_username = input("What is your new username? ")
    if change_username == ask_username:
        print("Username is the same as the old one!")
    if change_username in database:
        print("Username already exists!")
        save_database(database)

    #delete the old username and password from the database
    database[change_username] = database[ask_username]
    database.pop(ask_username)
    save_database(database)
    #if username exists in database, ask for a different one
    
    ask_username = change_username
    print("View profile to see changes")

def delete_account_function_settings(database, ask_username, save_database):
    delete = input("Are you sure you want to delete you account? ")
    if delete == "yes":
        database.pop(ask_username)
        print("Account Deleted!")
        Login = False
        save_database(database)
    else:
        print("Account not deleted!")

def view_profile_function(database, ask_username, save_posts, posts):
    print("Your username is:", ask_username)
    print("Your password is:", database[ask_username])
    if "friends" in database[ask_username]:
        print("You have", len(database[ask_username]["friends"]), "friends!")
    else:
        print("You have 0 friends!")
    user_posts = []
    for post in posts:
        if post["username"] == ask_username:
            user_posts.append(post)
            save_posts(posts)
            
    if len(user_posts) > 0:
        print("You have", len(user_posts), "posts!")  
        save_posts(posts)    
    else:
        print("You have 0 posts!")
    if "bio" in database[ask_username]:
        print("Your bio is:", database[ask_username]["bio"])

def write_bio_function(database, ask_username, save_database):
    bio = input("What is you bio? ")
    database[ask_username]["bio"] = bio
    save_database(database)
