import streamlit as st
import os
from pathlib import Path
import pandas as pd

from utils import collect_app_info


first_columns = ["app", "url", "status"]
hidden_columns = ["visible"]


if os.name == "nt":
    root_dirs = [r"C:\Users\marit\Documents\python"]
else:
    root_dirs = []
    for user_path in Path("/home").iterdir():
        if any(s in str(user_path) for s in ["admin", "sysmgr"]):
            continue
        root_dirs.append(str(user_path / "streamlit"))


st.title("Streamlit Web Apps")
st.set_page_config(page_title="Streamlit Server", page_icon=":signal_strength:", layout="wide")

# データの取得
data = []
for dir in root_dirs:
    data += collect_app_info(dir)

# visible == True のみ抽出
data = [d for d in data if d.get("visible", True)]

columns = first_columns + [col for col in data[0] if col not in first_columns + hidden_columns]
df = pd.DataFrame(data, columns=columns)
df = df.sort_values(by="port")

st.table(df)
