#!/bin/python3
#This is for sender section.
import socket


target_ip = "127.0.0.1"
target_port = 8080

#Now we are creating UDP socket.
#                     Ipv4     , UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)    #This part will use sender and receiver both.

msg=input("Enter your message : ")

#Now we can send to target.
#s.sendto(msg,(target_ip,target_port))
#We have to encode string to byte like object in python3 not necessary in python2.


#while True:
newmsg = msg.encode('ascii')                 #msg will trasfer in encode form ascii format.
print(newmsg)
#Now we send msg to target.
s.sendto(newmsg,(target_ip,target_port))
print(s.recvfrom(100))                  #s.recvfrom("count of character")







