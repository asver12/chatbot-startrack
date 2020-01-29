import random
import os
import json
from chatbot_startrek import json_reader, Sentences
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')


class StarTrackHandler:
    def __init__(self, path, file, sentiment_file="sentiment_data.json",neg_border=0.1,positive_border= 0.1):
        """
        Dataset structure:
        Series -> episodes -> character
        """

        self.sid = SentimentIntensityAnalyzer()
        self.data = json_reader.read_json(os.path.join(path, file))
        self.series = self.get_series()
        self.characters = self.get_characters()
        self.sentiment_data = []
        self.sentiment = self.load_sentiment_data(path, sentiment_file, neg_border, positive_border)

    def load_sentiment_data(self, path, file, neg_border=0.1, positive_border=0.1):
        if os.path.isdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                print("Loading sentiment data")
                with open(file_path) as target:
                    return json.load(target)
            else:
                sentiment = {"neg": [], "neu": [], "pos": []}
                for series in self.data.values():
                    for episode in series.values():
                        for character in episode.values():
                            for sentence in character:
                                if len(sentence) != 0:
                                    sentiment[self.get_sentiment(sentence, neg_border, positive_border)].append(sentence)

                with open(file_path, "w") as target:
                    json.dump(sentiment, target)
                return sentiment
        else:
            raise FileNotFoundError("Path: {} does not exist".format(path))

    def get_sentiment(self, sentence, neg_border=0.1, positive_border=0.1):
        if self.sid.polarity_scores(sentence)["neg"] > neg_border:
            return "neg"
        elif self.sid.polarity_scores(sentence)["pos"] > positive_border:
            return "pos"
        else:
            return "neu"

    def get_sentiment_sentence(self, user_input, sentiment, neg_border=0.1, positive_border=0.1):
        return random.choice(self.sentiment[self.get_sentiment(user_input, neg_border, positive_border)])

    def get_random_sentence(self, series=None, episode=None, character=None, iter=10000):
        sentences = []
        options = True
        if not series:
            _series = random.choice(list(self.data.keys()))
        else:
            _series = series
        if not episode:
            _episode = random.choice(list(self.data[_series].keys()))
        else:
            _episode = episode
        if not character:
            _character = random.choice(list(self.data[_series][_episode].keys()))
        else:
            _character = character.upper()
        while not len(sentences) and options and iter > 0:
            if not series:
                _series = random.choice(list(self.data.keys()))
            if not episode:
                _episode = random.choice(list(self.data[_series].keys()))
            if not character:
                _character = random.choice(list(self.data[_series][_episode].keys()))
            if _character in list(self.data[_series][_episode].keys()):
                if series and episode and character:
                    options = False
                sentences = self.data[_series][_episode][_character]
            iter -= 1
        if len(sentences):
            return _character + ": " + random.choice(sentences)
        return random.choice(Sentences.say_no) + "say anything"

    def get_sentence_from_character(self, character):
        if character in self.characters:
            return self.get_random_sentence(character=character)

    def get_sentence_from_series(self, serie):
        if serie in self.series:
            return self.get_random_sentence(series=serie)

    def get_series(self):
        return self.data.keys()

    def get_characters(self):
        return set(
            character.lower() for series in self.data.values() for episodes in series.values() for character in episodes.keys())
