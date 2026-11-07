import socket
import streamlit as st

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception:
        return False

st.set_page_config(page_title="Port Scanner Web", page_icon="🔍")

st.title("🔍 Port Scanner Web")

target_ip = st.text_input("Masukkan IP Target", "127.0.0.1")
start_port = st.number_input("Port Awal", min_value=1, max_value=65535, value=1)
end_port = st.number_input("Port Akhir", min_value=1, max_value=65535, value=100)

if st.button("Mulai Scan"):
    st.write(f"Memindai {target_ip} dari port {start_port} hingga {end_port}...\n")
    with st.spinner("Memindai..."):
        open_ports = []
        for port in range(start_port, end_port + 1):
            if scan_port(target_ip, port):
                open_ports.append(port)
        if open_ports:
            st.success(f"Port terbuka: {open_ports}")
        else:
            st.warning("Tidak ditemukan port terbuka.")
