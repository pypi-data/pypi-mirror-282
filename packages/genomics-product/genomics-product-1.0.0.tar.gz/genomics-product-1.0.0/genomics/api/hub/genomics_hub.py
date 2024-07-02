from __future__ import annotations

import logging
import sys
import threading
import time
from typing import Optional
from requests import Session
from .sdk_auth_hub_connection import AuthHubConnection
from .hub_connection_builder import HubConnectionBuilder


# with Session() as session:
#create a connection
class GenomicsHub:
    hub_connection: AuthHubConnection

    def __init__(self, base_url: str, api_key: str) -> None:
        self.hub_connection = (HubConnectionBuilder()
                               .with_url(f"{base_url}", options={
            "headers": {"X-API-KEY": api_key}
        })
                               .with_automatic_reconnect({
            "type": "interval",
            "keep_alive_interval": 10,
            "intervals": [1, 3, 5, 6, 7, 87, 3]
        })
                               .configure_logging(logging.DEBUG)
                               .build()
                               )
        self.event = threading.Event()
        self.received_message = None

    def start(self, ):
        self.hub_connection.on("testRt", self.on_receive_message)
        self.hub_connection.start()
        handlers = self.hub_connection.handlers

    def on_receive_message(self, message):
        print("Received message:", message)
        self.received_message = message
        self.event.set()

    def stop(self, ):
        self.hub_connection.stop()
