import requests


def login(username:str, password:str, useragent:str, proxy:str, X_RapidAPI_Key:str):
    url = "https://reddapi.p.rapidapi.com/api/login"
    payload = {
        "username": str(username),   
        "password": str(password),   
        "useragent": str(useragent), 
        "proxy": str(proxy)          
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": str(X_RapidAPI_Key),
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }

    return requests.post(url, json=payload, headers=headers)