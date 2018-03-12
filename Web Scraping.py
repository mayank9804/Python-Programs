from urllib.request import urlopen
from bs4 import BeautifulSoup

#Input the url from user
url = input('Enter - ')
#Fetch the HTML from URL
html = urlopen(url).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser

# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
# It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.
# It commonly saves programmers hours or days of work.
soup = BeautifulSoup(html, "html.parser")
sumNum = 0
# Retrieve all of the span tags
#eg: a = <span>Hello World</span>
# a.content[0] = Hello

tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    sumNum += int(tag.contents[0])

print(sumNum)




# The python program below scans a url provided by user!
# All the <a> tags are retrieved from the parsed HTML file
# Now these anchor tags if contains another url, goes to that URl
# '''(This redirection happens for some input dependent on count and
# retrieves a particular anchorTag in every redirection according to position )'''
url = input("Enter URL: ")
count = int(input("Enter count: "))
pos = int(input("Enter position: "))
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
anchorTags = soup('a')

while count > 1:
    anchorTags = BeautifulSoup(urllib.request.urlopen(anchorTags[pos-1].get('href',None)).read(),"html.parser")('a')
    count-=1

print(anchorTags[pos-1].contents[0])
