import tweepy

# Credentials
api_key = "M0YowhWJg7r7m2JqeLeiacYIi"
api_secret = "V54h2GQXJ8Rl7wFf1nLjHlci5HkD9w8oejODIZPrMZporPNLDA"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMaTtQEAAAAAn%2BxlYRv%2BDyNjklR4P9J2n9fjhnw%3DXXTYJlBf0ioPU6ViESfxsRspcOr9uS1up858iReMezk6GvZtmm"
access_token = "1660326716647014400-kyz0TC02s53ZBUPhbONwuhRIfebDtG"
access_token_secret = "COC882V9wZMH5L2hVundXQDQw5WtVadm7KKcGFkn113jU"
consumer_key = "SjI2dGh4UnZsWm9vMktzLWdJZ186MTpjaQ"
consumer_secret = "p2wBTG5lsoLpR0G9rn0O51KhsrhwxQRr4U87amCoiuzrXosaub"

# Authentication
auth = tweepy.OAuth1UserHandler(
    api_key, api_secret,
    access_token, access_token_secret
)

# Stream listener class
class MyStreamListener(tweepy.StreamingClient):

    def on_status(self, status):
        print(f"Tweet ID: {status.id}")
        
        try:
            # Retweet the tweet
            api.retweet(status.id)
            
        except Exception as e:
            print(f"Error retweeting: {e}")

if __name__ == "__main__":

    # Create StreamingClient
    stream = tweepy.StreamingClient(
        auth=auth,
        listener=MyStreamListener(),
        bearer_token="AAAAAAAAAAAAAAAAAAAAAMaTtQEAAAAAn%2BxlYRv%2BDyNjklR4P9J2n9fjhnw%3DXXTYJlBf0ioPU6ViESfxsRspcOr9uS1up858iReMezk6GvZtmm"
    )
    
    # Filter by hashtag
    hashtag = "#الحرية_المالية"
    stream.filter(track=[hashtag])
