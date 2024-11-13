# RedditBot_1

This project is a Reddit bot built using Python and the PRAW (Python Reddit API Wrapper) library. The bot monitors a specified subreddit for posts containing certain keywords, such as "Google" and "interview," and automatically replies with a helpful message.

Features
Keyword Monitoring: Tracks posts in a specified subreddit for user-defined keywords.
Automated Responses: Replies with a predefined message when matching keywords are found.
Spam Prevention: Marks replied posts to avoid duplicate replies.

Getting Started
Prerequisites
Python 3.x
PRAW library (pip install praw)
Reddit API credentials (client ID, client secret, username, password, user agent)

Setup
Clone the repository.
Create a config.py file to store your Reddit API credentials:
client_id = "your_client_id"
client_secret = "your_client_secret"
user_agent = "your_user_agent"
username = "your_reddit_username"
password = "your_password"
Ensure config.py is included in .gitignore to keep credentials secure.

Usage
Run the bot with:

python bot.py
The bot will start monitoring the specified subreddit and replying to posts containing the defined keywords.

License
This project is open-source and available under the MIT License.