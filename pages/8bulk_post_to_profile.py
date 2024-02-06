import streamlit as st

from template import _input, clear_watermark, _error, success
from interfaces.post_to_profile import post_to_profile
from src import validators
from src import utils


def main():
    clear_watermark.main(page_title="bulk post to profile")
    
    X_RapidAPI_Key = _error.check_api_key()

    "The data in the TXT file should be organized like the following:"
    "useragent::proxy::username::password::title::text::is_nsfw"

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

                useragent, proxy, username, password, title, text, is_nsfw  = validators.process_line(line=line, n=7)
                res = utils.core(
                    post_to_profile,
                    useragent,
                    username,
                    password,
                    proxy,
                    useragent=useragent,
                    proxy=proxy,
                    username=username,
                    title=title,
                    text=text,
                    is_nsfw=is_nsfw,
                    X_RapidAPI_Key=X_RapidAPI_Key
                )
                if res["reddit_status_code"] != 200:
                    _error.failed_to(action="post to profile", username=username, res=res)
                    continue

                success.success_to(action="posted to profile", username=username)

            except Exception as e:
                _error.exception(e=e)
                continue

main()