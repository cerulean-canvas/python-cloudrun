  
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Having fun? Please give us a rating at the end of the course!! 😊😊😊 "

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
