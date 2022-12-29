import socket
import termcolor

def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket() #calling socket function from library
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        print("[-] Port Closed " + str(port))

targets = input("[*] Enter Targets to Scan: ")
ports = input("[*] Enter How Many Ports to Scan: ")

if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)

else: 
    scan(targets, ports)