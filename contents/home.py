import streamlit as st
import pandas as pd

import config
from utils import collect_app_info


first_columns = ["app", "url", "status"]
hidden_columns = ["visible"]


st.title("Streamlit Dashboard")

# データの取得
data = []
for dir in config.ROOT_DIRS:
    data += collect_app_info(dir)

# visible == True のみ抽出
data = [d for d in data if d.get("visible", True)]

columns = first_columns + [col for col in data[0] if col not in first_columns + hidden_columns]
df = pd.DataFrame(data, columns=columns)
df = df.sort_values(by="port")

st.table(df)
