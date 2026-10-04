import socket

def run_udp_client():
    server_host = '127.0.0.1'
    server_port = 12345
    server_address = (server_host, server_port)

    # Maak client UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5.0)       # geef timout 

    print("[CLIENT] UDP Client ready. Type 'exit' to stop.")

    try:
        while True:
            message = input("\nGive a whole number (or type 'exit'): ")
            if message.lower() == 'exit':
                break

            client_socket.sendto(message.encode('utf-8'), server_address)


            try:
                data, _ = client_socket.recvfrom(1024)
                print(f"[CLIENT] answer from server is: {data.decode('utf-8')}")
            except socket.timeout:
                print("[CLIENT ERROR] No response from server (Timeout).")

    except Exception as e:
        print(f"[CLIENT ERROR] {e}")
    finally:
        client_socket.close()
        print("[CLIENT] Socket gesloten.")

if __name__ == '__main__':
    run_udp_client()