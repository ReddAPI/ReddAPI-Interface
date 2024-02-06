@echo off

rem Create Python virtual environment
python -m venv venv

rem Activate the virtual environment and run subsequent commands within the same process
call venv\Scripts\activate && (

  rem Install Python requirements
  pip install -r requirements.txt

  rem Start the Streamlit app
  streamlit run autoddit.py
)