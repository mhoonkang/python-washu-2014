from BeautifulSoup import BeautifulSoup
import csv 
from nltk.util import clean_html
import urllib2 
import time
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_, DateTime, Float
from sqlalchemy.orm import relationship, backref, sessionmaker
import tweepy
import calendar
import datetime

## The following codes enable us to directly store information from the webs into database.


## part 1
engine = sqlalchemy.create_engine('sqlite:///c:\\Users\\Myunghoon\\python\\blog.db', echo=True)
Base = declarative_base()

# Scrapes Table
class Scrapes(Base):
  __tablename__ = "scrapes"
  
  id = Column(Integer, primary_key=True)
  is_post = Column(Integer)
  date = Column(String)
  num_comment = Column(Integer)
  url = Column(String)
  title = Column(String)
  author = Column(String)
  source_id = Column(Integer, ForeignKey('source.id'))
  
    
  def __init__(self, is_post, date, url, title, author, num_comment):
    self.is_post = is_post
    self.date = date
    self.url = url
    self.title = title
    self.author = author
    self.num_comment = num_comment
  def __repr__(self):
    return "<Is_post: {0}. date: {1}. url: {2}. title: {3}. the number of comments: {4}>".format(self.is_post, self.date, self.url, self.title, self.num_comment)

# Source model
class Source(Base):
  __tablename__ = "source"
  
  id = Column(Integer, primary_key=True)
  source_name = Column(String)
  source_url = Column(String)
  scrape = relationship("Scrapes", backref="source", uselist=True)
  
  def __init__(self, name, url):
    self.source_name = name
    self.source_url = url
  
  def __repr__(self):
    return "<Source name: {0}, Source URL: {1}>" .format(self.source_name, self.source_url)

#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

# What page? 
page_to_scrape = 'http://phdtalk.blogspot.com/'

while True:
# Open webpage
  webpage = urllib2.urlopen(page_to_scrape)
  
# Parse it
  soup = BeautifulSoup(webpage.read())
  soup.prettify()
  
# Extract petitions on page
  dates = soup.findAll("h2", attrs={"class":"date-header"})
  posts = soup.findAll("div", attrs={"class":"post hentry uncustomized-post-template"})
  urls = soup.findAll("h3", attrs={"class":"post-title entry-title"})
  titles = soup.findAll("h3", attrs={"class":"post-title entry-title"})
  comments = soup.findAll("span", attrs={"class":"post-comment-link"})
  authors = soup.findAll("a", attrs={"class":"g-profile"})

  for i in range(len(dates)):
    post = posts[i]
    p = 0
    if clean_html(str(post.find("a")["name"])): p = 1
    date = dates[i]
    d = clean_html(str(date.find("span")))
    author = authors[i]
    a = clean_html(str(author.find("span")))
    url = urls[i]
    u = clean_html(str(url.find("a")["href"]))
    title = titles[i]
    t = clean_html(str(title.find("a")))
    comment = comments[i]
    c = clean_html(str(comment.find("a"))).split()[0]
    if c == "No": c = 0
  table_source = Source("Ph D talk", 'http://phdtalk.blogspot.com/')
  session.add(table_source)
  table_scrape = Scrapes(p,d,u,t,a,c)
  table_source.scrape.append(table_scrape)
  session.add(table_scrape)
  if soup.find("a", attrs={"class":"blog-pager-older-link"}) == None: break # When there is no link to older posts, then this loop is broken.
  next = soup.find("a", attrs={"class":"blog-pager-older-link"})["href"] # Find new link to older posts
  page_to_scrape = next # Replace the current web page with the new link to older posts.
  time.sleep(.25) # good citizenship rule :)
  print "I'm working"
session.commit()  

## Part 2

engine = sqlalchemy.create_engine('sqlite:///c:\\Users\\Myunghoon\\python\\twitter.db', echo=True)
Base = declarative_base()

## Users Model
class Users(Base):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer)
  user_name = Column(String)
  follower_count = Column(Integer)
  account_created_at = Column(DateTime)
  total_tweets = Column(Integer)
  tweet_per_day = Column(Integer)
  crawls_id = Column(Integer, ForeignKey('crawls.id'))
  
    
  def __init__(self, user_id, name, follower_count, created_at, tweets):
    self.user_id = user_id
    self.user_name = name
    self.follower_count = follower_count
    self.account_created_at = created_at
    self.total_tweets = tweets
    self.tweet_per_day = tweets/float((datetime.datetime.now() - account_created_at).days)
  def __repr__(self):
    return "<User ID: {0}. User Name: {1}. Followers: {2}. Following: {3}. Days: {4}. Tweets: {5}. Tweet per day: {6}.>".format(self.user_id, self.user_name, self.follower_count, self.following_count, self.days, self.tweets, self.tweet_per_day)

