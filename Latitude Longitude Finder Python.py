
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# This is the base URL to which we extend our query
# This is done in accordance to Google Map API's

# Inputs the address
# Encodes it to UTF-8 and concatenates to the service url
# The Google Map API responds with JSON String which is
# converted into Python dictionary
# And according to API docs, latitiude and longitude are displayed

while True:
    address = input('Enter Location: ')
    if len(address) < 1:
        print("Please enter an address")
        continue

    print('Retrieving :',address)
    url = serviceurl + urllib.parse.urlencode({'address':address})
    jsonifyData = urllib.request.urlopen(url).read().decode()
    print('Retrieved', len(jsonifyData), 'characters')

    try:
        pythonicJson = json.loads(jsonifyData)
    except:
        pythonicJson = None

    if pythonicJson == None or pythonicJson['status'] != 'OK':
        print('Fatal Error! Look at the data')
        print(pythonicJson)
        continue
    else:
        print(json.dumps(pythonicJson,indent=4))

        print("Latitude",pythonicJson["results"][0]["geometry"]["location"]["lat"])
        print("Longitude",pythonicJson["results"][0]["geometry"]["location"]["lng"])
