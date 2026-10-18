import random

def generate_password():
    password = ""
    if len(password) < 8:
        lower_case = random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
        upper_case = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        number = random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        special_case = random.choice(["!", "@", "#", "$", "%", "^", "&", "*"])
        password = password+(upper_case)
        password = password+(number)
        password = password+(special_case)
        password = password+(lower_case)
        while len(password) < 8:
            random_charecter = random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*"])
            password = password+(random_charecter)
    return password
    
def create_function(database, save_database, admin_password):
    create_username = input("Create A Username: ")
    if create_username in database:
        print ("already a username")
    password = ""
    if len(password) < 8:
        lower_case = random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
        upper_case = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        number = random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        special_case = random.choice(["!", "@", "#", "$", "%", "^", "&", "*"])
        password = password+(upper_case)
        password = password+(number)
        password = password+(special_case)
        password = password+(lower_case)
        
        while len(password) < 8:
            random_charecter = random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*"])
            password = password+(random_charecter)
    ask_admin = input("are you and admin? ")
    database[create_username] = {"password": password, "admin": ask_admin, "admin_password": admin_password}
    save_database(database)
    if ask_admin == "no":
        database[create_username] = {"password": password, "admin": ask_admin} 
        print(database)
        save_database(database)
    else:
        database[create_username] = {"password": password, "admin": ask_admin, "admin_password": admin_password}
        print(database)
        save_database(database)


def admin_login_function(database, save_database, admin_password, ask_username, login_options):
    save_database(database)
    ask_admin_password = input("Enter admin password: ")
    if ask_admin_password == admin_password:
        print("Admin Login Sucessful!")
        AdminLogin = True
        return AdminLogin
    elif ask_admin_password != admin_password and login_options == "admin":
        print("Password Wrong! Admin Login Unsucessful!")
        AdminLogin = False
        return AdminLogin
    elif database[ask_username]["admin"] == "no" and login_options == "admin":
        print("No Admin Access!")
        save_database(database)
def admin_setting_options_delete_function(database, save_database, delete_account):
    if delete_account in database:
        database.pop(delete_account)
        print("Account Deleted!")
        save_database(database)
    else:
        print("Account doesn't exist!")