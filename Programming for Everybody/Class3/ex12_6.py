from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cnt = 0
namelnks = []
url = "http://py4e-data.dr-chuck.net/known_by_Beinn.html"
while cnt < 7:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    namelnks = []
    tags = soup('a')
    for tag in tags:
        namelnks.append(tag.get('href', None))
    cnt += 1
    url = namelnks[17]
    print(url)