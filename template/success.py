import streamlit as st


def success_to(action:str, username:str):
    st.success(icon="✅", body=f"account with username: {username} {action} successfully")