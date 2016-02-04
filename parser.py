from re import findall
import unittest

class Tweet:
    """A simple Tweet parser class"""

    def __init__(self, tweet):
        self.text = tweet

    def get_mentions(self):
        return findall(r"@\w+", self.text)

    def get_topics(self):
        return findall(r"#[^\W_]+", self.text)

    def get_links(self):
        return findall(r"(https:\/\/t.co\/)[a-zA-Z|0-9]{20}", self.text)


tweet = Tweet('Hello #world @twitter')
print(tweet.__doc__)
print(tweet.text)
print(tweet.get_mentions())
print(tweet.get_topics())
