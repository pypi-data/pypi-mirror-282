from typing import Any, Generic, TypeVar

from requests import Response
from pydantic.generics import GenericModel

T = TypeVar("T")


# class HubResponse(GenericModel, Generic[T]):
#     def __init__(self, api_response: Response, message_response: Any | None):
#         self.api_response = api_response
#         self.message_response = message_response
