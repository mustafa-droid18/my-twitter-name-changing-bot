import tweepy
api_key = 'cSZyz1lc8r53bQ8I7wCZaMenJ'
api_secret_key = 'AQg6fbbdy1DN9YhHQQHzKhLGjJDNU8giA1Szo25kW89u73uUW9'
access_token = '1341737756829966337-y7RaJz4lNibHJ5IjUEsyXd7wCRrb8N'
secret_access_token = 'VJgRilB0GXm0qWyXPK4rZ9171PrchoftEQ7QJz5KDrc77'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, secret_access_token)

api=tweepy.API(auth)
import time
while True:
  user = api.get_user('Mustafa96934990')
  follower = user.followers_count
  api.update_profile(name= f'Mustafa {follower}')
  print(f'Mustafa {follower}')
  time.sleep(60)
