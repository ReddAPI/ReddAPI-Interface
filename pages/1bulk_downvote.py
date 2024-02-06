import streamlit as st

from template import _input, clear_watermark, _error, success
from interfaces.Downvote import downvote
from src import validators
from src import utils


def main():
    clear_watermark.main(page_title="bulk downvote")
    
    X_RapidAPI_Key = _error.check_api_key()

    post_url  = _input.input_template(label="The post url you wanna send downvotes to.")
    "The data in the TXT file should be organized like the following:"
    "useragent:/proxy:/username:/password"
    
    file_path = _input.input_template(label="the txt file path that contains the accounts info.")

    if not validators.are_all_true(elements=[post_url, file_path]):
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

                useragent, proxy, username, password = validators.process_line(line=line, n=4)
                res = utils.core(
                    downvote,
                    useragent,
                    username,
                    password,
                    proxy,
                    useragent=useragent,
                    proxy=proxy,
                    post_url=post_url,
                    X_RapidAPI_Key=X_RapidAPI_Key
                )
                if res["reddit_status_code"] != 200:
                    _error.failed_to(action="downvote", username=username, res=res)
                    continue

                success.success_to(action="downvoted", username=username)

            except Exception as e:
                _error.exception(e=e)
                continue
main()