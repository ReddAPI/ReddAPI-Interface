import configparser

from interfaces._login import login


def read_file(file_path:str) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().split("\n")
    
def save_data(file_path:str, data:str):
    with open(file_path, "a") as f:
        f.write(data)
    
def get_X_rapid_api_key() -> str:
    config = configparser.ConfigParser()
    config.read('conf.ini')
    api = config.get('API', 'X_rapid_api_key')
    return api if (api != "your_X_rapid_api_key" or not api) else ""

def core(callback, *args, **kwargs):
    """
    A core function that is responsible to deal with ReddAPI interfaces it returns the callback response
    """
    res = login(
        useragent=args[0],
        username=args[1],
        password=args[2],
        proxy=args[3],
        X_RapidAPI_Key=kwargs["X_RapidAPI_Key"]
    )
    return callback(
        bearer=res.json()["token_v2"],
        **kwargs
    )