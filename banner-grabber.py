import socket
import sys

try:
	ip = sys.argv[1]
	port = int(sys.argv[2])

except:
	print "  USAGE:\tpython banner-grabber.py <IPv4_Address> <PORT_NUMBER>"
	print "EXAMPLE:\tpython banner-grabber.py 192.168.1.1 80"


#Create an instance of type socket called conn
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to the IP/port provided at the command line
conn.connect((ip, port))

#Read the first 1024 bytes of data and print them to the screen
print conn.recv(1024)

#Close the connection
conn.close() 



