import json
import logging

from api.session import Session

logger = logging.getLogger("user_api." + __name__)


class UserApi(Session):
    # GET USER API
    GET_USERS = "/api"

    def __init__(self, host):
        super().__init__()
        self.host = host

    def get_users(self, gender: str = None, limit: int = None):
        """
        Get users list
        :param gender:  user sex
        :param limit: max value of elements return
        :return:
        """
        query = {"limit": limit, "gender": gender}

        return self._s.get(self.host + self.GET_USERS, params=query)
