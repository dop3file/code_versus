from dataclasses import dataclass
import json
from collections import namedtuple
from typing import Optional

from api import BaseAPIWorker
from exceptions import Unauthorized
from config import JSON_FILE_PATH


@dataclass
class User:
    username: str
    email: str
    first_name: str
    last_name: str
    rating: int
    count_submit_task: int


class AuthData:
    data = namedtuple("data", ["access", "refresh"])
    @staticmethod
    def load():
        try:
            with open(JSON_FILE_PATH) as file:
                data = json.load(file)
            return AuthData.data(**data)
        except Exception:
            return None

    @staticmethod
    def save(data: dict):
        with open(JSON_FILE_PATH, "w") as file:
            json.dump(data, file)

    @staticmethod
    def delete():
        with open(JSON_FILE_PATH, "w") as file:
            json.dump({"access": None, "refresh": None}, file)


class JWTAuth:
    def __init__(self):
        self.api = BaseAPIWorker()
        self._access_token = None
        self._refresh_token = None
        self.user = None

    async def get_user(self, token: Optional[str] = False):
        token = token or self._access_token
        return await self.api.get("curr_user/", token=token)

    def quit(self):
        self._access_token = None
        self._refresh_token = None
        self.user = None
        AuthData.delete()

    async def prefetch_auth(self):
        data = AuthData.load()

        if data is not None and data.access != None and  await self.get_user(data.access):
            self._access_token = data.access
            self._refresh_token = data.refresh
            self.user = User(**((await self.get_user(self._access_token)).data))
            return True
        else:
            return False

    async def register(self, data: dict):
        response = await self.api.post("register/", data=data)
        return response

    async def login(self, data: dict):
        response = await self.api.post("token/", data=data)
        if not response.is_ok:
            raise Unauthorized
        self._access_token = response.data["access"]
        self._refresh_token = response.data["refresh"]
        self.user = User(**((await self.get_user(self._access_token)).data))
        AuthData.save(response.data)
