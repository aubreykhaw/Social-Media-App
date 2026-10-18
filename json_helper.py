import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_database(): 
    # check if the file exists
    # if it does, we open the file and return whatever the file contains 
    # else, we return an empty dictionary 
    file_path = os.path.join(BASE_DIR, "users_for_password_generator.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return {}
    

def save_database(database): 
    file_path = os.path.join(BASE_DIR, "users_for_password_generator.json")

    # open our file as a write-file instead of a read-file
    # dump info into the json file 
    with open(file_path, "w") as file:
        json.dump(database, file, indent=4)

def load_posts(): 
    file_path = os.path.join(BASE_DIR, "posts_for_password_generator.json")

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
            
    else:
        return []    

def save_posts(posts):
    file_path = os.path.join(BASE_DIR, "posts_for_password_generator.json")

    with open(file_path, "w") as file:
        json.dump(posts, file, indent = 4)