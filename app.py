from flask import Flask, render_template, request

# import bot file as module
from chatbot_startrek import ChatbotStarTrek as chatbot
from chatbot_startrek.StarTrackHandler import StarTrackHandler
from chatbot_startrek.DialogStateTracker import DialogStateTracker

app = Flask(__name__)

startrackhandler = StarTrackHandler("data", "all_series_lines.json")
print(startrackhandler.get_random_sentence())
dialogstatehandler = DialogStateTracker()
chatbot = chatbot.Chatbot(startrackhandler, dialogstatehandler)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    bot_answer = chatbot.answer(user_text)
    return str(bot_answer)


if __name__ == "__main__":
    app.run()
