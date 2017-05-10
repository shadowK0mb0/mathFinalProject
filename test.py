import praw

reddit = praw.Reddit(client_id='gSpBr0PE7XcGnw',
                     client_secret='1T78VdUikAdZ0DXTA3IEDjnIXuw',
                     password='!@#$%^',
                     user_agent='test by /u/bakedBeans2010',
                     username='bakedBeans2010')

subreddit = reddit.subreddit('showerthoughts')

for submission in subreddit.hot(limit=10):
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.id)     # Output: the submission's ID
    print(submission.url)