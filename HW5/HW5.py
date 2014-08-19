from BeautifulSoup import BeautifulSoup
import csv 
from nltk.util import clean_html
import urllib2 
import time

# What page? 
page_to_scrape = 'http://phdtalk.blogspot.com/'

# What info do we want? 
headers = ["is_post", "publish_date", "author", "url", "post_title", "comment_count"]

# Where do we save info?
filename = "blog.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

while True:
# Open webpage
  webpage = urllib2.urlopen(page_to_scrape)
  
# Parse it
  soup = BeautifulSoup(webpage.read())
  soup.prettify()
  
# Extract petitions on page
  dates = soup.findAll("h2", attrs={"class":"date-header"})
  print len(dates)
  for date in dates:
    d = clean_html(str(date.find("span")))
    print d
  
  posts = soup.findAll("div", attrs={"class":"post hentry uncustomized-post-template"})
  print len(posts)
  for post in posts: # Each post has its own post id. 
    p = 0            # So, if the id is spotted, the value of p is recorded as 1.
    if clean_html(str(post.find("a")["name"])): p = 1
    print p
    
  authors = soup.findAll("a", attrs={"class":"g-profile"})
  print len(authors)
  for author in authors:
    a = clean_html(str(author.find("span")))
    print a
  
  urls = soup.findAll("h3", attrs={"class":"post-title entry-title"})
  print len(urls)
  for url in urls:
    u = clean_html(str(url.find("a")["href"]))
    print u
  
  titles = soup.findAll("h3", attrs={"class":"post-title entry-title"})
  print len(titles)
  for title in titles:
    t = clean_html(str(title.find("a")))
    print t
  
  comments = soup.findAll("span", attrs={"class":"post-comment-link"})
  print len(comments)
  for comment in comments:
    c = clean_html(str(comment.find("a"))).split()[0]
    if c == "No": c = 0
    print c
  
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
    csvwriter.writerow([p, d, a, u, t, c])
  if soup.find("a", attrs={"class":"blog-pager-older-link"}) == None: break # When there is no link to older posts, then this loop is broken.
  next = soup.find("a", attrs={"class":"blog-pager-older-link"})["href"] # Find new link to older posts
  page_to_scrape = next # Replace the current web page with the new link to older posts.
                        # So, it sorts the posts chronologically.
  time.sleep(2) # good citizenship rule :)
  
readFile.close()