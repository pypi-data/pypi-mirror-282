import logging

logger = logging.getLogger(__name__)


class TransactionDataGenerator:

    def generateTransactionData(self, transparency, caller_address, model_id, ai_request, ai_response):
        logger.info('[TransactionDataGenerator][generateTransactionData][model_id=%s][transparency=%s][ai_request=%s][ai_response=%s]',
                    model_id, transparency, ai_request, ai_response)

        transaction_data = {
            "timestamp": 1707395374,
            "caller": caller_address,
            "model_id": model_id,
            "request": ai_request,
            "response": ai_response
        }

        logger.info('[TransactionDataGenerator][generateTransactionData][transaction_data]\n%s', transaction_data)

        return transaction_data
