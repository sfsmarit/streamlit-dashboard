
import streamlit as st
import socket

import components

nl = "  "
HOST = socket.gethostname()

st.title("Streamlit Development Guide")
st.set_page_config(page_title="Streamlit Server", page_icon=":signal_strength:", layout="centered")

components.render_resouce_usage()
components.render_available_ports()

st.markdown("---")

st.subheader("1. Obtain a Streamlit Server Account", divider=True)
st.markdown(
    f"""
    IT Service Desk{nl}
    https://skyworksinc.atlassian.net/servicedesk/customer/portal/9/group/37/create/229 {nl}
    [Summary]
    Request login access to {HOST}
       
    If you need to use a database, please submit a separate ticket for DB access permissions.
    """
)

st.subheader("2. App Development & Deployment", divider=True)
st.markdown(
    f"""
    Detailed instructions are available on this page:{nl}
    https://app-startguide.streamlit.app/
    
    When deploying, create a `streamlit` directory in your home directory and place your app inside it.
    ```bash
    cd
    mkdir streamlit
    cd streamlit
    git clone https://github.com/<UserName>/sample-app.git
    ```
    """
)

st.subheader("3. Fixing the Port", divider=True)
st.markdown(
    f"""
    ```bash
    # Navigate to the project directory
    cd ~/streamlit/sample-app/
    
    # Create .streamlit/config.toml
    mkdir .streamlit
    touch .streamlit/config.toml
    ```    
    Edit config.toml to specify the port:
    ```toml
    [server]
    port=8650
    ```    
    For available ports, refer to [Available Ports] at the top of the page.
    """
)

st.subheader("4. Place info.yaml", divider=True)
st.markdown(
    f"""
    Ensure your app information is displayed in the Streamlit Server app list.
    ```bash
    # Navigate to the project directory
    cd ~/streamlit/sample-app/

    # Copy info.yaml
    cp /home/marit/template/info.yaml ./
    ```    
    Edit info.yaml:
    ```yaml
    app: "AppName"
    description: ""
    intended_users: ""
    developer: "YourName"
    email: ""
    visible: true
    ```    
    """
)

st.subheader("5. Start the App", divider=True)
st.markdown(
    f"""
    Start the app:
    ```bash
    # nohup: Keeps the process running after logout
    # & : Run in the background
    nohup <path_to_venv>/bin/streamlit run main.py &
    ```

    Check running apps:
    ```bash
    pgrep -a streamlit
    # 144000 /home/marit/streamlit/streamlit/bin/python3 ../streamlit/bin/streamlit run main.py{nl}
    # 144010 /home/marit/streamlit/streamlit/bin/python3 ../streamlit/bin/streamlit run main.py
    ```

    Stop the app:
    ```bash
    kill 144010
    ```
    """
)
