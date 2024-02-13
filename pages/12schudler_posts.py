import concurrent.futures
import streamlit as st

from template import _input, _error, clear_watermark
from interfaces.post_to_subreddit import post_to_subreddit
from src import utils, validators



def runner(line:str, X_RapidAPI_Key:str):
    useragent, proxy, username, password, subreddit, title, text, is_nsfw = validators.process_line(line=line, n=8)

    res = utils.core(
        post_to_subreddit,
        useragent,
        username,
        password,
        proxy,
        useragent=useragent,
        proxy=proxy,
        subreddit=subreddit,
        title=title,
        text=text,
        is_nsfw=is_nsfw,
        X_RapidAPI_Key=X_RapidAPI_Key
    )

    if res["reddit_status_code"] != 200:
        utils.save_data(file_path="post_schudler_logs.txt", data=f"{username} faild to DM with response code <{res}>\n")
        return
    
    utils.save_data(file_path="post_schudler_logs.txt", data=f"{username} made a DM successfully with response code <{res}>\n")


def run_multithreaded(lines:list, X_RapidAPI_Key:str):
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(lines)) as executor:
        futures = [executor.submit(runner, line, X_RapidAPI_Key) for line in lines]
        concurrent.futures.wait(futures)


def main():
    clear_watermark.main(page_title="schudler for bulk posting to subreddits")
    
    X_RapidAPI_Key = _error.check_api_key()

    st.header("make post for every:")
    col1, col2 = st.columns([2, 1])

    interval = col1.slider("-", 1, 60, 5, label_visibility="hidden")
    time_unit = col2.selectbox("-", ["Seconds", "Minutes", "Hours"], label_visibility="hidden")

    "The data in the TXT file should be organized like the following:"
    "useragent::proxy::username::password::subreddit::title::text::is_nsfw"
    file_path = _input.input_template(label="the txt file path that contains the accounts info.")
    
    if not validators.are_all_true(elements=[file_path]):
        return

    if st.button("run scheduler"):
        if not X_RapidAPI_Key:
            "No API Found in 'conf.ini'"
            return
         
        lines = utils.read_file(file_path=file_path)
        utils.run_scheduler(interval=interval, 
                        time_unit=time_unit,
                        callback=lambda: run_multithreaded(lines=lines, X_RapidAPI_Key=X_RapidAPI_Key)
                )

main()