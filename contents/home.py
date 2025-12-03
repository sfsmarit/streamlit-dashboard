import streamlit as st
import os
from pathlib import Path
import socket
import yaml
import toml
import pandas as pd


if os.name == "nt":
    root_dir = r"C:\Users\marit\Documents\python"
else:
    root_dir = "/home"

first_columns = ["app", "url", "port"]


# ---------------------------------------------------


def generate_email_from_name(name: str) -> str:
    address = ".".join(name.lower().split())
    return f"{address}@skyworksinc.com"


st.title("Streamlit Web Apps")
st.set_page_config(page_title="Streamlit Server", page_icon=":signal_strength:", layout="wide")


print("Searching info files ...", end="")
info_files = list(Path(root_dir).rglob("info.yaml"))
print("Done!")

try:
    hostname = socket.gethostname()
except:
    hostname = "localhost"


data = {}

for file in info_files:
    # YAMLファイルの読み込み
    with open(file, "r", encoding="utf-8") as f:
        info = yaml.safe_load(f)

    for k, v in info.items():
        # email を補完
        if k == "email" and not v:
            name = info.get("developer", "")
            v = generate_email_from_name(name)
        # data に追加
        data.setdefault(k, []).append(v)

    # .streamlit/config.toml の読み込み
    config_file = file.parent / ".streamlit/config.toml"
    if config_file.exists():
        config = toml.load(config_file)
        port = config.get("server", {}).get("port")
    else:
        port = "Unknown"
    data.setdefault("port", []).append(port)

    url = f"http://{hostname}:{port}"
    data.setdefault("url", []).append(url)


columns = first_columns + [col for col in data if col not in first_columns]
df = pd.DataFrame(data, columns=columns)
st.table(df)
