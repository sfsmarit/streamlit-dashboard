import streamlit as st
import psutil

import config
import utils as ut


def render_resouce_usage():
    # Resource usage
    cols = st.columns(3)
    with cols[0]:
        # CPU usage
        cpu_pct = psutil.cpu_percent(interval=1)
        with st.container(border=True):
            st.subheader("CPU")
            st.write(f"{cpu_pct:.1f}%")
            st.progress(int(min(cpu_pct, 100)))
    with cols[1]:
        # Memory usage
        mem = psutil.virtual_memory()
        mem_used_gb = mem.used / (1024**3)
        mem_total_gb = mem.total / (1024**3)
        with st.container(border=True):
            st.subheader("Memory")
            st.write(f"{mem_used_gb:.1f} / {mem_total_gb:.1f} GB")
            st.progress(int(min(mem.percent, 100)))
    with cols[2]:
        # Storage usage
        disk = psutil.disk_usage("/")
        disk_used_gb = disk.used / (1024**3)
        disk_total_gb = disk.total / (1024**3)
        with st.container(border=True):
            st.subheader("Storage")
            st.write(f"{disk_used_gb:.0f} / {disk_total_gb:.0f} GB")
            st.progress(int(min(disk.percent, 100)))


def render_available_ports(start=8501, stop=8699):
    # Used port
    data = []
    for dir in config.ROOT_DIRS:
        data += ut.collect_app_info(dir)
    used_ports = [d["port"] for d in data]
    available_ports = []
    for port in range(start, stop):
        if port in used_ports:
            continue
        if ut.can_bind(port):
            available_ports.append(port)

    st.markdown("#### Available Ports")
    st.selectbox("", available_ports, label_visibility="collapsed",
                 help="It is recommended to keep 8501-8599 open for test apps")
    st.markdown(
        f"""
        > It is recommended to keep ports 8501-8599 open for test apps.
        """
    )
