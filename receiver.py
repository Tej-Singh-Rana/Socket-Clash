#!/bin/python3

#This is for receiver side.
import socket,time,subprocess,pyttsx3

target_ip = "127.0.0.1"
target_port = 8080

#Now we are creating UDP socket.
#                  Ipv4       ,   UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)    #this part is used in sender & receiver both side.

#This is only for receiver.
s.bind((target_ip,target_port))
#print(s.recvfrom(100))                     #only one sender msg can receive at a time.

#To receive multiple msg at a time.
#while True:             
   # print(s.recvfrom(100))                        #s.recvfrom("count of character")
   # time.sleep(3)
   # print(s.recvfrom(100))

#while True:
client_data=s.recvfrom(150)
print(client_data)
#now converting msg into audio form.
#if module is not avaiable then install pip3 install pyttsx3.
audio1=pyttsx3.init()
audio1.say(client_data[0].decode('ascii')
audio1.runAndWait()
time.sleep(2)
print("-------------------------------------------")
print("##                                       ##")   
print("##                                       ##")   
print("-------------------------------------------")
print("Now replying to : -------------- ",client_data[1][0])
s.sendto("Hello!! thanks for the msg ".encode('ascii'),client_data[1])

#Now saving each data in system with its IP name.

subprocess.getoutput("touch "+client_data[1][0]+".txt")
with open(client_data[1][0]+".txt","a") as m:
    m.write(client_data[0].decode('ascii'))
