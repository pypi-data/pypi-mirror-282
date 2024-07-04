import logging
from .IpfsHttpClient import IpfsHttpClient as IpfsClient
from .TransactionDataGenerator import TransactionDataGenerator

logger = logging.getLogger(__name__)


class IpfsService:
    config: {}

    def __init__(self, config=None):
        if config is None:
            logger.error('Missing configuration')
            exit()
        self.config = config
        self.transaction_data_generator = TransactionDataGenerator()
        self.ipfsClient = IpfsClient(config)

    def store_transaction(self,
                          transparency,
                          caller_address,
                          model_id,
                          ai_rq,
                          ai_rs):
        transaction_data = self.transaction_data_generator.generateTransactionData(transparency,
                                                                                   caller_address,
                                                                                   model_id,
                                                                                   ai_rq,
                                                                                   ai_rs)

        return self.ipfsClient.call(transaction_data)
