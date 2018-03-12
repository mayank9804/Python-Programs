# Json stands for Javascript Object Notation

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# When exchanging data between a browser and a server, the data can only be text.
# JSON is text, and we can convert any JavaScript object into JSON, and send JSON to the server.
# We can also convert any JSON received from the server into JavaScript objects.
# This way we can work with the data as JavaScript objects, with no complicated parsing and translations.


import json
jsonData = '''
{
    "name":"Chuck",
    "phone":{
        "type":"intl",
        "number":"+19814670363"
    },
    "email":{
        "hide":"yes"
    }
}
'''
jsonArrayObjects = '''[
{
    "id":"001",
    "x":"2",
    "name":"Chuck"
},
{
    "id":"002",
    "x":"3",
    "name":"Mayank"
}

]'''

pythonicJsonData = json.loads(jsonData) #json.loads uses JSON sring to convert it into dictionary
print("Data 1:\n")
print("Name: ",pythonicJsonData['name'])
print("Phone: ",pythonicJsonData['phone']['type'],'-',pythonicJsonData['phone']['number'])
print("Name: ",pythonicJsonData['email']['hide'])

print("\nData 2:")
pythonicJsonlist = json.loads(jsonArrayObjects)
print("User Counts:",len(pythonicJsonlist))
for pythonicItem in pythonicJsonlist:
    print("Id: ",pythonicItem['id'])
    print("Name: ",pythonicItem["name"])
