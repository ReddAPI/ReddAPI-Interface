import requests


def post_to_subreddit(X_RapidAPI_Key:str,
                    useragent:str, 
                    proxy:str, 
                    bearer:str, 
                    subreddit:str,
                    title:str,
                    text:str,
                    is_nsfw:bool
                    ):

    url = "https://reddapi.p.rapidapi.com/api/post_to_subreddit"

    payload = {
        "useragent": str(useragent),
        "proxy": str(proxy),
        "bearer": str(bearer),
        "title": str(title),       
        "text": str(text),           
        "sub_reddit": str(subreddit),
        "is_nsfw": bool(is_nsfw)
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": str(X_RapidAPI_Key),
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }

    return requests.post(url, json=payload, headers=headers).json()