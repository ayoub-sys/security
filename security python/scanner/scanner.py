import socket
from IPy import IP 

def scan(target):
    converted_ip = check_ip(target)
    print('\n'+ '[-_0 Scanning Target]'+ str(target))
    for port in range(1,100):
        scan_port(converted_ip, port)
def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)
def scan_port(ipaddress, port):
 try:
    sock = socket.socket()
    sock.settimeout(0.5)
    sock.connect((ipaddress,port))
    try:
     banner=get_banner(sock)
     print('[+] port'+ str(port) + 'is open' + ':' +str(banner))

    except:
     print('[+] port' + str(port) + 'is open') 
 except:
    pass 
def get_banner(s):
    return s.recv(1024)


target =input("donner les targets")
for k in target.split(','):
    scan(k)

    