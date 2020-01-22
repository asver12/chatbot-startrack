from nltk import word_tokenize
import random

class SentenceHandler:
    def __init__(self, startrackhandler):
        """
        Recognizes the intent of sentences >.>
        """
        self.startrackhandler = startrackhandler

    def find_names(self, sentence):
        names = set([name.lower() for name in word_tokenize(sentence)]) & set(self.startrackhandler.characters)
        if len(names):
            return random.choice(list(names))
        return None
