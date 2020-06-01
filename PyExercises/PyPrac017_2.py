'''http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
https://www.nytimes.com/'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.nytimes.com/'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text)
    else:
        print(story_heading.contents[0])
