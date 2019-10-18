# Determine webpage status. 
# NOTE: Must install "requests" package

import requests
res = requests.get("https://news.ycombinator.com")
res
# Output
<Response [200]>

import requests
url = "https://google.com"
response = requests.get(url)
print(response)
# Output
<Response [200]>
# Or
print(response.status_code)
# Output
200
# If you print "response.text" you will get all of the sites HTML


# Request a site's plain text
import requests
url = "https://icanhazdadjoke.com"

response = requests.get(url, headers={"Accept": "text/plain"})

print(response.text)
# Output will only be the site's plain text

# Request JSON
response = requests.get(url, headers={"Accept": "application/json"})
data = response.json()
print(data)
# Output
{'id': '08xHQCdx5Ed', 'joke': 'Why didn’t? Because he had no guts.', 'status': 200}
# NOTE: This is a dictionary, but if we had used "response.text"
# it would have returned actual JSON


# This is specific to this website, but is an example of programmtically
# getting data from a site;
import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url, headers={"Accept": "application/json"}, 
    params={"term": "cat", "limit": 1})

data = response.json()
print(data["results"])
# Output
[{'id': 'iGJeVKmWDlb', 'joke': 'My cat was sick, I don’t think it’s feline well.'}]


# Exercise - fully functional user input, output one random joke
import requests
import random

url = "https://icanhazdadjoke.com/search"

topic = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
    url, headers={"Accept": "application/json"}, 
    params={"term": topic})

data = response.json()
num_jokes = len(data["results"])

if num_jokes > 0:
    print("I've got " + str(num_jokes) + " jokes about " + topic + "s. Here's one: " )
    print(data["results"][random.randrange(num_jokes)]["joke"])
else:
    print("Sorry, I don't have any jokes about "+ topic +". Please try again.")