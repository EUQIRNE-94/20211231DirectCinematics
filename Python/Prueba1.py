# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 21:50:32 2021

@author: enriq
"""

import serial
import time
import numpy as np


com = serial.Serial("COM6",115200)
time.sleep(1)
com.read_until()
com.read_until()


t0 = time.time()
tant = 0
try:
    while True:
        tact = time.time() - t0
        if (com.inWaiting() > 0):
            data = com.read_until()
            data_clean = data[0:len(data)-2].decode()
            valuesF = np.array(data_clean.split(","),dtype=float)
            print(valuesF)
            
            
            
            if (tact >= 2):
                break
            
except KeyboardInterrupt:
    pass

com.close()