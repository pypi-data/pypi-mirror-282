import logging
import requests

logger = logging.getLogger(__name__)


class IpfsHttpClient:
    config: {}

    def __init__(self, config=None):
        if config is None:
            logger.error('Missing configuration')
            exit()
        self.config = config

    def call(self, transaction_data):
        ipfs_url = self.config['ipfs']['url']['transaction']

        logger.info('[IPFS][transaction][RQ][%s]\n%s', ipfs_url, transaction_data)
        ipfs_response = requests.post(ipfs_url, json=transaction_data)
        ipfs_response_body = ipfs_response.json()
        logger.info('[IPFS][transaction][RS][%s]\n%s', ipfs_response.status_code, ipfs_response_body)
        return ipfs_response_body
