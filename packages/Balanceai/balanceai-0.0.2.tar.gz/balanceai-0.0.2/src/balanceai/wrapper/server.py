from flask import Flask
from flask import request
import logging

# if __name__ == '__main__':
#     print("[server][import] __main__")
#     from ai.AiService import AiService as Ai
#     from chain.ChainService import ChainService as Chain
#     from ipfs.IpfsService import IpfsService as Ipfs
#
#     from config.configuration import read_json
#     from signature.SignatureService import SignatureService as Signature
# else:
#     print("[server][import] modules")
from balanceai.wrapper.ai.AiService import AiService as Ai
from balanceai.wrapper.chain.ChainService import ChainService as Chain
from balanceai.wrapper.ipfs.IpfsService import IpfsService as Ipfs

from balanceai.config.configuration import read_json
from balanceai.wrapper.signature.SignatureService import SignatureService as Signature

app = Flask(__name__)
LOG_FORMAT = '%(levelname) -7s %(asctime)s %(name) -30s: %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)

# config = read_json("bai-config.json")
# if config is None:
#     config = read_json("../bai-config.json")
#
ai = None
chain = None
ipfs = None
signature = None


# ai, chain, ipfs, signature
# chain = Chain(config)
# ipfs = Ipfs(config)
# signature = Signature(config)


@app.route("/baiwrapper", methods=['GET'])
def status():
    return {
        "name": "bai-wrapper",
        "status": "OK"
    }


@app.route("/baiwrapper/aimodel", methods=['POST'])
def storeRequestResponse():
    payload = request.get_json()

    app.logger.info('[BAI-WRAPPER][aimodel][RQ]\n%s', payload)

    model_id = payload["model_id"]
    caller_address = payload['caller_address']
    rq_id = payload['id']

    app.logger.info('[BAI-WRAPPER][aimodel][model_id=%s][caller_address=%s]', model_id, caller_address)

    valid_signature = signature.verify(payload)
    # if NOT - return unauthorized error
    # close SSE conn

    chain_rs = chain.authorize(caller_address, model_id)
    # if NOT - return unauthorized error
    # close SSE conn

    ai_rq = payload['request']
    ai_rs = ai.aiModel(model_id, ai_rq)
    # return AI response
    # if error -> return error & close SSE conn

    rs_body = {
        "model_id": model_id,
        "id": rq_id,
        "model_response": ai_rs
    }
    rs_signature = signature.sign(rs_body)
    rs_body['signature'] = rs_signature
    app.logger.info('[BAI-WRAPPER][aimodel][RS]\n%s', rs_body)

    chain_usage_rs = chain.update_model_usage_info(caller_address, model_id)
    # send SSE event with confirmation

    # if false & false - do NOT call ipfs
    transparency = payload['transparency']
    ipfs_rs = ipfs.store_transaction(transparency, caller_address, model_id, ai_rq, ai_rs)
    # return CID
    # close SSE - all done

    return rs_body


def setup(config):
    global ai, chain, ipfs, signature

    ai = Ai(config)
    chain = Chain(config)
    ipfs = Ipfs(config)
    signature = Signature(config)


def run(mode, configFile):
    app.logger.info(f"Configuration file: [{configFile}]")

    config = read_json(configFile)['wrapper']
    # if config is None:
    #     app.logger.info(f"Configuration file: [{config}]")

    setup(config)

    enable_debug = False
    if mode == 'prod':
        app.logger.info("[PROD] RUNNING IN PRODUCTION MODE")
    else:
        app.logger.info("[DEV] RUNNING IN DEV MODE")
        if config['bai']['debug'] is not None:
            enable_debug = config['bai']['debug']

    app.run(port=config['bai']['port'], debug=enable_debug)


if __name__ == "__main__":
    run()
    # LOG_FORMAT = ('%(levelname) -7s %(asctime)s %(name) -30s %(funcName) '
    #               '-6s %(lineno) -5d: %(message)s')
    # LOG_FORMAT = '%(levelname) -7s %(asctime)s %(name) -30s: %(message)s'
    # logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
    #
    # config = read_json("bai-config.json")
    # ai = Ai(config)
    # chain = Chain(config)
    # ipfs = Ipfs(config)
    # signature = Signature(config)
    #
    # app.run(port=9000, debug=True)
