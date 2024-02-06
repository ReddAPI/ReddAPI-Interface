import streamlit as st

def input_template(label:str, **kwargs):
    return st.text_input(label=label, **kwargs)
