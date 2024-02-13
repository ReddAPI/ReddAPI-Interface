import streamlit as st

from interfaces.scrape_users import scrape_users_from_comments
from template import _input, clear_watermark, _error
from src import validators
from src import utils


def main():
    clear_watermark.main(page_title="scrape users")
    
    X_RapidAPI_Key = _error.check_api_key()

    post_url  = _input.input_template(label="The post url you wanna scrape users from.")
    proxy  = _input.input_template(label="The proxy url **it should start with 'http://'or 'https://'**.")

    file_path = _input.input_template(label="the txt file to save the scraped users.")
    
    if not validators.are_all_true(elements=[post_url, file_path]):
        return
    
    if st.button("Submit"):
        if not X_RapidAPI_Key:
            "No API Found in 'conf.ini'"
            return
        
        bar = st.progress(0)
        comments = scrape_users_from_comments(
            X_RapidAPI_Key=X_RapidAPI_Key,
            post_url=post_url,
            proxy=proxy
        )

        user_ids = []

        for i, comment in enumerate(comments):
            user_ids.append(comment["user_id"])
            bar.progress((i + 1) / len(comments))

        utils.save_data(file_path=file_path,data="\n".join(user_ids))

main()