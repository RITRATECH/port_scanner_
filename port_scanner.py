import socket

# Fungsi untuk memindai port
def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set timeout 1 detik untuk menghindari penundaan panjang
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} terbuka di {target}")
    sock.close()

# Fungsi untuk memindai rentang port
def scan_ports(target, start_port, end_port):
    print(f"Menyambung ke {target}...")
    for port in range(start_port, end_port+1):
        scan_port(target, port)

# Memasukkan alamat IP target dan rentang port untuk dipindai
target_ip = "192.168.1.1"  # Ganti dengan IP target yang ingin dipindai
start_port = 1
end_port = 1024

scan_ports(target_ip, start_port, end_port)
