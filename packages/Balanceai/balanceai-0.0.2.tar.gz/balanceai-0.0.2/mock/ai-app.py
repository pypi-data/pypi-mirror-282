from flask import Flask
from random_sleep import random_sleep

app = Flask(__name__)


@app.route("/ai", methods=['GET'])
def status():
    return {
        "status": "OK"
    }


@app.route("/ai/<model>", methods=['POST'])
def execute_model(model):
    random_sleep()

    return {
        "status": "OK",
        "model": f'RS for {model}',
        "data": 23
    }


if __name__ == "__main__":
    app.run(port=9300, debug=True)
