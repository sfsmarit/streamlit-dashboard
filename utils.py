from pathlib import Path
import socket
import yaml
import toml


HOST = socket.gethostname()


def generate_email_from_name(name: str) -> str:
    address = ".".join(name.lower().split())
    return f"{address}@skyworksinc.com"


def check_TCP_connection(port: int, timeout: float = 0.05) -> bool:
    """TCPコネクションが張れるかを確認（ポートが開いているか）"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((HOST, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False


def can_bind(port: int) -> bool:
    """指定ポートにバインド可能か（=他プロセスが使用していないか）"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # NOTE: OSごとの挙動差に注意。REUSEADDR は TIME_WAIT を回避するのに使われるが、
        # 厳密な占有チェックなら設定しない方が良い。
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, port))
        return True
    except OSError:
        return False
    finally:
        s.close()


def collect_app_info(root_dir: str) -> list[dict]:
    data = []

    info_files = list(Path(root_dir).rglob("info.yaml"))

    for file in info_files:
        # YAMLファイルの読み込み
        with open(file, "r", encoding="utf-8") as f:
            info = yaml.safe_load(f)

        # email を補完
        if not info["email"]:
            name = info.get("developer", "")
            info["email"] = generate_email_from_name(name)

        # .streamlit/config.toml の読み込み
        config_file = file.parent / ".streamlit/config.toml"
        if config_file.exists():
            config = toml.load(config_file)
            port = config.get("server", {}).get("port")
        else:
            port = "unknown"
        info["port"] = port

        url = f"http://{HOST}:{port}"
        info["url"] = url

        info["status"] = "enabled" if check_TCP_connection(info["port"]) else "disabled"

        data.append(info)

    return data
