from flask import Flask
from twilio.twiml.voice_response import Gather, VoiceResponse, Say
import requests, urllib

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def hello_monkey():
    resp = VoiceResponse()
    resp.say("HELLO MONKEY")
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)



