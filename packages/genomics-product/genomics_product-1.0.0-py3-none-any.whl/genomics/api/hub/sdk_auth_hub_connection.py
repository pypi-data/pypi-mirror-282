from signalrcore.hub.base_hub_connection import BaseHubConnection
from signalrcore.helpers import Helpers

class AuthHubConnection(BaseHubConnection):
    def __init__(self, headers=None, **kwargs):
        if headers is None:
            self.headers = dict()
        else:
            self.headers = headers
        super(AuthHubConnection, self).__init__(headers=headers, **kwargs)

    def start(self):
        try:
            Helpers.get_logger().debug("Starting connection ...")
            return super(AuthHubConnection, self).start()
        except Exception as ex:
            Helpers.get_logger().warning(self.__class__.__name__)
            Helpers.get_logger().warning(str(ex))
            raise ex