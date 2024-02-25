import concurrent.futures
import streamlit as st

from template import _input, clear_watermark, _error
from interfaces.create_account import create_account
from src import validators
from src import utils


def runner(proxy:str, X_RapidAPI_Key:str):

    res = create_account(
        proxy=proxy,
        X_RapidAPI_Key=X_RapidAPI_Key
    )
    if not res["success"]:
        utils.save_data(file_path="ERRORS.txt", data=f'{res["message"]} | reddit response: {res["reddit_response"]} |  reddit status code: {res["reddit_status_code"]}\n')
        return 
    
    utils.save_data(file_path="accounts.txt", data=f'{res["email"]}::{res["username"]}::{res["password"]}\n')
        
    
def run_multithreaded(proxies:list, X_RapidAPI_Key:str):
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(runner, proxy, X_RapidAPI_Key) for proxy in proxies]
        concurrent.futures.wait(futures)

def main():
    clear_watermark.main(page_title="bulk account creation")
    
    X_RapidAPI_Key = _error.check_api_key()

    st.header("accounts creator:")

    "The data in the TXT file should be organized like the following:"
    "http://ip:port"
    "http://ip:port"
    "the bot will create as many accounts as the proxies number if you give 3 proxies the bot will create 3 accounts"
    file_path = _input.input_template(label="the txt file path that contains proxies.")
    if not validators.are_all_true(elements=[file_path]):
        return
    
    if st.button("start"):
        if not X_RapidAPI_Key:
            "No API Found in 'conf.ini'"
            return
        
        proxies = utils.read_file(file_path=file_path)
        run_multithreaded(proxies=proxies, X_RapidAPI_Key=X_RapidAPI_Key)
        st.success("completed, SEE file 'accounts.txt'", icon="✅")

main()