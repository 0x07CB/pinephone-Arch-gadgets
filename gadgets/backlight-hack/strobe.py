#!/usr/bin/python3
#coding: utf-8
import time
#import os

pathf = "/sys/class/leds/white:flash/flash_strobe"

def strobe_flash():
    with open(pathf,'w') as f:
        f.write("1")
        f.close()

pathf_b = "/sys/class/leds/white:flash/flash_strobe"
def zap_strobe():
    val=1
    for i in range(0,100):
        try:
            with open(pathf_b,'w') as f:
                val=int(not val)
                f.write(str(i))
        except Exception as e:
            pass
k=0.00
while (True):
    zap_strobe()
    time.sleep(k)
    if k<0.059:
        k=k+0.0005
  
