from __future__ import annotations

from typing import Optional

from pydantic import SecretStr

from .api_client import ApiClient
from .config import APIConfig
from .jobs.jobs import Jobs
from .genomics_models.models import Models
# from .hub.hub_response import HubResponse


class GenomicsClient:

    def __init__(
            self,
            api_key: Optional[str] = None,
            backend_url: Optional[str] = None,
            # rt_url: Optional[str] = None,
            config: Optional[APIConfig] = None,
    ) -> None:
        if config is None and (api_key is None or backend_url is None):
            raise ValueError("Either (api_key an backend_url) or config must be provided")
        if not ((api_key is not None and backend_url is not None) or config is not None):
            raise ValueError("Either api_key and backend_url must both have values or "
                             "config must have a value.")

        if config is not None:
            self.client = ApiClient(config)
        elif api_key and backend_url:

            self.client = ApiClient(
                APIConfig(
                    backend_url=backend_url,
                    # rt_url=rt_url,
                    access_token=SecretStr(api_key)
                )
            )

    @classmethod
    def from_config(cls, config: APIConfig) -> GenomicsClient:
        return cls(config=config)

    def jobs(self) -> Jobs:
        return Jobs(self.client)

    def models(self) -> Models:
        return Models(self.client)

    # def test_rt(self) -> HubResponse:
    #     result = self.client.test_rt()
    #     return result
