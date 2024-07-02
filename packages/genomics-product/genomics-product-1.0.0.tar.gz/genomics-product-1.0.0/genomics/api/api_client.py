from __future__ import annotations

from typing import Any

import jsonpickle
import requests
from requests import Response, Session

# from .hub.hub_response import HubResponse
from .config import APIConfig


class ApiClient:
    def __init__(self, config: APIConfig) -> None:

        self.base_url = config.backend_url
        self.session: Session = requests.session()
        self.session.headers["Content-Type"] = "python-sdk/json"
        self.session.headers["Accept"] = "python-sdk/json"
        self.session.headers["X-SDK-Client"] = "sdk"
        self.form_data_session: Session = requests.session()
        self.form_data_session.headers["X-SDK-Client"] = "sdk"
        if config.access_token is not None:
            self.session.headers["X-API-KEY"] = config.access_token.get_secret_value()
            self.form_data_session.headers["X-API-KEY"] = (
                config.access_token.get_secret_value())
        # self.hub_connection = GenomicsHub(base_url=config.rt_url, api_key=config.access_token.get_secret_value())
        # self.hub_connection.start()

    def delete(self, endpoint: str) -> Response:
        response = self.session.delete(self.base_url + endpoint)
        response.raise_for_status()
        return response

    def get(self, endpoint: str, params: Any = None) -> Response:
        response = self.session.get(self.base_url + endpoint, params=params)
        response.raise_for_status()
        return response

    def post(self, endpoint: str, data: Any) -> Response:
        response = self.session.post(self.base_url + endpoint,
                                     data=jsonpickle.encode(data))
        response.raise_for_status()
        return response

    def patch(
            self,
            endpoint: str,
            data: Any = None,
            files: Any = None,
    ) -> Response:
        response = self.form_data_session.patch(
            self.base_url + endpoint,
            data=data,
            files=files
        )
        response.raise_for_status()

        return response

    def put(self, endpoint: str, data: Any) -> Response:
        response = self.session.put(self.base_url + endpoint, None, json=data)
        response.raise_for_status()
        return response

    # def test_rt(self) -> HubResponse:
    #     response = self.form_data_session.get(
    #         self.base_url + 'apikey/test-rt'
    #     )
    #     response.raise_for_status()
    #     self.hub_connection.event.wait()
    #     return HubResponse(api_response=response, message_response=self.hub_connection.received_message)
