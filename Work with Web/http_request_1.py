import requests

res = requests.get("https://news.ycombinator.com/")

res
# Output
< response[200] >

res.ok
# Output
True

res.headers
# Output
{'Server': 'nginx', 'Date': 'Sun, 28 Apr 2019 18:12:09 GMT',
'Content-Type': 'text/html; charset=utf-8',
'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive',
'Vary': 'Accept-Encoding', 'Cache-Control': 'private; max-age=0',
'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff',
'X-XSS-Protection': '1; mode=block', 'Referrer-Policy': 'origin',
blah, blah, blah...

res.text
# Output
Tons of html


# Make an actual page request
import requests

url = "http://www.google.com"
req = requests.get(url)

print(f"Your web request to {url} returned a status of {req.status_code}")

# Output
Your web request to http: // www.google.com returned a status of 200


# Make a text request to get back plain text from the webpage
import requests

url = "https://www.icanhazdadjoke.com"
req = requests.get(url, headers = {"Accept": "text/plain"})

print(req.text)

# Output
blah, blah, blah...

# Request data in json format
import requests

url = "https://www.icanhazdadjoke.com"
req = requests.get(url, headers={"Accept": "application/json"})

data = req.json()
print(data)

# Output
{'id': 'M7wPC5wPKBd', 'joke': 'Hear the one about the guy with the broken hearing aid? Neither did he.',
'status': 200}

# And this can be parsed just like a dictionary
print(data["joke"])
# Output
Hear the one about the guy with the broken hearing aid? Neither did he.

