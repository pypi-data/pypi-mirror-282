from balanceai.config.configuration import read_json
import requests
import sys
import logging

logger = logging.getLogger(__name__)
class HuggingFace:
    config: {}

    def __init__(self, config=None):
        if config is None:
            logger.error('Missing configuration')
            exit()

        API_TOKEN = config['api_token']
        self.headers = {"Authorization": f"Bearer {API_TOKEN}"}

        MODEL_ID = config['model_id']
        self.API_URL = "https://api-inference.huggingface.co/models/" + MODEL_ID

        self.config = config
        logger.info(f"Setting up HuggingFace model: {config['model_id']}")


    def query(self, payload):
        logger.info(f"Calling HuggingFace model: {self.config['model_id']}")
        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        return response.json()