## Crawls table
class Crawls(Base):
  __tablename__ = "crawls"
  
  id = Column(Integer, primary_key=True)
  starting_user_id = Column(Integer)
  time = Column(DateTime)
  user = relationship("Users", backref="crawls", uselist=True)
  
  def __init__(self, user_id, time):
    self.starting_user_id = user_id
    self.time = time
  def __repr__(self):
    return "<Starting User ID: {0}, Initiation Time: {1}>" .format(self.starting_user_id, self.time)

#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()


auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')    
api = tweepy.API(auth)

# The following code will store all the information that we need for our purpose into SQL database.
# So, We can find the most followed user, the most active user by using query.
# It means that the only thing we need to do is to scrape the related information and to store it into SQL database.

#1 degree of separation from the target
Adam_Long = api.get_user(screen_name="Adam_B_Long") # get the target's user information
Adam_friends = api.followers_ids(Adam_Long.screen_name) # get IDs of users following the target
print "Now in process..."
initiation_time = datetime.datetime.now()
for f in Adam_friends:
  try:
  	  user_info = api.get_user(f)
  	  statuses_count = user_info.statuses_count #the total number of tweets the user made 
  	  account_created_at = user_info.created_at #the date when the user created her/his own account
  	  table_crawl = Crawls(Adam_Long.id, initiation_time)
  	  session.add(table_crawl)
  	  table_user = Users(f, user_info.name, user_info.followers_count, user_info.created_at, statuses_count)  
  	  table_crawl.user.append(table_user)
  	  session.add(table_user)
  except tweepy.TweepError:# Check when to try again if rate limited.(from http://stackoverflow.com/questions/18053514/tweepy-hipchat-api-except-rate-limit)
  	  print "Waiting for rate limit reset" # printing now waiting for rate limit reset.
  	  rate_info=api.rate_limit_status()['resources']
  	  reset_time = rate_info['users']['/users/show/:id']['reset']
  	  current_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
  	  try_again_time = reset_time - current_time + 5 #wait the minimum time necessary plus a few seconds to be safe
  	  time.sleep(try_again_time) # try again in try_again_time seconds
  	  print "Now in process..."
  	  
#2 degrees of separation from the target
print "Now in process..."
for f in Adam_friends: #followers of the target
  try: 
    second_follower = api.followers_ids(f) # the users that follow the follower of the target
    initiation_time = datetime.datetime.now()
    try: 
      for ff in second_follower: 
  	     user_info = api.get_user(ff)
  	     statuses_count = user_info.statuses_count #the total number of tweets the user made 
  	     account_created_at = user_info.created_at #the date when the user created her/his own account
  	     table_crawl = Crawls(f, initiation_time)
  	     session.add(table_crawl)
  	     table_user = Users(ff, user_info.name, user_info.followers_count, user_info.created_at, statuses_count)  
  	     table_crawl.user.append(table_user)
  	     session.add(table_user)
    except tweepy.TweepError:
      print "Waiting for rate limit reset" 
      rate_info = api.rate_limit_status()['resources']
      reset_time = rate_info['users']['/users/show/:id']['reset']
      current_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
      try_again_time = reset_time - current_time + 5
      time.sleep(try_again_time)
      print "Now in processing..."
  except tweepy.TweepError:
  	print "Waiting for rate limit reset"
  	rate_info = api.rate_limit_status()['resources']
  	reset_time = rate_info['users']['/users/show/:id']['reset']
  	current_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
  	try_again_time = reset_time - current_time + 5
  	time.sleep(try_again_time)
  	print "Now in process..."

#The information of users being followed by the target (1 degree of separation)
Adam_friends = api.friends_ids(Adam_Long.screen_name) # get IDs of users being followed by the target

print "Now in process..."
initiation_time = datetime.datetime.now()
for f in Adam_friends:
  try:
      user_info = api.get_user(f)
      statuses_count = user_info.statuses_count #the total number of tweets the user made 
      account_created_at = user_info.created_at #the date when the user created her/his own account
      table_crawl = Crawls(Adam_Long.id, initiation_time)
      session.add(table_crawl)
      table_user = Users(f, user_info.name, user_info.followers_count, user_info.created_at, statuses_count)  
      table_crawl.user.append(table_user)
  except tweepy.TweepError:# Check when to try again if rate limited.(from http://stackoverflow.com/questions/18053514/tweepy-hipchat-api-except-rate-limit)
  	  print "Waiting for rate limit reset" # printing now waiting for rate limit reset.
  	  rate_info=api.rate_limit_status()['resources']
  	  reset_time = rate_info['users']['/users/show/:id']['reset']
  	  current_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
  	  try_again_time = reset_time - current_time + 5 #wait the minimum time necessary plus a few seconds to be safe
  	  time.sleep(try_again_time) # try again in try_again_time seconds
  	  print "Now in process..."
print "The most active user(s) being followed by the target is(are) {0}. \n({1} tweets per day since the creation of the account)".format(mostguy, best)

session.commit()