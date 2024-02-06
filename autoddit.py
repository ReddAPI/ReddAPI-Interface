import streamlit as st
import time

from template import _error, clear_watermark

def home_page():
    clear_watermark.main(page_title="Autoddit")

    st.header("autoddit home page")
    st.markdown("**you are using the free version**")

    bar = st.progress(0)

    for i in range(10):
        time.sleep(0.08)
        bar.progress((i + 1) / 10)

    if _error.check_api_key():
        st.success("No Issues found", icon="✅")

    st.info(icon="ℹ️", body="Join our **[Telegram group](https://t.me/autoddit_support)** for Quick support tips & tricks and more ...")

if __name__ == "__main__":
    home_page()