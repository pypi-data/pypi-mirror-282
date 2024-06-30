from abc import abstractmethod

from pydantic import BaseModel

from rooms_shared_services.src.lambda_handlers.abstract.handlers import AbstractNestedLambdaEventHandler
from rooms_shared_services.src.models.lmbda.abstract import AbstractLambdaEventModel


class AbstractDynamodbStreamLambdaEventHandler(AbstractNestedLambdaEventHandler):
    """Handle Dynamodb Stream events."""

    @abstractmethod
    def provide_lambda_event_model(self, event: dict) -> AbstractLambdaEventModel:
        """Validate dynamodb stream lambda event model.

        Args:
            event (dict): _description_

        Returns:
            AbstractLambdaEventModel: _description_
        """
        ...

    def run_processor(self, data_model: BaseModel, response: dict) -> dict | None:
        return self.event_data_processor(data_model, response)
