from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

totcoms = 0
cnt = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
    cnt += 1
    tag_ = str(tag)
    nmbs = re.findall('[0-9]+', tag_)
    for nmb in nmbs:
        totcoms = totcoms + int(nmb)
print('Count', cnt)
print('Sum', totcoms)
