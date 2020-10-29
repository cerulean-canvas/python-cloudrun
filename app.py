  
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Are you enjoying this Class? Don't forget to rate us!!😊😊😊 "

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
