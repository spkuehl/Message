from re import findall

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
        links = findall(r"http:\/\/t.co\/[a-zA-Z|0-9]+", self.text)
        filtered_links = []
        for i in links:
            if len(i) <= 22:
                filtered_links.append(i)
        return filtered_links