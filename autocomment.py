import tweepy

# enter your Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY_HERE"
consumer_secret = "YOUR_CONSUMER_SECRET_HERE"
access_token = "YOUR_ACCESS_TOKEN_HERE"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET_HERE"

# authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create API object
api = tweepy.API(auth)

# search for tweets containing a specific word
search_query = "python"
tweets = api.search(q=search_query, lang="en")

# loop through the tweets and comment under the word "python"
for tweet in tweets:
    text = tweet.text
    if "python" in text.lower():
        # get the word index and add 1 to avoid commenting on the word itself
        word_index = text.lower().find("python") + 1
        comment = f"Hey @{tweet.user.screen_name}, I love {search_query} too!"
        api.update_status(
            status=comment,
            in_reply_to_status_id=tweet.id,
            auto_populate_reply_metadata=True,
            exclude_reply_user_ids=[tweet.user.id],
            attachment_url=tweet.entities["urls"][0]["url"],
            attachment_type="media"
        )
        print(f"Commented on tweet from @{tweet.user.screen_name}: {comment}")
