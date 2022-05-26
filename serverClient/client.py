# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 21:48:55 2021

@author: khlifi
"""

import socket            
 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.close() 