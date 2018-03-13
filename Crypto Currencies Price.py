import urllib.request,urllib.parse
import json

serviceurl = 'https://api.coinmarketcap.com/v1/ticker/'

while True:
    print("1. List prices of top 10 crypto keys.")
    print("2. Search for a specific crypto")
    print("3. List prices of top 10 crypto keys in INR")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = urllib.request.urlopen(serviceurl+'?'+urllib.parse.urlencode({'limit':10}))
        print(data.getheaders())
        data = data.read().decode()
        pythonicJson = json.loads(data)

        for crypto in pythonicJson:
            print(crypto["rank"],crypto["name"])
            print("Price: $"+crypto["price_usd"])

    elif choice == 2:
        cryptoCoin = input("Enter the name of crypto: ")
        data = urllib.request.urlopen(serviceurl+cryptoCoin).read().decode()
        crypto = json.loads(data)

        print(crypto[0]["rank"],crypto[0]["name"])
        print("Price: $"+crypto[0]["price_usd"])

    elif choice == 3:
        data = urllib.request.urlopen(serviceurl+'?'+urllib.parse.urlencode({'convert':"INR",'limit':"10"})).read().decode()
        pythonicJson = json.loads(data)

        for crypto in pythonicJson:
            print(crypto["rank"],crypto["name"])
            print("Price: Rs."+crypto["price_inr"])
            print("\n")
    else:
        print("Invalid choice! Please try again.")
