import socket

def run_tcp_server():
    host = '127.0.0.1'
    port = 12346 

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"[TCP SERVER] Listening for connections on {host}:{port}...")

    try:
        while True:
            conn, client_address = server_socket.accept()
            print(f"[TCP SERVER] Connection accepted from {client_address}")

            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    
                    message = data.decode('utf-8')
                    print(f"[TCP SERVER] Received from {client_address}: '{message}'")

                    try:
                        number = int(message)
                        if number % 2 == 0:
                            response = f"{number} is EVEN."
                        else:
                            response = f"{number} is ODD."
                    except ValueError:
                        response = "Invalid input, Please use a whole number."

                    conn.sendall(response.encode('utf-8'))
                    print(f"[TCP SERVER] Response sent to {client_address}: {response}")

            print(f"[TCP SERVER] Connection with {client_address} disconnected.")

    except KeyboardInterrupt:
        print("\n[TCP SERVER] Server stopped by user.")
    finally:
        server_socket.close()
        print("[TCP SERVER] Server socket closed.")

if __name__ == '__main__':
    run_tcp_server()