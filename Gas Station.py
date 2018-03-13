import urllib.request,urllib.parse,urllib.error
import json
import ssl
#
# Fetch the API key from GOOGLE
serviceurlPlaceSearch = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
serviceurlGeocode = 'https://maps.googleapis.com/maps/api/geocode/json?'

loc = input("Enter location: ")
url = serviceurlGeocode +  urllib.parse.urlencode({'address':loc,'key':'##############################################'})

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(url,context=ctx).read().decode()
try:
    pythonicJson = json.loads(data)
except:
    pythonicJson = None

if pythonicJson == None or pythonicJson["status"]!="OK":
    print("Fatal Error")
    quit()

lat = pythonicJson["results"][0]["geometry"]["location"]["lat"]
lng = pythonicJson["results"][0]["geometry"]["location"]["lng"]

print("Latitude: ",lat)
print("Longitude: ",lng)

latLng = str(lat)+','+str(lng)
urlPlaceSearch = serviceurlPlaceSearch + urllib.parse.urlencode({'location':latLng,'radius':500,'type':'gas_station',
                                                                'key':'#####'})

dataGasStation = urllib.request.urlopen(urlPlaceSearch,context=ctx)
dataGasStation = dataGasStation.read().decode()

try:
    pythonicJsonGasStation = json.loads(dataGasStation)
except:
    pythonicJsonGasStation = None

if pythonicJsonGasStation == None or pythonicJsonGasStation["status"]!="OK":
    print("Fatal Error")
    quit()


for gasStation in pythonicJsonGasStation["results"]:

    print("Name: ",gasStation["name"])
    print("Latitude :",gasStation["geometry"]["location"]["lat"])
    print("Longitude :",gasStation["geometry"]["location"]["lng"])
