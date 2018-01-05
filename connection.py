from flask import Flask

app = Flask(__name__)
@app.route("/")
def main():
    return "Time to make phone calls!"

if __name__ == "__main__":
    app.run()
