import logging
import requests

logger = logging.getLogger(__name__)


class AiHttpClient:
    config: {}

    def __init__(self, config=None):
        if config is None:
            logger.error('Missing configuration')
            exit()
        self.config = config

    def call(self, model_id, ai_model_request):
        ai_model_url = self.config['ai']['url']['model'] + model_id
        logger.info('[AI][model][RQ][%s]\n%s', ai_model_url, ai_model_request)
        ai_response = requests.post(ai_model_url, ai_model_request)
        ai_response_body = ai_response.json()
        logger.info('[AI][model][RS][%s]\n%s', ai_response.status_code, ai_response_body)
        return ai_response_body
