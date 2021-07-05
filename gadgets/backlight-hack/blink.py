#!/usr/bin/python3
#coding: utf-8
import time
#import os

pathf = "/sys/class/leds/white:flash/flash_strobe"

def strobe_flash():
    with open(pathf,'w') as f:
        f.write("1")
        f.close()


while (True):
    strobe_flash()
    time.sleep(2)

  
