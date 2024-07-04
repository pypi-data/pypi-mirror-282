import logging
from .ChainHttpClient import ChainHttpClient as ChainClient
from .UsageInfoDataGenerator import UsageInfoDataGenerator

logger = logging.getLogger(__name__)


class ChainService:
    config: {}
    chainClient: ChainClient

    def __init__(self, config=None):
        if config is None:
            logger.error('Missing configuration')
            exit()

        self.config = config
        self.chainClient = ChainClient(config)
        self.usage_info_data_generator = UsageInfoDataGenerator()

    def authorize(self, caller_address, model_id):
        return self.chainClient.authorize(caller_address, model_id)

    def update_model_usage_info(self, caller_address, model_id):
        chain_usage_rq = self.usage_info_data_generator.generateUsageInfo(model_id, caller_address)
        return self.chainClient.update_model_usage_info(chain_usage_rq)
