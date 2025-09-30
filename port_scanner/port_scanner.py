# port_scanner.py

import socket

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # 1 second timeout
    try:
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def main():
    host = input("Enter target host (IP or domain): ")
    start_port = int(input("Enter start port number: "))
    end_port = int(input("Enter end port number: "))

    print(f"\nScanning {host} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is closed")

if __name__ == "__main__":
    main()



