import urllib.request, urllib.error, urllib.parse
import json
# Hidden is the py file that has a function hiddenKey() which returns a dictionary with CODEWARS API key
# API key can be found
# import hidden
import ssl
userCheckUrl = 'https://www.codewars.com/api/v1/users/'

while True:
    user = input("Check for a user: ")
    url = userCheckUrl + user + '/?'+ urllib.parse.urlencode({'access_key':
                                        hidden.hiddenKey()["key"]})
    print("\n Calling CODEWARS! HAVE PATIENCE")

    #Ignore SSL errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    data = urllib.request.urlopen(url,context=ctx)
    # print(data.getheaders())
    data = data.read().decode()
    try:
        pythonicJson = json.loads(data)
    except:
        pythonicJson = None
    if pythonicJson !=None:
        print("User Name: ",pythonicJson["username"])
        print("Screen Name: ",pythonicJson["name"])
        print("Points: ",pythonicJson["honor"])
        print("Leader Board Position: ",pythonicJson["leaderboardPosition"])
        if pythonicJson["skills"]:
            print("Skills")
            for index,skill in enumerate(pythonicJson["skills"]):
                print(index+1,".",skill)
        print("Kata Solved: ",pythonicJson["codeChallenges"]["totalCompleted"])
    else:
        print("Some error occurred")
