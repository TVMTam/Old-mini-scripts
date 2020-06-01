"""http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the exercise posted here.)

This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file."""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
title = [soup.find(class_='hed').get_text()]
title.append(soup.find(class_='dek').string)
for i in range(len(title)):
    print(title[i]+'\n')
tags = soup.find_all('p')
for tag in tags:
    print (tag.get_text()+'\n')
