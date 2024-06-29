import requests
from urllib.parse import quote

__all__ = ["api"]


class HorridAPI:

    def __init__(self) -> None:
        pass

    @staticmethod
    def llama(query: str):
        prompt = quote(query)
        api = f'https://horrid-api.onrender.com/llama?query={prompt}'
        res = requests.get(api).json()
        k = res['response']
        return k

    @staticmethod
    def dare():
        api = f'https://horrid-api.onrender.com/dare'
        res = requests.get(api).json()
        dare = res['dare']
        return dare

    @staticmethod
    def truth():
        api = f'https://horrid-api.onrender.com/truth'
        res = requests.get(api).json()
        k = res['truth']
        return k


api = HorridAPI()
