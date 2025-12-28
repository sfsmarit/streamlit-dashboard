import streamlit as st
import socket

import common.components as components


def render():
    nl = "  "
    HOST = socket.gethostname()

    st.title("Streamlit Development Guide")

    placeholder_resource = st.empty()
    placeholder_port = st.empty()

    st.markdown("---")

    st.subheader("1. Obtain Streamlit Server Account", divider=True)
    st.markdown(
        f"""
        IT Service Desk{nl}
        https://skyworksinc.atlassian.net/servicedesk/customer/portal/9/group/37/create/229 {nl}
        
        ```
        [Summary]
        Request for login access to {HOST}
        
        [Description]
        I would like to release a Streamlit Web application and request the following access permissions:
        1. Login access to {HOST}
        2. Write permission to /data
        ```
        """
    )

    st.subheader("2. App Development & Deployment", divider=True)
    st.markdown(
        f"""
        Detailed explanation is available on this page:{nl}
        https://app-startguide.streamlit.app/
        
        To log in via ssh from a Windows PC, you need to go through the IRV server:
        ```bash
        ssh <UserName>@sftp_irv
        # On the remote server
        ssh http://uw-v-appstm-000.nb-engr.skyworksinc.com
        ```

        When deploying, place the app in `/data/streamlit/`.
        ```bash
        cd /data/streamlit/
        git clone https://github.com/<UserName>/sample-app.git
        ```
        
        """
    )

    st.subheader("3. Fixing the Port", divider=True)
    st.markdown(
        f"""
        Create `.streamlit/config.toml`.
        ```bash
        # Move to the project directory
        cd /data/streamlit/sample-app/
        
        # Create .streamlit/config.toml
        mkdir .streamlit
        touch .streamlit/config.toml
        ```    
        
        Add the following to config.toml:      
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
        Make the app visible on the Dashboard.
        ```bash
        # Move to the project directory
        cd /data/streamlit/sample-app/

        # Copy info.yaml
        cp /data/streamlit/dashboard/info.yaml ./
        ```    

        Edit info.yaml:
        ```yaml
        app: "AppName"
        description: ""
        intended_users: ""
        developer: "YourName"
        email: ""
        test: false
        visible: true
        ```    
        """
    )

    st.subheader("5. Start the App", divider=True)
    st.markdown(
        f"""
        Start the app:
        ```bash
        # /data/streamlit/streamlit : Python virtual environment 
        # nohup : Keeps process running after logout
        # & : Run in background
        cd /data/streamlit/sample-app/
        nohup /data/streamlit/streamlit/bin/streamlit run main.py &
        ```

        Check running apps:
        ```bash
        pgrep -a streamlit
        # 144000 /home/marit/streamlit/streamlit/bin/python3 ../streamlit/bin/streamlit run streamlit_dashboard.py{nl}
        # 144010 /home/marit/streamlit/streamlit/bin/python3 ../streamlit/bin/streamlit run tapeout_checklist.py
        ```

        Stop the app:
        ```bash
        kill 144010
        ```
        """
    )

    components.render_resouce_usage(placeholder_resource)
    components.render_available_ports(placeholder_port)
