import requests


def post_to_profile(useragent:str,
                    proxy:str,
                    bearer:str,
                    username:str,
                    title:str,
                    text:str,
                    is_nsfw:bool,
                    X_RapidAPI_Key:str
                    ):
    url = "https://reddapi.p.rapidapi.com/api/post_to_profile"

    payload = {
        "useragent": str(useragent),
        "proxy": str(proxy),
        "bearer": str(bearer),
        "username": str(username),
        "title": str(title),
        "text": str(text),
        "is_nsfw": bool(is_nsfw)
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": str(X_RapidAPI_Key),
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }

    return requests.post(url, json=payload, headers=headers).json()
