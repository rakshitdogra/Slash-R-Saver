import os
import pyfiglet
import praw
import requests

print(pyfiglet.figlet_format("REDSAVE"))
print("\n")

# Reddit API credentials
client_id = input("Enter client_id: ")
client_secret = input("Enter client_secret: ")
username = input("Enter username: ")
password = input("Enter password: ")

# Subreddit name
subreddit_name = input("Enter subreddit name: ")

# Create a Reddit instance
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, username=username,password=password, user_agent="<user_agent>")

# Get the subreddit
subreddit = reddit.subreddit(subreddit_name)

# Directory to save the images/videos
save_dir = input("Enter the folder/directory name to save: ")

# Check if the directory exists, otherwise create it
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

#Entering the limit
Lim=input("Enter the Limit of posts requests you want to make: ")

print("SORT BY: 1.HOT / 2.NEW / 3.TOP : ")
Choice = str(input("Enter your choice 1/2/3 : "))
if Choice==1:
    # Loop through the hot submissions in the subreddit
    for submission in subreddit.hot(limit=Lim):
        # Check if the submission is an image or video
        if submission.url.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp4")):
            # Get the file name from the URL
            file_name = submission.url.split("/")[-1]
            file_path = os.path.join(save_dir, file_name)
            
            # Download the file using the `requests` library
            response = requests.get(submission.url)
            with open(file_path, "wb") as file:
                file.write(response.content)

    print("Command successfully executed!")
    print("Images/videos saved in the", save_dir, "directory.")
if Choice==2:
    # Loop through the new submissions in the subreddit
    for submission in subreddit.new(limit=Lim):
        # Check if the submission is an image or video
        if submission.url.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp4")):
            # Get the file name from the URL
            file_name = submission.url.split("/")[-1]
            file_path = os.path.join(save_dir, file_name)
            
            # Download the file using the `requests` library
            response = requests.get(submission.url)
            with open(file_path, "wb") as file:
                file.write(response.content)

    print("Command successfully executed!")
    print("Images/videos saved in the", save_dir, "directory.")

if Choice==3:
    ch=input("TOP BY today/week/month/year/all: ")
    # Loop through the top submissions in the subreddit
    for submission in subreddit.top(ch,limit=Lim):
        # Check if the submission is an image or video
        if submission.url.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp4")):
            # Get the file name from the URL
            file_name = submission.url.split("/")[-1]
            file_path = os.path.join(save_dir, file_name)
            
            # Download the file using the `requests` library
            response = requests.get(submission.url)
            with open(file_path, "wb") as file:
                file.write(response.content)

    print("Command successfully executed!")
    print("Images/videos saved in the", save_dir, "directory.")
else:
    pass
