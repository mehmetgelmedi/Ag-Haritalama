from scapy.all import *
import sys
try:
	alive,dead=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]+"/255"), timeout=2, verbose=0)
	print "IP 	    - MAC"
	for i in range(0,len(alive)):
        	print alive[i][1].psrc + " - " + alive[i][1].hwsrc
except:
	pass