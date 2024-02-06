import streamlit as st

from src import utils


def lines_error(allowed_lines:int=2):
    st.error(body=f"you are not allowed to run more than {allowed_lines} accounts each time, \
                   please consider upgrading to the premium plan for more flexibility",
             icon="🚨")
    return

def check_api_key():
    if api := utils.get_X_rapid_api_key():
        return api
    else:
        st.error(icon="🚨", body="you still haven't added your API key to conf.ini, \
                 Please consider getting one at 'https://rapidapi.com/SeasonedCode/api/reddapi'")


def line_not_structred(i):
    st.warning(icon="⚠️", 
               body=f"the line number {i+1} isn't structured properly, moving to the next line...")
    
def failed_to(action:str, username:str, res):
    st.error(icon="🚨", body=f"account with username: {username} failed to {action} with response {res}")

def exception(e:Exception):
    st.error(icon="🚨", body=e)