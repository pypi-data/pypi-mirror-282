import logging

logger = logging.getLogger(__name__)


class UsageInfoDataGenerator:

    def generateUsageInfo(self, model_id, caller_address):
        logger.info('[UsageInfoGenerator][generateUsageInfo][model_id=%s][caller_address=%s]', model_id, caller_address)

        # what put here?

        # usage = {
        #     "model_id": model_id,
        #     "caller_address": caller_address
        # }
        usage = {
            "model_id": model_id,
            "usage_info": {
                "units": 1234
            }
        }

        logger.info('[UsageInfoGenerator][generateUsageInfo][usage]\n%s', usage)

        return usage
