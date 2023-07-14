import aiohttp
from exceptions import ServerIsNotAvailable


class Response:
    def __init__(self, data: dict, status_code: int):
        self.data = data
        self.status_code = status_code
        self.is_ok = status_code < 400


class BaseAPIWorker:
    def __init__(self):
        self.url = "http://127.0.0.1:8000/api/v1/"

    async def post(self, endpoint: str, data: dict, token=None, **kwargs) -> Response:
        try:
            form_data = aiohttp.FormData()
            for key, value in data.items():
                form_data.add_field(key, value)

            headers = {
                "Authorization": f"Bearer {token}"
            }
            async with aiohttp.ClientSession() as session:
                async with session.post(self.url + endpoint, data=form_data, headers=headers, **kwargs) as response:
                    response = Response(data=await response.json(encoding="utf-8"), status_code=response.status)
                    return response
        except Exception as e:
            raise ServerIsNotAvailable

    async def get(self, endpoint: str, token: str) -> Response:
        try:
            headers = {
                "Authorization": f"Bearer {token}"
            }
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url + endpoint, headers=headers) as response:
                    response = Response(data=await response.json(encoding="utf-8"), status_code=response.status)
                    return response
        except Exception as e:
            raise ServerIsNotAvailable