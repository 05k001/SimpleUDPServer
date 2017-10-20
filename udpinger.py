#UDPinger Server Python Random packet loss server

import random
from socket import *

#Create UDP Socket

serverSocket = socket(AF_INET, SOCK_DGRAM)

#Assign Ip

serverSocket.bind(('',12000))



while True:
    #Generate Random Number from 0 - 10
    rand = random.randint(0,10)
    #Recieve the Client Pkg
    message, address  = serverSocket.recvfrom(1024)
    #Caps that
    message = message.upper()
    #If rand is less than 4 its lost
    if rand < 4:
        continue
    serverSocket.sendto(message, address)
    
