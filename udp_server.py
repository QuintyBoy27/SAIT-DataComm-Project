import socket

def run_udp_server():
    host = '127.0.0.1'      # is voor de Localhost
    port = 12345        # is voor de Poortnummer

    # Maakt UDP socket aan
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    
    # zoda de socket aan de host en poort gecoonnect
    server_socket.bind((host, port))
    print(f"[SERVER] UDP Server listening on {host}:{port}...")

    try:
        while True:
            data, client_address = server_socket.recvfrom(1024)
            message = data.decode('utf-8')
            print(f"[SERVER] Received from {client_address}: '{message}'")


            try:
                number = int(message)
                if number % 2 == 0:
                    response = f" {number} is EVEN."
                else:
                    response = f" {number} is ODD."
            except ValueError:
                response = "Invalid input: Only whole numbers allowed."

            server_socket.sendto(response.encode('utf-8'), client_address)
            print(f"[SERVER] Answer to {client_address}: {response}")

    except KeyboardInterrupt:
        print("\n[SERVER] Server stopped...")
    finally:
        server_socket.close()
        print("[SERVER] Socket closed.")

if __name__ == '__main__':
    run_udp_server()