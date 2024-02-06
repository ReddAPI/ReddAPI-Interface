@echo off

rem Activate the virtual environment
call venv\Scripts\activate && (
  streamlit run autoddit.py
)