class Tweet:
    """A simple Tweet parser class"""
    def __init__(self, tweet):
        self.text = tweet

tweet = Tweet('Hello World')
print(tweet.__doc__)
print(tweet.text)