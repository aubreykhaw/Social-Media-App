def send_friend_request_function(ask_username, database, save_database):
        send_friend_request = input("Who do you want to send a friend request to? ")
        if send_friend_request not in database:
            print("User does not exist!")
            
        if send_friend_request in database:
            # a user will need a way to keep track of all the friend requests they RECEIVE
            # a user can have multiple friend requests at a time 

            # error checking 
            # can't send a friend request to someone that doesn't exist 
            # can't send a friend request to yourself 
            # can't send a friend request to someone you've already sent a request to/is already your friend 
            if send_friend_request == ask_username:
                print("No sending friend requests to yourself!")
                
            if "friends" in database[ask_username] and send_friend_request in database[ask_username]["friends"]:
                print("Already friends with this user!")
                
            if "friend_requests" in database[send_friend_request] and ask_username in database[send_friend_request]["friend_requests"]:
                print("Already sent a friend request to this user!")
            if "friend_requests" in database[send_friend_request]:
                database[send_friend_request]["friend_requests"].append(ask_username)
                save_database(database)
            else:
                database[send_friend_request]["friend_requests"] = [ask_username]
                save_database(database)
                print("Friend request sent!")

def view_friend_requests_function(database, ask_username, save_database):
    if "friend_requests" in database[ask_username]:
        print("Friend Requests: ", database[ask_username]["friend_requests"])
        accept_request = input("Do you want to accept any of the requests? ")
        save_database(database)
        if accept_request == "yes":
            accept_request_username = input("Who do you want to become friends with? ")
            if accept_request_username in database[ask_username]["friend_requests"]:

                if "friends" in database[ask_username]:
                    database[ask_username]["friends"].append(accept_request_username)
                    save_database(database)
                else:
                    database[ask_username]["friends"] = [accept_request_username]
                    save_database(database)
                if "friends" in database[accept_request_username]:
                    database[accept_request_username]["friends"].append(ask_username)
                    save_database(database)
                    print("You are now friends with ", accept_request_username)
                    database[ask_username]["friend_requests"].remove(accept_request_username)
                    save_database(database)
                else:
                    database[accept_request_username]["friends"] = [ask_username]
                    save_database(database)
                    print("You are now friends with ", accept_request_username)
                    database[ask_username]["friend_requests"].remove(accept_request_username)
                    save_database(database)

    else:
        print("No friend requests!")

def view_friends_list_function(database, ask_username):
    if "friends" in database[ask_username]:
        print("Friends List: ", database[ask_username]["friends"])
    
    else:
        print("No friends yet!")

def remove_friend_function(database, ask_username, save_database):
    # ask user for the username of the friend they'd like to remove 
    # check if the user exists in the database 
    # they have to be friends 
    # remove the inputted user from the current user's friend list 
    # remove the user from the friend's friend list 
    remove_friend = input("Who do you want to remove from your friends list? ")
    if remove_friend not in database:
        print("User does not exist!")
    if "friends" in database[ask_username] and remove_friend in database[ask_username]["friends"]:
        database[ask_username]["friends"].remove(remove_friend)
        database[remove_friend]["friends"].remove(ask_username)
        print("No longer friends with ", remove_friend)
        save_database(database)
    else:
        print("You are not friends with this user!")
                