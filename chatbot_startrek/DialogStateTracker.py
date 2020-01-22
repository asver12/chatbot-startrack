class DialogStateTracker:
    def __init__(self, chatpartner=""):
        """
        Aka "Frame" remembers the state of a conversation
        """
        self.chatpartner = chatpartner

    def get_chatpartner(self):
        return self.chatpartner

    def set_chatpartner(self, chatpartner):
         self.chatpartner = chatpartner
