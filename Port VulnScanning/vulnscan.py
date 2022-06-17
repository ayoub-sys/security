#! /usr/bin/env python3
import socket
import os
import sys


# search il filetext if when scanning vulnerable is occuring in  a given filetext

def retbanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        s.connect((ip,port))
        banner=s.recv(1024)
        return banner
    except:
        return

def checkVuln(banner,filename):
    f=open(filename,"r")
    for line in f.readlines():
        if line.strip("\n") in banner:
            print("[+] Server is vulnerable :"+ banner.strip("\n"))

def main():
    if len(sys.argv)==2:
        filename=sys.argv[1]
        if not os.path.isfile(filename):
            print('[-] file doesn \'t exist')
        if not os.access(filename, os.R_OK):
            print("[-] Access denied!")
            exit(0)
    else:
        print("[-] Usage :" + str(sys.arv[0])+"<vuln filename>")
        exit(0)
    portlist=[21,22,25,80,110,443,445]
    ip="192.168.1.15"
    for port in portlist:
        banner=retbanner(ip,port)
        if banner:
            print("[+]" + ip + "/" + str(port) + ":" + banner)
            checkVuln(banner,filename)