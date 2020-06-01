'''http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
https://www.nytimes.com/'''#I still dont understand why it's still different? the print statement shown same texts
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
emp1=[]
emp2=[]
tags = soup.find_all(class_="story-heading")
for story_heading in tags:
    emp2.append(str(story_heading.get_text().strip())) #add to list emp2
    print(str(story_heading.get_text().strip()))

    if story_heading.a:
        emp1.append(str(story_heading.a.text.replace("\n", " ").strip()))
        print(str(story_heading.a.text.replace("\n", " ").strip()))
    else:
        emp1.append(str(story_heading.contents[0].strip()))
        print(str(story_heading.contents[0].strip()))
print(len(emp1),len(emp2))
count = 0
for i in range(len(emp1)):
    if i != emp2[i]:
        print("Different")
        print(emp1[i])
        print(emp2[i])
        count +=1
print(count)
#I still dont understand why it's still different? the print statement shown same texts
