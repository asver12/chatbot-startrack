import random
import os
from chatbot_startrek import json_reader


class StarTrackHandler:
    def __init__(self, path, file):
        """
        Dataset structure:
        Series -> episodes -> character
        """
        self.data = json_reader.read_json(os.path.join(path, file))
        self.series = self.get_series()
        self.characters = self.get_characters()

    def get_random_sentence(self):
        sentences = []
        while not len(sentences):
            movie = random.choice(list(self.data.keys()))
            episode = random.choice(list(self.data[movie].keys()))
            character = random.choice(list(self.data[movie][episode].keys()))
            sentences = self.data[movie][episode][character]
        return random.choice(sentences)

    def get_series(self):
        return self.data.keys()

    def get_characters(self):
        return set(character for series in self.data.values() for episodes in series.values() for character in episodes.keys())