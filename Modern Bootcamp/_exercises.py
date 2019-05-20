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


print("There are " + str(num_jokes) + " for the topic of " + topic + "." )
print(random.sample([data["results"]['joke']], 1))