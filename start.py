import platform
import subprocess as sp
import os

system = platform.system()

def build_app():

    setup_script = os.path.join("scripts", "setup.")
    start_script = os.path.join("scripts", "start.")

    if system == "Linux" or system == "Darwin":
        setup_script += "sh"
        start_script += "sh"
        
        sp.run(f"chmod +x {setup_script}", shell=True)
        sp.run(f"chmod +x {start_script}", shell=True)
        sp.run(f"./{setup_script}", shell=True)

    elif system == "Windows":
        setup_script += "bat"
        sp.run(f"{setup_script}", shell=True)


def start_app():
    start_autoddit = "scripts\start.bat" if system == "Windows" else "./scripts/start.sh"
    sp.run(start_autoddit, shell=True)

def main():
    if os.path.exists("venv"):
        start_app()
    else:
        build_app()
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")