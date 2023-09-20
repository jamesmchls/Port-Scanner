import socket
from termcolor import colored  # Import 'colored' function from 'termcolor' module


def scan(target, ports):
    print('\n' + 'Starting Scan For ' + target)
    for port in range(1, ports + 1):  # Adjust the range to include 'ports'
        # Correct the function call from 'targets' to 'target'
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        sock.connect((ipaddress, port))
        # Use 'colored' for green text
        print(colored("[+] Port Opened " + str(port), 'green'))
        sock.close()
    except (socket.timeout, ConnectionRefusedError):
        # Use 'colored' for red text
        print(colored("[-] Port Closed " + str(port), 'red'))


targets = input("[*] Enter Targets to Scan (Split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want to Scan: "))
if ',' in targets:
    print(colored("[*] Scanning Multiple Targets", 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)  # Remove extra space when stripping
else:
    scan(targets, ports)
