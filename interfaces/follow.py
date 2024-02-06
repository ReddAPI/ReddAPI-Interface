import requests


def follow(X_RapidAPI_Key:str,
            useragent:str, 
            proxy:str, 
            bearer:str, 
            username:str
                    ):
    
    url = "https://reddapi.p.rapidapi.com/api/follow"

    payload = {
        "useragent": str(useragent),
        "proxy": str(proxy),
        "bearer": str(bearer),
        "username": str(username)
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": str(X_RapidAPI_Key),
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }

    return requests.post(url, json=payload, headers=headers).json()