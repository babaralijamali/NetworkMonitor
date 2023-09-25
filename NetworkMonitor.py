#Real-time Network Monitoring Tools
import psutil
import tkinter as tk
from tkinter import ttk

def get_network_usage():
    network_info = {}
    for conn in psutil.net_connections(kind='inet'):
        pid = conn.pid
        if pid is not None:
            try:
                process = psutil.Process(pid)
                process_name = process.name()
                network_info[process_name] = network_info.get(process_name, 0) + 1
            except psutil.NoSuchProcess:
                pass
    return network_info

def update_network_usage():
    network_info = get_network_usage()
    sorted_network_info = dict(sorted(network_info.items(), key=lambda item: item[1], reverse=True))
    text.delete('1.0', tk.END)
    for process_name, connections in sorted_network_info.items():
        text.insert(tk.END, f"{process_name}: {connections} connections\n")
    root.after(1000, update_network_usage)

root = tk.Tk()
root.title("Real-Time Network Monitoring Tool by Babar Ali Jamali")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

label = ttk.Label(frame, text="Network Usage (Connections)")
label.pack()

text = tk.Text(frame, wrap=tk.WORD, height=20, width=40)
text.pack()

update_network_usage()

root.mainloop()
