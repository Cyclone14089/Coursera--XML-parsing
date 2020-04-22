import xml.etree.ElementTree as et
import urllib.request, urllib.parse, urllib.error

url = input("Enter location: ")
print("Retrieving",url)
content = urllib.request.urlopen(url).read()

stuff = et.fromstring(content)
lst = stuff.findall('.//comment')
print('Retrieved',len(content),'characters')
print('Count:',len(lst))
s = 0

for item in lst :
    i = item.find('count').text
    s = s + int(i)

print('Sum:',s)
