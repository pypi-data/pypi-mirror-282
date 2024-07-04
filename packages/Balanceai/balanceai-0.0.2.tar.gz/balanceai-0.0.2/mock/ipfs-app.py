from flask import Flask
from flask import request
from random_sleep import random_sleep

app = Flask(__name__)


@app.route("/ipfs", methods=['GET'])
def status():
    return {
        "name": "ipfs",
        "status": "OK"
    }


@app.route("/ipfs/transaction", methods=['POST'])
def storeRequestResponse():
    random_sleep()

    payload = request.get_json()
    # app.logger.debug('A value for debugging')
    # app.logger.warning('A warning occurred (%d apples)', 42)
    # app.logger.error('An error occurred')
    return {
        "status": "OK",
        # "transactionId": 12313,
        # "payload": payload,
        "CID": "bafybeiemxf5abjwjbikoz4mc3a3dla6ual3jsgpdr4cjr3oz3evfyavhwq"
    }


if __name__ == "__main__":
    app.run(port=9100, debug=True)
