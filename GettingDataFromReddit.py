import praw
import datetime
import time
"""  1. upvotes
  2. upvotes over time after post
  3. time posted
  4. comments on a post
  5. array of comments of the post
  6. URL
  7. port into Excel for Nick
  8. lenght of post"""
def upvotesPerHour(submission, createdat):
    now = datetime.datetime.fromtimestamp(time.time(), datetime.timezone.utc)
    diff = now - createdat
    hours = ((diff.seconds / 60)/60)+24*diff.days
    return submission.score/hours

def timePosted(submission):
    createdat = datetime.datetime.fromtimestamp(submission.created_utc, datetime.timezone.utc)
    return createdat

"""full thing"""
reddit = praw.Reddit(client_id='gSpBr0PE7XcGnw',
                     client_secret='1T78VdUikAdZ0DXTA3IEDjnIXuw',
                     password='!@#$%^',
                     user_agent='test by /u/bakedBeans2010',
                     username='bakedBeans2010')

subreddit = reddit.subreddit('pics')

for submission in subreddit.hot(limit=10):
    upvotes = submission.score
    posted = timePosted(submission)
    rate = upvotesPerHour(submission,posted)
    numComments = len(submission.comments)
    arrayOfComments = submission.comments
    url = submission.url
    title = submission.title
    lengthOfPost = len(title)
    print(title+'('+str(lengthOfPost)+') score:'+str(upvotes)+' upvotes per hour:'+str(rate)+' has '+str(numComments)+' comments')

