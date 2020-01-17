from flask import Flask, render_template, request

# import bot file as module
import chatbot_star_trek as chatbot
from StarTrackHandler import StarTrackHandler
app = Flask(__name__)

startrackhandler = StarTrackHandler("data/all_series_lines.json")
print(startrackhandler.get_random_sentence())
chatbot = chatbot.Chatbot(startrackhandler)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    bot_answer = chatbot.answer(userText)
    return (str(bot_answer))

if __name__ == "__main__":
    app.run()
