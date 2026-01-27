import socket # Importing the socket module to create network connections
import threading # Importing the threading module to handle multiple threads
import matplotlib.pyplot as plt # Importing matplotlib for potential future use (not used in this snippet)

open_ports = [] # List to store open ports

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.settimeout(0.5) 
        result = s.connect_ex((ip, port))

        if result == 0:
            print(f"[*] Poort {port} is OPEN op {ip}")
            open_ports.append(port)

        s.close() # Close the socket
    except:
        pass

def show_port_chart(total_scanned):
    open_count = len(open_ports)
    closed_count = total_scanned - open_count

    labels = [f'Open({open_count})', f'Closed/Filterd({closed_count})']
    sizes = [open_count, closed_count]
    colors = ['#ff4444', '#66b3ff']

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=(0.1, 0))
    plt.title(f'Security Scan Results\nTarget: Ports 1-{total_scanned}')

    print("[*] Dashboard: Generating visual report...")
    plt.show()