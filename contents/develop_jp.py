import streamlit as st
import socket

import common.components as components


def render():
    nl = "  "
    HOST = socket.gethostname()

    st.title("Streamlit 開発ガイド")

    placeholder_resource = st.empty()
    placeholder_port = st.empty()

    st.markdown("---")

    st.subheader("1. Streamlit サーバのアカウントを取得", divider=True)
    st.markdown(
        f"""
        IT Service Desk{nl}
        https://skyworksinc.atlassian.net/servicedesk/customer/portal/9/group/37/create/229 {nl}
        
        ```
        [Summary]
        Request for login access to {HOST}
        
        [Description]
        I would like to release Streamlit Web application and request the following access permissions:
        1. Login accress to {HOST}
        2. Write permission to /data
        ```
        """
    )

    st.subheader("2. アプリ開発・デプロイ", divider=True)
    st.markdown(
        f"""
        こちらのページで詳しく解説しています。{nl}
        https://app-startguide.streamlit.app/
        
        Windows PC から`ssh`でログインするには、IRV サーバを経由します。
        ```bash
        ssh <UserName>@sftp_irv
        # ログイン先で
        ssh http://uw-v-appstm-000.nb-engr.skyworksinc.com
        ```
        
        デプロイするときは `/data/streamlit/` にアプリを配置してください。
        ```bash
        cd /data/streamlit/
        git clone https://github.com/<UserName>/sample-app.git
        ```
        
        """
    )

    st.subheader("3. ポートの固定", divider=True)
    st.markdown(
        f"""
        `.streamlit/config.toml` を作成します。
        ```bash
        # プロジェクトディレクトリに移動
        cd /data/streamlit/sample-app/
        
        # .streamlit/config.toml を作成
        mkdir .streamlit
        touch .streamlit/config.toml
        ```    
        
        config.toml に以下を記述します。      
        ```toml
        [server]
        port=8650
        ```    

        利用可能なポートについては、ページ上部の [Available Ports] を参照してください。
        """
    )

    st.subheader("4. info.yaml の配置", divider=True)
    st.markdown(
        f"""
        アプリが Dashboard に表示されるようにします。
        ```bash
        # プロジェクトディレクトリに移動
        cd /data/streamlit/sample-app/

        # info.yaml をコピー
        cp /data/streamlit/dashboard/info.yaml ./
        ```    

        info.yaml を編集します。
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

    st.subheader("5. アプリの起動", divider=True)
    st.markdown(
        f"""
        アプリの起動
        ```bash
        # /data/streamlit/streamlit : Python 仮想環境 
        # nohup : ログアウトしてもプロセスが残る
        # & : バックグラウンド実行
        cd /data/streamlit/sample-app/
        nohup /data/streamlit/streamlit/bin/streamlit run main.py &
        ```

        実行中のアプリの確認
        ```bash
        pgrep -a streamlit
        # 144000 /home/marit/streamlit/streamlit/bin/python3 ../streamlit/bin/streamlit run streamlit_dashboard.py{nl}
        # 144010 /home/marit/streamlit/streamlit/bin/python3 ../streamlit/bin/streamlit run tapeout_checklist.py
        ```

        アプリの終了
        ```bash
        kill 144010
        ```
        """
    )

    components.render_resouce_usage(placeholder_resource)
    components.render_available_ports(placeholder_port)
