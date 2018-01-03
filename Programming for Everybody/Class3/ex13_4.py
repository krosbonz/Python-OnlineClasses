from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_40852.xml"
cnt = 0
tot = 0
html = urlopen(url, context=ctx).read()
stuff = ET.fromstring(html)
com = stuff.findall('comments/comment')

for item in com:
    cnt += 1
    tot = tot + int(item.find('count').text)
print('Count: ', cnt)
print('Sum: ', tot)