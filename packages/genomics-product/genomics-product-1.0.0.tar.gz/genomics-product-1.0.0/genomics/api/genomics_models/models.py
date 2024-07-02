from genomics.api.api_client import ApiClient
from genomics.api.models import GetModelsResult, GetModelsRequest, PageInfo
from genomics.configs.logger_config import get_logger


class Models:

    def __init__(self, api_client: ApiClient):
        self._api_client = api_client

    def list(self):
        get_logger().info("getting genomics models...")
        payload = GetModelsRequest(
            keyword="",
            page_info=PageInfo(
                number=1,
                size=100,
            )
        )
        response = self._api_client.post("/model/models", payload.dict())
        result = GetModelsResult.parse_obj(response.json())

        if result.error_code:
            raise Exception(result.error_message)
        for model in result.result.data:
            get_logger().info(f"* {model.name}:\n==> {model.id}\n")
