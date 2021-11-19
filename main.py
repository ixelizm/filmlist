from flask import Flask, request, jsonify
import json
app = Flask(__name__)


app.config["JSON_AS_ASCII"] = False
# A welcome message to test our server
@app.route('/')
def index():
    with open("Filmler.json", "r", encoding="UTF-8") as veriler:
        filmler = json.load(veriler)
    return jsonify({"result":filmler})

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
