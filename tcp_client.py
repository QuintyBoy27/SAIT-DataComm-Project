import socket

def run_tcp_client():
    server_host = '127.0.0.1'
    server_port = 12346
    server_address = (server_host, server_port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"[TCP CLIENT] Making connection to TCP server at {server_host}:{server_port}...")
    
    try:
        client_socket.connect(server_address)
        print("[TCP CLIENT] Connected! Type 'exit' to stop.")
        while True:
            message = input("\nType a whole number to check if it's even or odd (or 'exit'): ")
            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode('utf-8'))

            data = client_socket.recv(1024)
            print(f"[TCP CLIENT] Received from server: {data.decode('utf-8')}")

    except Exception as e:
        print(f"[TCP CLIENT FOUT] There is an error: {e}")
    finally:
        client_socket.close()
        print("[TCP CLIENT] Connection closed.")

if __name__ == '__main__':
    run_tcp_client()