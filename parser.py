from re import findall


class Tweet:
    """A simple Tweet parser class"""

    def __init__(self, tweet):
        self.text = tweet

    def get_mentions(self):
        findall(r"@\w+", self.text)

    def get_topics(self):
        findall(r"Hello", self.text)


tweet = Tweet('Hello #world @twitter')
print(tweet.__doc__)
print(tweet.text)
print(tweet.get_mentions())
print(tweet.get_topics())
