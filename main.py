from app_init import *
from src.routes import *
from src.functions import *
import webbrowser
import threading
import os


file_to_open = r"" # give your docx, txt, or pdf's file path
if not os.path.exists(file_to_open):
    print("Please provide a valid file path to your project!")
    exit()

path = os.path.abspath(file_to_open)


def open_browser():
    webbrowser.open_new(f"http://localhost/cards?path={path}")


if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        threading.Timer(1, open_browser).start()
    app.run(port=80)