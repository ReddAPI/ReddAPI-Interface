import streamlit as st
import random

from template import _input, clear_watermark, _error, success
from interfaces.dm import dm
from src import validators
from src import utils


def main():
    clear_watermark.main(page_title="DM")
    
    X_RapidAPI_Key = _error.check_api_key()

    users_list  = _input.input_template(label="The txt file that contains user list you wanna DM.")

    file_path = _input.input_template(label="the accounts data **it should be like this useragent::username::password::proxy**")
    spin_taks = _input.input_template(label="The spintaks for the DM **should be like this 'message1|message2|and so on...'**.")

    if not validators.are_all_true(elements=[users_list, file_path, spin_taks]):
        return
    
    if st.button("Submit"):
        if not X_RapidAPI_Key:
            "No API Found in 'conf.ini'"
            return
        
        user_ids = utils.read_file(file_path=users_list)
        accounts = utils.read_file(file_path=file_path)

        bar = st.progress(0)

        for i, user_id in enumerate(user_ids):
            try:
                bar.progress((i + 1) / len(user_ids))

                useragent, username, password, proxy = random.choice(accounts).split("::")
                dm_msg = random.choice(spin_taks.split("|"))
                res = utils.core(
                    dm,
                    useragent,
                    username,
                    password,
                    proxy,
                    useragent=useragent,
                    proxy=proxy,
                    dm_msg=dm_msg,
                    user_id=user_id,
                    X_RapidAPI_Key=X_RapidAPI_Key
                )
                if res["reddit_status_code"] == 200:
                    success.success_to(action="DMed", username=username)
            
            except Exception as e:
                st.error(body=e, icon="🚨")

main()