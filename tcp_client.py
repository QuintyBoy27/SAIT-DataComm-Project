import socket

def run_tcp_client():
    server_host = '127.0.0.1'
    server_port = 12346
    server_address = (server_host, server_port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"[TCP CLIENT] Verbinding maken met TCP server op {server_host}:{server_port}...")
    
    try:
        client_socket.connect(server_address)
        print("[TCP CLIENT] Verbonden! Typ 'exit' om te stoppen.")

        while True:
            message = input("\nVoer een geheel getal in om te controleren (of 'exit'): ")
            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode('utf-8'))

            data = client_socket.recv(1024)
            print(f"[TCP CLIENT] Ontvangen van server: {data.decode('utf-8')}")

    except Exception as e:
        print(f"[TCP CLIENT FOUT] Er is een fout opgetreden: {e}")
    finally:
        client_socket.close()
        print("[TCP CLIENT] Verbinding gesloten.")

if __name__ == '__main__':
    run_tcp_client()