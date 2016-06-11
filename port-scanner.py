import socket
import sys	

try:
	ip = sys.argv[1]
except:
	print "  USAGE: python port-scanner.py <IPv4_Address>"
	print "EXAMPLE: python port-scanner.py 192.168.1.1"
	exit()
	

for port in range(1, 200):
	try:
		#socket constructor
		# 1st arg is the IP version (socket.AF_INET is IPV4)
		# 2nd arg is the TCP or UDP (socket.SOCK_STREAM is TCP)
		
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		#Set the timeout to 1/4 of a second
		#This line will let us differentiate between closed ports
		#and ports blocked by a firewall.
				
		conn.settimeout(.25) 		

		conn.connect((ip, port))
	
		#If a port is open, a syn/ack will be sent back, causing no exception
		#and the three-way handshake will complete normally.
	
		print "Port %i is open." % port		
		conn.close()
	
	#A socket.timeout exception will occur if there is 
	#no response to the SYN request is received 
	#This indicates that there is a firewall in place.

	except socket.timeout:
		print "Port %i is filtered." % port

	#A socket.error exception will occur if there is
	#a RST flag received in response to the SYN request
	#This indicates that the port is closed; there is nothing listening.
 
	except socket.error:
		print "Port %i is closed." % port		


