import socket
import tkinter as tk
from tkinter import messagebox, scrolledtext

def scan_ports():
    target = entry_target.get()
    try:
        start_port = int(entry_start.get())
        end_port = int(entry_end.get())
    except ValueError:
        messagebox.showerror("Error", "Port harus berupa angka.")
        return

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Memindai {target} dari port {start_port} hingga {end_port}...\n\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            result_text.insert(tk.END, f"[✓] Port {port} terbuka\n")
        sock.close()

# GUI Setup
window = tk.Tk()
window.title("Port Scanner GUI")
window.geometry("450x400")
window.resizable(False, False)

frame = tk.Frame(window)
frame.pack(pady=10)

tk.Label(frame, text="IP Target:").grid(row=0, column=0)
entry_target = tk.Entry(frame, width=30)
entry_target.grid(row=0, column=1)

tk.Label(frame, text="Port Awal:").grid(row=1, column=0)
entry_start = tk.Entry(frame, width=10)
entry_start.grid(row=1, column=1, sticky='w')

tk.Label(frame, text="Port Akhir:").grid(row=2, column=0)
entry_end = tk.Entry(frame, width=10)
entry_end.grid(row=2, column=1, sticky='w')

btn_scan = tk.Button(window, text="Mulai Scan", command=scan_ports, bg="green", fg="white")
btn_scan.pack(pady=10)

result_text = scrolledtext.ScrolledText(window, width=50, height=15)
result_text.pack(padx=10, pady=10)

window.mainloop()
