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

'''
Example usage:
python port_scanner.py
Enter target host (IP or domain): example.com
Enter start port number: 7500
Enter end port number: 7510
Scanning example.com from port 7500 to 7510...
Port 7500 is closed
Port 7501 is closed
Port 7502 is OPEN
Port 7503 is closed
Port 7504 is closed
Port 7505 is closed
Port 7506 is closed
Port 7507 is closed
Port 7508 is closed
Port 7509 is closed
Port 7510 is closed
This will scan ports 7500 to 7510 on example.com and report which are open.
'''

# Note: Scanning ports on systems you do not own or have permission to scan may be illegal. Always ensure you have authorization before performing a port scan.
# This script scans a range of ports on a specified host to check if they are open or closed.
# It uses Python's socket library to attempt connections to each port in the specified range.
# The user is prompted to enter the target host and the range of ports to scan.
# The results are printed to the console, indicating which ports are open and which are closed.
# The script includes error handling for socket errors and sets a timeout for connections to avoid long waits on unresponsive ports.
# The script is intended for educational purposes and should be used responsibly.
# Always ensure you have permission to scan the target host.
# Scanning ports without permission may be illegal in some jurisdictions.
# Use this script at your own risk.
# This script is provided "as is" without warranty of any kind.
# The author is not responsible for any damage or legal issues arising from the use of this script.
# Always follow ethical guidelines and legal requirements when performing network scans.

# End of port_scanner.py
