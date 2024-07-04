import logging
import requests

logger = logging.getLogger(__name__)


class ChainHttpClient:
    config: {}

    def __init__(self, config=None):
        if config is None:
            logger.error('Missing configuration')
            exit()
        self.config = config

    def authorize(self, caller_address, model_id):
        chain_auth_url = self.config['chain']['url']['auth']
        chain_auth_request = {
            "caller_address": caller_address,
            "model_address": model_id,

        }
        logger.info('[CHAIN][authorize][RQ][%s]\n%s', chain_auth_url, chain_auth_request)
        chain_response = requests.post(chain_auth_url, json=chain_auth_request)
        chain_response_body = chain_response.json()
        logger.info('[CHAIN][authorize][RS][%s]\n%s', chain_response.status_code, chain_response_body)
        return chain_response_body

    def update_model_usage_info(self, chain_usage_rq):
        chain_url = self.config['chain']['url']['update_usage']

        logger.info('[CHAIN][update_model_usage_info][RQ][%s]\n%s', chain_url, chain_usage_rq)
        chain_response = requests.post(chain_url, json=chain_usage_rq)
        chain_response_body = chain_response.json()
        logger.info('[CHAIN][update_model_usage_info][RS][%s]\n%s', chain_response.status_code, chain_response_body)
        return chain_response_body
