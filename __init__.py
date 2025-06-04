from .ui import init_addon
import os

os.environ["PATH"] += ":/usr/local/bin"
os.environ["KRDICT_API_KEY"] = ""

init_addon()
