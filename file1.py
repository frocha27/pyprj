# Frederic Rocha
# January 2018
# Bergstrom Inc
#alternate version

import pycom
import time

for i in range(10): print(2**i)
pycom.heartbeat(False)
loop=True
i=0
for j in [0,8,16]:
    for i in range(1,256):
        color=(i*2**j)+(256-i)*2**(16)
        pycom.rgbled(color)
        time.sleep(0.1)
        print(i,'-',hex(color))
while loop:
    pycom.rgbled(0xff0000)  #Red LED
    time.sleep(0.3)
    pycom.rgbled(0x00ff00)  #Green LED
    time.sleep(0.3)
    pycom.rgbled(0x0000ff)  #Blue LED
    time.sleep(0.3)
    i=i+1
    print(i)
