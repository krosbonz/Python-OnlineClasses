import urllib.request, urllib.parse, urllib.error
import json


serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#This is the base URL required to do address lookups. The Remaining part is what is added after the "?"
#This information will be provided in the code below

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})
#This concatinates the URL above and the remaining address pieces. 
# The "urlllib...." formats the address as required by Google as part of the API 

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
#Open the URL
    data = uh.read().decode()
#Requires decoding from UTF-8 to Unicode
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
#This parses the information returned by Google. It is in the format of json (dictionary/lists)

    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
#The information returned from Google has a "status" and it must return "OK"
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
#Results sub zero "[0]" is due to the Google information returned as a list
#This walks down the tree to get results>geometry>location>latitude
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)