import requests

def join_subreddit(X_RapidAPI_Key:str,
                    useragent:str,
                    proxy:str,
                    bearer:str,
                    subreddit:str):

    url = "https://reddapi.p.rapidapi.com/api/join_subreddit"

    payload = {
        "useragent": str(useragent),
        "proxy": str(proxy),
        "bearer": str(bearer),
        "sub_reddit": str(subreddit)
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": str(X_RapidAPI_Key),
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }

    return requests.post(url, json=payload, headers=headers).json()

