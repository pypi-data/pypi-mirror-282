from flask import Flask
from flask import request
from random_sleep import random_sleep

app = Flask(__name__)


@app.route("/chain", methods=['GET'])
def status():
    return {
        "name": "chain",
        "status": "OK"
    }


@app.route("/chain/authorize", methods=['POST'])
def authorize():
    random_sleep()

    # payload = request.get_json()
    # app.logger.info('[POST][authorize]\n%s', payload)
    # app.logger.info('caller_address: %s', payload['caller_address'])
    # app.logger.info('model_address: %s', payload['model_address'])
    return {
        "authorized": "true"
    }


@app.route("/chain/updateModelUsageInfo", methods=['POST'])
def storeRequestResponse():
    random_sleep()

    payload = request.get_json()
    # app.logger.info('[POST][updateModelUsageInfo]\n%s', payload)
    # app.logger.info('model_address: %s', payload['model_address'])
    # app.logger.info('usage_info: %s', payload['usage_info']["units"])
    return {
        "status": "OK",
        "transactionId": 98765
    }


if __name__ == "__main__":
    app.run(port=9200, debug=True)
