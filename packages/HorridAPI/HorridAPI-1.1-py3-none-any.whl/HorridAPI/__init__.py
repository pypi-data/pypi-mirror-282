import requests
from urllib.parse import quote

__version__ = "1.1"


class HorridAPI:

    def __init__(self) -> None:
        pass

    @staticmethod
    def joke():
        api = f'https://horrid-api.onrender.com/joke'
        res = requests.get(api).json()
        joke = res['joke']
        return joke
        
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

    @staticmethod
    def gpt(query: str):
        prompt = quote(query)
        api = f'https://horrid-api.onrender.com/gpt?query={prompt}'
        res = requests.get(api).json()
        k = res['response']
        return k    


api = HorridAPI()
