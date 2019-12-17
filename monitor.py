import praw
import os
import time
import datetime
import yaml

config = yaml.safe_load(open("config.yaml"))

reddit = praw.Reddit(client_id=config['client_id'],
					 client_secret=config['client_secret'],
					 user_agent=config['user_agent'])

clear = lambda: os.system('cls')
x=True

while x == True:
	clear()
	for submission in reddit.subreddit('buildapcsales').new(limit=5):
		subtime = submission.created
		print('------------------------------------------------------------\n')
		print(submission.title,'\n',datetime.datetime.fromtimestamp(subtime),'\n')
		print('------------------------------------------------------------')
		print('\n')
	for submission in reddit.subreddit('buildapcsales').hot(limit=1):
		subtime = submission.created
		print('--HOT--HOT--HOT--HOT--HOT--HOT--HOT--HOT--HOT--HOT--HOT--HOT--\n')
		print(submission.title,'\n',datetime.datetime.fromtimestamp(subtime),'\n')
		print('--HOT--HOT--HOT--HOT--HOT--HOT--HOT--HOT--HOT--HOT--HOT--HOT--')
		print('\n')
	for i in range(15):
		print(i+1, end="\r", flush=True)
		time.sleep(1)
	