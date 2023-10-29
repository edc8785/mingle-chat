from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/')
def home():
    return 'mingle-chat'


## flask hosting
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

