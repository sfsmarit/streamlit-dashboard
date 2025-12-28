import streamlit as st
import pandas as pd

from common.utils import collect_app_info


first_columns = ["app", "url", "status"]
hidden_columns = ["test", "visible"]


st.title("Streamlit Dashboard")

check_status = st.button("Check Status")

# データの取得
with st.spinner("Loading data..."):
    data = collect_app_info(check_status)

# visible == True のみ抽出
data = [d for d in data if d.get("visible", True)]

unique_keys = []
for d in data:
    for k in d:
        if k not in unique_keys:
            unique_keys.append(k)

columns = first_columns + [col for col in unique_keys if col not in first_columns]
df = pd.DataFrame(data, columns=columns)
df = df.sort_values(by="port")

column_config = {
    "url": st.column_config.LinkColumn(label="url", display_text=":material/open_in_new:")
}

df1 = df[df["test"] == False].drop(columns=hidden_columns)
st.subheader("Released")
st.data_editor(df1, width="stretch", column_config=column_config)

df2 = df[df["test"] == True].drop(columns=hidden_columns)
if len(df2):
    st.markdown("---")
    st.subheader("Test")
    st.data_editor(df2, width="stretch", column_config=column_config)
