import configparser
import schedule
import time 

from interfaces._login import login


def read_file(file_path:str) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().split("\n")
    
def save_data(file_path:str, data:str):
    with open(file_path, "a") as f:
        f.write(data)

def format_cookie(cookie:dict) -> str:
    domain = cookie['domain']
    secure = "TRUE" if cookie['secure'] else "FALSE"
    path = cookie['path']
    session = "TRUE" if cookie['session'] else "FALSE"
    expires = int(cookie['expires'])
    name = cookie['name']
    value = cookie['value']   
    return f"{domain}    {secure}    {path}    {session}    {expires}    {name}    {value}"
    
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
    if res.status_code != 200:
        raise ValueError(res.json()["detail"])

    return callback(
        bearer=res.json()["token_v2"],
        **kwargs
    )

def run_scheduler(interval:int, time_unit:str, callback):
    time_multiplier = {"Seconds": 1, "Minutes": 60, "Hours": 3600}

    schedule.every(interval * time_multiplier[time_unit]).seconds.do(callback)

    while True:
        schedule.run_pending()
        time.sleep(1)