#! /usr/bin/env python3

from socket import *
import optparse
from threading import *

def connScan(tgtHost,tgtPort):
    try:
        sock=socket(AF_INET,SOCK_STREAM)
        sock.connect((tgtHost,tgtPort))
        print('[+] %d/tcp open'.format(tgtPort))
    except:
        print('[-] %d/tcp closed'.format(tgtPort))
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)

    except:
        print("unkown target %s".format(tgtHost))
    
    try:
        tgtName=gethostbyaddr(tgtIP)
        print('[+] Scan Results For:' + tgtName[0])
    except:
        print('[+] Scan Results FOR :'+tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t=Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser=optparse.OptionParser('Usage of program:' + '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string' , help='specify the target host')
    parser.add_option('-p', dest='tgtPort', type='string' , help='specify the target port')
    (options,args)=parser.parse_args()
    tgtHost= options.tgtHost
    tgtPorts= str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0]==None):
        print (parser.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)
if __name__=='__main__':
        main()