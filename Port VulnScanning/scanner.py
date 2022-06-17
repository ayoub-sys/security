import socket
sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)
host = input("[*] Enter The Host To Scan")
port=int(input("[*] Enter the Port To Scan"))
def portscanner():
    if sock.connect_ex((host,port)):
        #if is true return closed
        print ("port %d is closed" %(port))
    else:
        print("port %d is opened "%(port))
    

portscanner()