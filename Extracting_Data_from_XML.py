# The program will prompt for a URL,
# Read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data,
# Compute the sum of the numbers in the file.

import xml.etree.ElementTree as ET
import urllib

url = raw_input("enter url")
if(len(url) < 1):
    url = "http://python-data.dr-chuck.net/comments_270121.xml"
urlstring = urllib.urlopen(url).read()
parsedxml = ET.fromstring(urlstring)
lst = parsedxml.findall('comments/comment/count')
sum = 0
for item in lst:
    sum += int(item.text)
print sum
