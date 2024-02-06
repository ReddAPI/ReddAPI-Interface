import requests

def comment(X_RapidAPI_Key:str,
            useragent:str, 
            proxy:str, 
            bearer:str, 
            text:str, 
            post_url:str):

    url = "https://reddapi.p.rapidapi.com/api/comment"
    payload = {
        "useragent": str(useragent),
        "proxy": str(proxy),
        "bearer": str(bearer),
        "text": str(text),
        "post_url": str(post_url)
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": str(X_RapidAPI_Key),
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }

    return requests.post(url, json=payload, headers=headers).json()