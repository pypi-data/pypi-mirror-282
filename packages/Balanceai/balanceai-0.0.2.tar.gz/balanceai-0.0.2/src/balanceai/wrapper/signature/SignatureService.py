import logging

logger = logging.getLogger(__name__)


class SignatureService:
    config: {}

    def __init__(self, config=None):
        if config is None:
            logger.error('Missing configuration')
            exit()
        self.config = config

    def verify(self, payload):
        pub_key = payload['caller_address']
        signature = payload['signature']
        message_without_signature = {}

        for (k, v) in payload.items():
            if k != 'signature':
                message_without_signature[k] = v

        logger.info('[SignatureService][verify][signature=%s][pub_key=%s]',
                    signature, pub_key)
        logger.info('[SignatureService][verify][message_without_signature]\n%s', message_without_signature)

        # based on data above verify signature
        valid = True

        logger.info('[SignatureService][verify][valid] %s', valid)

        return valid

    def sign(self, rs_body):
        signature = "balanceai.wrapper_signed_rs_sdjfgh837h"
        # sign by wrapper private key // sdk client will validate rs

        logger.info('[SignatureService][sign]\n%s', signature)

        return signature
