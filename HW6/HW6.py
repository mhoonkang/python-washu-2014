import tweepy
import time
import calendar
import datetime

#First parameter is Consumer Key, second is Consumer Secret 
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')    
api = tweepy.API(auth)

#The most followed user that follows the target
Adam_Long = api.get_user(screen_name="Adam_B_Long") # get the target's user information
Adam_friends = api.followers_ids(Adam_Long.screen_name) # get IDs of users following the target
best = 0 # create a baseline for comparing the number of followers.
print "Now in process..."
for f in Adam_friends:
  try:
      user_info = api.get_user(f)
      if best < user_info.followers_count:
         best = user_info.followers_count
         mostguy = user_info.name
      elif best == user_info.followers_count:#just in case that there are more than one most followed users.
         mostguy = mostguy + ", " + user_info.name
      else:
         pass
  except tweepy.TweepError:# Check when to try again if rate limited.(from http://stackoverflow.com/questions/18053514/tweepy-hipchat-api-except-rate-limit)
  	  print "Waiting for rate limit reset" # printing now waiting for rate limit reset.
  	  rate_info=api.rate_limit_status()['resources']
  	  reset_time = rate_info['users']['/users/show/:id']['reset']
  	  current_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
  	  try_again_time = reset_time - current_time + 5 #wait the minimum time necessary plus a few seconds to be safe
  	  time.sleep(try_again_time) # try again in try_again_time seconds
  	  print "Now in process..."
print "The most followed user(s) is(are) {0}. ({1} followers)".format(mostguy, best)

# the most followed user that has at most 2 degrees of separation from the target
for f in Adam_friends: #followers of the target
  try: 
    second_follower = api.followers_ids(f)
    try: 
      for ff in second_follower: #followers of the follower of the target
  	      user_info = api.get_user(ff)
  	      if best < user_info.followers_count: #the initial value of 'best' is the number of follower for the most followed user that follows the target
  	         best = user_info.followers_count
  	         mostguy = user_info.name #the initial value of 'mostguy' is the name of the most followed user that follows the target
  	      elif best == user_info.followers_count:
  	         mostguy = mostguy + ", " + user_info.name
  	      else:
  	         pass
    except tweepy.TweepError:
      print "Waiting for rate limit reset" 
      rate_info = api.rate_limit_status()['resources']
      reset_time = rate_info['users']['/users/show/:id']['reset']
      current_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
      try_again_time = reset_time - current_time + 5
      time.sleep(try_again_time)
      print "Now in process..."
  except tweepy.TweepError:
  	print "Waiting for rate limit reset"
  	rate_info = api.rate_limit_status()['resources']
  	reset_time = rate_info['users']['/users/show/:id']['reset']
  	current_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
  	try_again_time = reset_time - current_time + 5
  	time.sleep(try_again_time)
  	print "Now in process..."
print "The most followed user(s) that has at most 2 degrees of separation from the target is(are) {0}. ({1} followers)".format(mostguy, best)


# Definition: I will define 'the most active user' as the user who makes the most tweets in a day.
# (tweets include retweet)
# So, I take the average of the number of tweets a user makes. To do this, I take the total number of 
# tweets of a user and divide it by the days for which the user has had the account.

#The most active user that has at most 2 degrees of separation from your target
best = 0 #create a baseline 
today = datetime.datetime.now()#today's date

#Find the most active user that has 1 degree of separation from the target
print "Now in process..."
for f in Adam_friends:
  try:
      user_info = api.get_user(f)
      statuses_count = user_info.statuses_count #the total number of tweets the user made 
      account_created_at = user_info.created_at #the date when the user created her/his own account
      days = today - account_created_at # the days for which the user has had the account 
      tweet_per_day = statuses_count/float(days.days) # tweet per day since the user made the account
      if best < tweet_per_day:
         best = tweet_per_day
         mostguy = user_info.name
      elif best == tweet_per_day:#just in case that there are more than one most active users.
         mostguy = mostguy + ", " + user_info.name
      else:
         pass
  except tweepy.TweepError:# Check when to try again if rate limited.(from http://stackoverflow.com/questions/18053514/tweepy-hipchat-api-except-rate-limit)
  	  print "Waiting for rate limit reset" # printing now waiting for rate limit reset.
  	  rate_info=api.rate_limit_status()['resources']
  	  reset_time = rate_info['users']['/users/show/:id']['reset']
  	  current_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
  	  try_again_time = reset_time - current_time + 5 #wait the minimum time necessary plus a few seconds to be safe
  	  time.sleep(try_again_time) # try again in try_again_time seconds
  	  print "Now in process..."

#Find the most active user that has 2 degrees of separation from the target
for f in Adam_friends: #followers of the target
  try: 
    second_follower = api.followers_ids(f) # the users that follow the follower of the target
    try: 
      for ff in second_follower: 
  	      user_info = api.get_user(ff)
  	      statuses_count = user_info.statuses_count
          account_created_at = user_info.created_at
          days = today - account_created_at
          tweet_per_day = statuses_count/float(days.days)
          if best < tweet_per_day: #the initial value of 'best' is the number of tweet per day for the most active user that follows the target
             best = tweet_per_day
             mostguy = user_info.name
          elif best == tweet_per_day:#just in case that there are more than one most active users.
             mostguy = mostguy + ", " + user_info.name
          else:
             pass
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
print "The most active user(s) that has at most 2 degrees of separation from the target is(are) {0}. \n({1} tweets per day since the creation of the account)".format(mostguy, best)


#The most active user being followed by the target
Adam_friends = api.friends_ids(Adam_Long.screen_name) # get IDs of users being followed by the target
best = 0 #create a baseline 
today = datetime.datetime.now()#today's date

print "Now in process..."
for f in Adam_friends:
  try:
      user_info = api.get_user(f)
      statuses_count = user_info.statuses_count #the total number of tweets the user made 
      account_created_at = user_info.created_at #the date when the user created her/his own account
      days = today - account_created_at # the days for which the user has had the account 
      tweet_per_day = statuses_count/float(days.days) # tweet per day since the user made the account
      if best < tweet_per_day:
         best = tweet_per_day
         mostguy = user_info.name
      elif best == tweet_per_day:#just in case that there are more than one most active users.
         mostguy = mostguy + ", " + user_info.name
      else:
         pass
  except tweepy.TweepError:# Check when to try again if rate limited.(from http://stackoverflow.com/questions/18053514/tweepy-hipchat-api-except-rate-limit)
  	  print "Waiting for rate limit reset" # printing now waiting for rate limit reset.
  	  rate_info=api.rate_limit_status()['resources']
  	  reset_time = rate_info['users']['/users/show/:id']['reset']
  	  current_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
  	  try_again_time = reset_time - current_time + 5 #wait the minimum time necessary plus a few seconds to be safe
  	  time.sleep(try_again_time) # try again in try_again_time seconds
  	  print "Now in process..."
print "The most active user(s) being followed by the target is(are) {0}. \n({1} tweets per day since the creation of the account)".format(mostguy, best)
