import requests
import urllib.parse


def flair_scraper(X_RapidAPI_Key:str,
                    subreddit:str, 
                    proxy:str, 
                    cookies:str
                    ):

    url = "https://reddapi.p.rapidapi.com/api/scrape_flairs"
    
    params = {
        "subreddit": str(subreddit),
        "proxy": str(proxy),
        "cookies": urllib.parse.urlencode(cookies),
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": str(X_RapidAPI_Key),
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }

    return requests.get(url, params=params, headers=headers).json()