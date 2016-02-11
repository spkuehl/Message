from re import findall

class Tweet:
    """A simple Tweet parser class"""

    def __init__(self, tweet):
        self.text = tweet

    def get_mentions(self):
        mention = findall(r"@[\w@]{1,20}", self.text)
        mention = [x for x in mention if x.count('@') == 1]
        filtered_mentions = []

        for m in mention:
            filtered = findall(r"@[\w]+", m)
            if len(filtered) == 1:
                if m == filtered[0]:
                    filtered_mentions.append(m)
        mention = filtered_mentions
        filtered_mentions = []

        for m in mention:
            if self.text.find(m) == 0:
                filtered_mentions.append(m)
            elif self.text[(self.text.find(m) - 1)] == ''\
            or self.text[(self.text.find(m) - 1)] == ' ':
                filtered_mentions.append(m)

        return filtered_mentions

    def get_topics(self):
        topics = findall(r"#[a-zA-Z][^\W_]+", self.text)
        filtered_topics = []

        for topic in topics:
            if self.text.find(topic) == 0:
                filtered_topics.append(topic)
            elif self.text[(self.text.find(topic) - 1)] == ''\
            or self.text[(self.text.find(topic) - 1)] == ' ':
                filtered_topics.append(topic)
        return filtered_topics

    def get_links(self):
        links = findall(r"http:\/\/t.co\/[a-zA-Z|0-9]+", self.text)
        filtered_links = []
        for i in links:
            if len(i) <= 22:
                filtered_links.append(i)
        return filtered_links