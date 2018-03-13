import urllib.request, urllib.parse, urllib.error
import json
# import hidden
import twurl
import ssl

serviceurl = 'https://api.twitter.com/1.1/search/tweets.json?'
while True:
    searchQuery = input('Enter the keyword you would like to lookup on twitter').strip(' ')
    if len(searchQuery) < 1:
        continue

    print('Calling Twitter.......')
    url = serviceurl + urllib.parse.urlencode({'q':searchQuery})
    # This would require hidden.py file to get the important Access Token
    # hidden.py would return the following dictionary with your twitter keys
    # {"consumer_key":"",
    #         "consumer_secret":"",
    #         "access_token":"",
    #         "access_token_secret":""
    #         }

    furl = twurl.augment(url)

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    connection = urllib.request.urlopen(furl,context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    try:
        tweets = json.loads(data)
    except:
        tweets = None

    if tweets == None or headers["status"]!="200 OK":
        print("Fatal error")
        continue
    #print(json.dumps(pythonicJson,indent=4))
    inc = 1
    for tweet in tweets["statuses"]:

        print(inc,". ","Posted on: ",tweet["created_at"])
        print("Posted by : @" + tweet["user"]["screen_name"])
        print("Tweet reads: ", tweet["text"])
        if tweet['urls'][0]:
            inc+=1

        print("\n\n")

    print("Number of API calls remaining: ",headers['x-rate-limit-remaining'])
