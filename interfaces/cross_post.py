import requests


def cross_post(X_RapidAPI_Key:str,
                    useragent:str, 
                    proxy:str, 
                    bearer:str, 
                    title:str,
                    text:str,
                    subreddit:str,
                    post_url:str,
                    is_nsfw:bool
                    ):

    url = "https://reddapi.p.rapidapi.com/api/cross_post"


    payload = {
        "useragent": str(useragent),
        "proxy": str(proxy),
        "bearer": str(bearer),
        "title": str(title),
        "text": str(text),            
        "sub_reddit": str(subreddit), 
        "post_url": str(post_url),
        "is_nsfw": str(is_nsfw)
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": str(X_RapidAPI_Key),
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }

    return requests.post(url, json=payload, headers=headers).json()