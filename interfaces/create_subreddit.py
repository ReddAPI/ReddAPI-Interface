import requests

def create_subreddit(X_RapidAPI_Key:str,
                    useragent:str, 
                    proxy:str, 
                    bearer:str, 
                    subreddit:str
                    ):

    url = "https://reddapi.p.rapidapi.com/api/create_subreddit"

    payload = {
        "useragent": str(useragent),  
        "proxy": str(proxy),          
        "bearer": str(bearer),       
        "name": str(subreddit)
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": str(X_RapidAPI_Key),
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }

    return requests.post(url, json=payload, headers=headers).json()