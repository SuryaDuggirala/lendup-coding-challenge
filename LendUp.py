from flask import Flask
from twilio.twiml.voice_response import Gather, VoiceResponse, Say
import requests, urllib

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def hello_monkey():
    resp = VoiceResponse()
    res = resp.say("HELLO MONKEY")
    return str(res)

if __name__ == "__main__":
    app.run()



