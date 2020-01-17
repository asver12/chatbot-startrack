import random
import json_reader

class StarTrackHandler:
    def __init__(self, file):
        self.data = json_reader.read_json(file)

    def get_random_sentence(self):
        movie = random.choice(list(self.data.keys()))
        episode = random.choice(list(self.data[movie].keys()))
        character = random.choice(list(self.data[movie][episode].keys()))
        # self.data['DS9']['episode 0']['SISKO']
        # print(self.data[movie][episode])
        return random.choice(list(self.data[movie][episode].values()))
