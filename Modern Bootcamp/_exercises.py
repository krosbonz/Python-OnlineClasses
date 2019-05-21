# # Define function, accepts multiple lists, returns True if contains 
# # Python keyword


# from keyword import iskeyword

# def contains_keyword(*args):
#     return any([x for x in args if iskeyword(x)])
    
        


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
