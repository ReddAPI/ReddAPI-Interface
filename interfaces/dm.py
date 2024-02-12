import requests


def dm(X_RapidAPI_Key:str,
        useragent:str, 
        proxy:str, 
        bearer:str, 
        dm_msg:str,
        user_id:str
        ):

    url = "https://reddapi.p.rapidapi.com/api/dm"

    payload = {
        "useragent": str(useragent),  
        "proxy": str(proxy),          
        "bearer": str(bearer),       
        "dm_msg": str(dm_msg),
        "user_id": str(user_id)
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": str(X_RapidAPI_Key),
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }

    return requests.post(url, json=payload, headers=headers).json()