import tweepy
import config
import datetime
start = datetime.datetime(2022,5,30)
end = datetime.datetime(2022,6,5)
client = tweepy.Client(bearer_token = config.bearer_token)
query1 = "-is:retweet #nzvseng has:images "  #  -22.9122,-43.2302,1km #location hastag start end
response = client.search_recent_tweets(query = query1,
max_results=10,tweet_fields=['attachments','entities'],media_fields = ['preview_image_url','url','media_key'],start_time=start,end_time=end,expansions = ['author_id','attachments.media_keys'],user_fields=['url','entities','profile_image_url'])
# print(response)                               include_entities=True                                                                 #tweet.fields=attachments   #attachments.media_keys
# users = {u['id']: u for u in response.includes['users']}
for tweet in response.includes['media']:
    print(tweet.url)
    # if users[tweet.author_id]:
    #     user = users[tweet.author_id]
    #     print(user)
    #     print()
    #     # print(tweet.author_id)
    #     # user = users[tweet.author_id]
    #     # # print(tweet.attachments.media_keys)
    #     # print(user.includes.media_key)
    #     # # print(user.entities.media)
    
