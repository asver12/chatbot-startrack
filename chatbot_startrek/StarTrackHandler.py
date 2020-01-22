import random
import os
from chatbot_startrek import json_reader, Sentences


class StarTrackHandler:
    def __init__(self, path, file):
        """
        Dataset structure:
        Series -> episodes -> character
        """
        self.data = json_reader.read_json(os.path.join(path, file))
        self.series = self.get_series()
        self.characters = self.get_characters()

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
