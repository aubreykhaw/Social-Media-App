def creating_post_function(posts, ask_username, save_posts):
    post = input("What is your post? ")
    posts.append({"username": ask_username, "post" : post})
    save_posts(posts)
def comment_post_function(posts, ask_username, save_posts):
    comment_post = input("Which post do you want to comment on? ")
    for post in posts:
        post_id = posts.index(post)
        if str(post_id) == comment_post:
            comment = input("What would you like to comment? " )
            save_posts(posts)
            if "comments" in post:
                post["comments"].append({"username": ask_username, "comment": comment })
                save_posts(posts)
            else:
                post["comments"] = [{"username": ask_username, "comment": comment}]
                save_posts(posts)
def like_post_function(posts, ask_username, save_posts):
    like_post = input("Which post do you want to like? ")
    for post in posts:
        post_id = posts.index(post)
        if str(post_id) == like_post:
            if "likes" in post:
                post["likes"] += 1
                save_posts(posts)
            else:
                post["likes"] = 1
                print("You liked the post!")
                save_posts(posts)
def delete_post_function(posts, ask_username, save_posts):
    delete_post = input("Which post do you want to delete? ")
    for post in posts:
        post_id = posts.index(post)
        if str(post_id) == delete_post:
            if post["username"] == ask_username:
                posts.remove(post)
                print("Post Deleted!")
                save_posts(posts)
            else:
                print("You can only delete your own posts!")
def edit_post_function(posts, ask_username, save_posts):
    edit_post = input("Which post do u want to edit? ")
    for post in posts:
        post_id = posts.index(post)
        if str(post_id) == edit_post:
            if post["username"] == ask_username:
                new_post = input("What is your new post? ")
                post["post"] = new_post
                print("Post Edited!")
                save_posts(posts)
            else:
                print("You can not edit this post!")
def display_posts_function(posts, save_posts):
        # display posts
    if len(posts) == 0:
        print("There are no posts yet!")
        save_posts(posts)
    c = ""
    for post in posts:
        for comment in post.get("comments") or []: 
            c = c + " comments: " + " " + "user: " + comment["username"]+ "," + " " + comment["comment"] + "|" 
        save_posts(posts)
        print("postId: " + str(posts.index(post)) + " | " + "user: " + post["username"] + " | " + "post: " + post["post"] + " | " + str(post.get("likes"))+ "likes" + " | ", c )
        post_id = posts.index(post)