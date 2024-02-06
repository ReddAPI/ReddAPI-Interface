import streamlit as st


def main(page_title:str):

    st.set_page_config(page_title=page_title)
    st.markdown(
        """
        <style>
        #MainMenu {
            visibility: hidden;
        }
        footer {
            visibility: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True
    )