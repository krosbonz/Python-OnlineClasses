import json
#In this example the json data is between brackets which makes it a list
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info = json.loads(data)
#print('User count:', len(info))

#for item in info:
    #print('Name', item['name'])
    #print('Id', item['id'])
    #print('Attribute', item['x'])
print(info)