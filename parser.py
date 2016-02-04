from re import findall
import unittest

class Tweet:
    """A simple Tweet parser class"""

    def __init__(self, tweet):
        self.text = tweet

    def get_mentions(self):
        mention = findall("@[\w@]{1,20}", self.text)
        mention = [x for x in mention if x.count('@') == 1]
        filtered_mentions = []

        for m in mention:
            filtered = findall("@[\w]+", m)
            if len(filtered) == 1:
                if m == filtered[0]:
                    filtered_mentions.append(m)

        return filtered_mentions

    def get_topics(self):
        return findall(r"#[a-zA-Z][^\W_]+", self.text)

    def get_links(self):
        return findall(r"(https:\/\/t.co\/)[a-zA-Z|0-9]{20}", self.text)

class TestTweetMethods(unittest.TestCase):

    def test_get_mentions(self):
        tweet = Tweet('This is a @test')
        self.assertEqual(tweet.get_mentions(), ['@test'])

    def test_get_mentions_max(self):
        tweet = Tweet('@01234567890123456789012345')
        self.assertEqual(tweet.get_mentions(),['@01234567890123456789'])

    def test_get_mentions_underscore(self):
        tweet = Tweet('@Under_Score')
        self.assertEqual(tweet.get_mentions(),['@Under_Score'])

    def test_get_mentions_nonalphaunderscore(self):
        tweet = Tweet('@replystopshere+right')
        self.assertEqual(tweet.get_mentions(),['@replystopshere'])

    def test_get_mentions_multiple(self):
        tweet = Tweet('Hi @randy and @kim')
        self.assertEqual(tweet.get_mentions(),['@randy', '@kim'])

    def test_get_mentions_no_reply(self):
        tweet = Tweet('I am talking to myself')
        self.assertEqual(tweet.get_mentions(),[])

    def test_get_mentions_empty_reply(self):
        tweet = Tweet('I am talking to no one @')
        self.assertEqual(tweet.get_mentions(),[])

    def test_get_mentions_at_in_mention(self):
        tweet = Tweet('@does@not@work')
        self.assertEqual(tweet.get_mentions(),[])

    def test_get_mentions_at_after_mention(self):
        tweet = Tweet('@01234567890123456789@')
        self.assertEqual(tweet.get_mentions(),[])

    def test_get_mentions_no_leading_at(self):
        tweet = Tweet('this@doesnothing')
        self.assertEqual(tweet.get_mentions(),[])

    def test_get_topics(self):
        tweet = Tweet('This is #trendingin2016')
        self.assertEqual(tweet.get_topics(),['#trendingin2016'])

    def test_get_topics_multiple(self):
        tweet = Tweet('#one #two #three')
        self.assertEqual(tweet.get_topics(),['#one','#two','#three'])

    def test_get_topics_start_with_num(self):
        tweet = Tweet('#2016trending')
        self.assertEqual(tweet.get_topics(),[])

    def test_get_topics_contain_non_leading_hash(self):
        tweet = Tweet('#this#doesnothing')
        self.assertEqual(tweet.get_topics(),[])

    def test_get_topics_non_leading_hash(self):
        tweet = Tweet('thisdoesnot#workeither')
        self.assertEqual(tweet.get_topics(),[])

    def test_get_topics_underscore(self):
        tweet = Tweet('#thiscuts_off')
        self.assertEqual(tweet.get_topics(),['#thiscuts'])

    def test_get_links(self):
        tweet = Tweet('dont click random link http://t.co/f5E8eGREwq')
        self.assertEqual(tweet.get_topics(),['http://t.co/f5E8eGREwq'])



def main():
    tweet = Tweet('Hello #comp330 @student')
    print(tweet.__doc__)
    unittest.main()


if __name__ == '__main__':
    main()