import socket
import time

UDP_IP = "10.0.2.15" #change to the IP value of your VM
#UDP_IP = "127.0.0.1" #change to the IP value of your VM
UDP_PORT = 8000   #The port of the rx

counter=10

MESSAGE = "I:+20:+20:+20:E_"
print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)
MESSAGE=MESSAGE
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
while True:
	
	if counter>=50:
		counter=5
	counter=counter +5
	MESSAGE = "I:+00:+00:+"+ str(counter) + ":E_"
	sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT)) #sends the specified message using UDP
	
	#print ("message:", MESSAGE)
	time.sleep(1)
