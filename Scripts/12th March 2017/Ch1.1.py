
from urllib.request import urlopen 
#Retrieve HtML string from the URL 
html= urlopen("http://pythonscraping.com/exercises/exercise1.html")
print(html.read())

