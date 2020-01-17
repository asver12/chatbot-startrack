class Chatbot:
    def __init__(self, startrackhandler):
        self.startrackhandler = startrackhandler

    def answer(self, user_input):
        return('{}'.format(self.startrackhandler.get_random_sentence()))
