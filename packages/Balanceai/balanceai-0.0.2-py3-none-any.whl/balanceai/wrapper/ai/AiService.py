import logging
from .AiHttpClient import AiHttpClient as AiClient

logger = logging.getLogger(__name__)


class AiService:
    config: {}
    aiClient: AiClient

    def __init__(self, config=None):
        if config is None:
            logger.error('Missing configuration')
            exit()
        self.config = config
        logger.info(config)
        self.aiClient = AiClient(config)

    def aiModel(self, model_id, ai_model_request):
        return self.aiClient.call(model_id, ai_model_request)
