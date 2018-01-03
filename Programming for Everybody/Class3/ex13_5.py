import urllib.request
import json

url = "http://py4e-data.dr-chuck.net/comments_40853.json"
cnt = 0
tot = 0
html = urllib.request.urlopen(url)
data = html.read().decode()

info = json.loads(data)

for i in info['comments']:
    tot = tot + (i['count'])
    cnt += 1

print('Count: ', tot)
print('Sum: ', cnt)





