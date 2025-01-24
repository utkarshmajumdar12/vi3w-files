import os
import subprocess
import sys

def install_dependencies():
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)

def run_gradio_app():
    print("Running the Gradio web app...")
    try:
        subprocess.check_call([sys.executable, "gradio_app.py"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to run the Gradio app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()

    run_gradio_app()
