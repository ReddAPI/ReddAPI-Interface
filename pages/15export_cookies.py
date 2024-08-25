import streamlit as st
import os

from template import _input, clear_watermark, _error
from interfaces._login import login
from src import validators
from src import utils

def main():
    clear_watermark.main(page_title="bulk Cookies exporting")
    
    X_RapidAPI_Key = _error.check_api_key()
    st.header("cookies exporter:")

    "The data in the TXT file should be organized like the following:"
    "username::password::proxy"

    file_path = _input.input_template(label="the txt file path that contains accounts.")
    output_folder_path = _input.input_template(label="the folder path that you want to save exported cookies in it.")
    
    if not validators.are_all_true(elements=[file_path, output_folder_path]):
        return
    
    if st.button("start"):
        if not X_RapidAPI_Key:
            "No API Found in 'conf.ini'"
            return
        
        try:
            accs = utils.read_file(file_path=file_path)
        except FileNotFoundError:
            _error.exception(f"File not found: {file_path}")
            return
        except Exception as e:
            _error.exception(f"An error occurred while reading the file: {e}")
            return
        
        failed_accounts = []
        successful_accounts = []

        for acc in accs:
            with st.spinner(f"Processing account: **{acc[:20]}**..."):
                try:
                    username, password, proxy = acc.split("::")
                except ValueError:
                    _error.exception(f"Invalid account format in line: {acc}")
                    failed_accounts.append(acc)
                    continue
                
                response = login(
                    username=username,
                    password=password,
                    useragent="",
                    proxy=proxy,
                    X_RapidAPI_Key=X_RapidAPI_Key
                )
                
                if response.status_code != 200:
                    _error.failed_to("export cookies", username=username, res=response.text)
                    failed_accounts.append(acc)
                    continue
                
                try:
                    cookies_output = [
                        utils.format_cookie(cookie=cookie)
                    for cookie in response.json()["cookies"]
                    ]
                    
                    output_file_path = os.path.join(output_folder_path, f"{username}.txt")
                    utils.save_data(output_file_path, data="\n".join(cookies_output))
                    successful_accounts.append(username)
                    st.info(f"Cookies exported successfully for user: {username}")
                except Exception as e:
                    failed_accounts.append(acc)
                    _error.exception(f"An error occurred while processing cookies for {username}: {e}")
                    continue
        
        if successful_accounts:
            st.success(f"Successfully exported cookies for {len(successful_accounts)} account(s).")
        if failed_accounts:
            st.error(f"Failed to export cookies for {len(failed_accounts)} account(s):")
            st.text("\n".join(failed_accounts))


main()