  
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello, There! Welcome to this class!! 😊😊😊 "

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
