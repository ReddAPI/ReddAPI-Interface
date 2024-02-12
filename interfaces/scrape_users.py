import requests

def scrape_users_from_comments(X_RapidAPI_Key:str,
                                post_url:str, 
                                proxy:str, 
                                comments_num:int=20000
                                ):

    url = "https://reddapi.p.rapidapi.com/api/scrape_post_comments"
    
    params = {
        "proxy": str(proxy),
        "comments_num": comments_num,
        "post_url": str(post_url)
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": str(X_RapidAPI_Key),
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }

    return requests.get(url, params=params, headers=headers).json()