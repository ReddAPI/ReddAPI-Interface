import streamlit as st

from template import _input, clear_watermark, _error
from interfaces.flairs_scraper import flair_scraper
from src import validators, utils


def main():
    clear_watermark.main(page_title="flair scraper")
    
    X_RapidAPI_Key = _error.check_api_key()

    subreddit = _input.input_template("the subreddit you wanna scrape flairs from")
    proxy = _input.input_template("the proxy to use")
    
    if not validators.are_all_true(elements=[subreddit, proxy]):
        return
    if st.button("Submit"):
        if not X_RapidAPI_Key:
            "No API Found in 'conf.ini'"
            return
        
        res = flair_scraper(
            X_RapidAPI_Key=X_RapidAPI_Key,
            subreddit=subreddit,
            proxy=proxy,
            cookies="reddit_session=84532100825132%252C2024-02-11T09%253A13%253A23%252C8514013377013f8d488072dd6c12fbc3e51c3e2b&loid=000000000typie9z58.2.1707641617104.Z0FBQUFBQmx5SS16OWVodGtiYUx5VFk5U3d3Q242N0h6TmlFa1l5VmtzMTIza09yUnVmVUhGSlFLS3JDMDlxYm9fT2ZxdXhtNVdrNnIxZERkeFROcGtWenRhaWU2VjRSUDB1QWNoRnZMLXRxdVBsVWRPclJid0tGX09qTUhjNHkzR2M0T0V4N0MwcWE"
        )

        file_path = f"{subreddit}_flairs.txt"
        utils.save_data(file_path=file_path, data=f"{res}\n")

        st.info(f"bot finished, check file '{file_path}'", icon="ℹ️")
main()