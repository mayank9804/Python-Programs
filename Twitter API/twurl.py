import hidden
import urllib.request,urllib.parse,urllib.error
import oauth2

# def augment(url,parameters):
#     secrets = hidden.oauth()
#     consumer = oauth.OAuthConsumer(secrets['consumer_key'],secrets['consumer_secret'])
#     token = oauth.OAuthToken(secrets['access_token'],secrets['access_token_secret'])
#
#     oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,token=token,
#                     http_method='GET',http_url=url,parameters=parameters)
#     oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
#                                 consumer,token)
#     return oauth_request.to_url()

def augment(url):
    secrets = hidden.oauth()
    consumer = oauth2.Consumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth2.Token(key=secrets['access_token'], secret=secrets['access_token_secret'])
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method='GET')

    return resp["content-location"]
#
# home_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/home_timeline.json', 'abcdefg', 'hijklmnop' )
