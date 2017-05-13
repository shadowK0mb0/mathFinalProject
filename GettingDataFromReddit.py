import praw
import datetime
import time
import xlwt

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

response = input('Print data to Excel? Answer Y/N: ')
if response=='Y':
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    sheet1.write(0, 0, 'upvotes')
    sheet1.write(0, 1, 'posted')
    sheet1.write(0, 2, 'rate')
    sheet1.write(0, 3, 'numComments')
    sheet1.write(0, 4, 'url')
    sheet1.write(0, 5, 'title')
    sheet1.write(0, 6, 'lengthOfPost')

inc = 1 #for use in row count

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
    if response=='Y':
        sheet1.write(inc,0,upvotes)
        sheet1.write(inc, 1, str(posted))
        sheet1.write(inc, 2, rate)
        sheet1.write(inc, 3, numComments)
        sheet1.write(inc, 4, url)
        sheet1.write(inc, 5, title)
        sheet1.write(inc, 6, lengthOfPost)
        inc = inc+1
if response=='Y':
    book.save("RedditData.xls")