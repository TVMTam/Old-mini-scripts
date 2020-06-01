"""http://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

Extras:
Ask the user to specify the name of the output file that will be saved."""
# ============================ FROM EXERCISE 17 ============================
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

# Retrieve all of the anchor tags
tags = soup.find_all(class_="story-heading")
with open('Ex_21.txt', 'w') as open_file:
    for tag in tags:
        temp = tag.get_text().strip()+'\n'
        print (temp)
        open_file.write(temp)
# ============================ FROM EXERCISE 17 ============================
