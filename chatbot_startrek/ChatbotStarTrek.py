from chatbot_startrek.SentenceHandler import SentenceHandler

class Chatbot:
    def __init__(self, startrackhandler, dialogstatehandler):
        """
        Whom who manages all the other shall take the highest price
        """
        self.startrackhandler = startrackhandler
        self.sentencehandler = SentenceHandler(startrackhandler)
        self.dialogstatehandler = dialogstatehandler


    def answer(self, user_input):
        character = self.sentencehandler.find_names(user_input)
        if character is None:
            return
        if character is not None:
            self.dialogstatehandler.set_chatpartner(character)
        return '{}'.format(self.startrackhandler.get_random_sentence(character=self.dialogstatehandler.get_chatpartner()))
