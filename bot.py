import praw
import time
import config

reddit= praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=config.user_agent,
    username=config.username,
    password=config.password,
    read_only=False
)

# Setting the subreddit and keywords
subreddit= reddit.subreddit("leetcode")
keywords = ["google", "interview"]

# Reply with a message
reply_message= "Hi, I'am bot created by brainy_bones. It seems like you're discussing Google interviews. Here is a helpful resource : https://github.com/snehasishroy/leetcode-companywise-interview-questions/blob/master/google.csv"

# Monitor and respond to the posts
for submission in subreddit.stream.submissions():
    if any (keyword in submission.title.lower() or keyword in submission.selftext.lower() for keyword in keywords):
        if not submission.saved:
            print(f"Replying to post: {submission.title}")
            submission.reply(reply_message)
            submission.save()  # Mark as replied to avoid duplicate replies
            time.sleep(10)  # Sleep to avoid rate-limiting




