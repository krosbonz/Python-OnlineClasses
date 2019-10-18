import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''
#"json.loads(data)" takes the information in the json format and makes it avail in
#the variable "info"
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])