#!/usr/bin/python3
#coding: utf-8
import time
#import os
import random

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
    time.sleep(abs(k))
    if k>0.159:
        k=0.159
    if k<0.000:
        k=0.000
    zap_strobe()
    k=k+random.randrange(-1000,1000)/1000000

  
