import requests

def create_account(X_RapidAPI_Key:str,
                    proxy:str,
                    email_verified:bool=True
                    ):

    url = "https://reddapi.p.rapidapi.com/api/create_account"

    payload = {
        "proxy": str(proxy),          
        "email_verified": email_verified,
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": str(X_RapidAPI_Key),
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }

    return requests.post(url, json=payload, headers=headers).json()