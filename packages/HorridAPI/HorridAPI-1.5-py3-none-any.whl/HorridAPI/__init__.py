import requests
from urllib.parse import quote

__version__ = "1.5"

__all__ = ["api"]


class HorridAPI:

    def __init__(self)->None:
        pass

    def joke():
        api = f'https://horrid-api.onrender.com/joke'
        res = requests.get(api).json()
        joke = res['joke']
        return joke
        
    def dare():
        api = f'https://horrid-api.onrender.com/dare'
        res = requests.get(api).json()
        dare = res['dare']
        return dare
  
    def truth():
        api = f'https://horrid-api.onrender.com/truth'
        res = requests.get(api).json()
        k = res['truth']
        return k

    def gpt(query: str):
        prompt = quote(query)
        api = f'https://horrid-api.onrender.com/gpt?query={prompt}'
        res = requests.get(api).json()
        k = res['response']
        return k    


api=HorridAPI()
