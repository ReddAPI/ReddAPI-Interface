import streamlit as st

from template import _input, clear_watermark, _error, success
from interfaces.cross_post import cross_post
from src import validators
from src import utils


def main():
    clear_watermark.main(page_title="bulk cross post")
    
    X_RapidAPI_Key = _error.check_api_key()

    "The data in the TXT file should be organized like the following:"
    "useragent::proxy::username::password::subreddit::title::text::post_url::is_nsfw"

    file_path = _input.input_template(label="the txt file path that contains the accounts info.")
    
    if not validators.are_all_true(elements=[file_path]):
        return
    
    if st.button("Submit"):
        if not X_RapidAPI_Key:
            "No API Found in 'conf.ini'"
            return
        
        lines = utils.read_file(file_path=file_path)

        bar = st.progress(0)

        for i, line in enumerate(lines):
            try:
                bar.progress((i + 1) / len(lines))
                
                if not line:
                    _error.line_not_structred(i=i)
                    continue

                (useragent, proxy, username, password, subreddit, 
                title, text, post_url, is_nsfw) = validators.process_line(line=line, n=9)
                
                res = utils.core(
                    cross_post,
                    useragent,
                    username,
                    password,
                    proxy,
                    useragent=useragent,
                    proxy=proxy,
                    subreddit=subreddit,
                    post_url=post_url,
                    title=title,
                    text=text,
                    is_nsfw=is_nsfw,
                    X_RapidAPI_Key=X_RapidAPI_Key
                )
                if res["reddit_status_code"] != 200:
                    _error.failed_to(action="crosspost", username=username, res=res)
                    continue

                success.success_to(action="cross posted", username=username)
            
            except Exception as e:
                _error.exception(e=e)   
                continue         
main()