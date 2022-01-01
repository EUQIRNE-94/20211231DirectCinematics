# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 21:50:32 2021

@author: enriq
"""

import serial
import time
import numpy as np
import vpython as vp


vp.scene.autoscale = False
vp.scene.range = 1.5
vp.scene.width = 1600
vp.scene.height = 800

framerate = 100
ball1 = vp.sphere(pos=vp.vector( 1.5,0,0),radius=0.1,color=vp.color.red)
ball2 = vp.sphere(pos=vp.vector( 0.5,0,0),radius=0.1,color=vp.color.green)
ball3 = vp.sphere(pos=vp.vector(-0.5,0,0),radius=0.1,color=vp.color.blue)
ball4 = vp.sphere(pos=vp.vector(-1.5,0,0),radius=0.1,color=vp.color.purple)

xArrow = vp.arrow(pos = vp.vector(0,0,0),axis= vp.vector(1,0,0),shaftwidth = 0.05, color = vp.color.red)
yArrow = vp.arrow(pos = vp.vector(0,0,0),axis= vp.vector(0,1,0),shaftwidth = 0.05, color = vp.color.green)
zArrow = vp.arrow(pos = vp.vector(0,0,0),axis= vp.vector(0,0,1),shaftwidth = 0.05, color = vp.color.blue)

com = serial.Serial("COM6",115200)
time.sleep(1)
com.read_until()
com.read_until()


t0 = time.time()
tant = 0
dt = 1/framerate
try:
    while True:
        tact = time.time() - t0
        if (com.inWaiting() > 0):
            data = com.read_until()
            data_clean = data[0:len(data)-2].decode()
            # print(data_clean)
            valuesF = np.array(data_clean.split(","),dtype=float)
            valuesF = valuesF*(5/1024) - 2.5
            # print(valuesF)
            
        if (tact - tant >= dt):
            ball1.pos = vp.vector( 1.5,valuesF[0],0)
            ball2.pos = vp.vector( 0.5,valuesF[1],0)
            ball3.pos = vp.vector(-0.5,valuesF[2],0)
            ball4.pos = vp.vector(-1.5,valuesF[3],0)
            print(tact)
            tant = tact
            
            
            if (tact >= 30):
                break
            
except KeyboardInterrupt:
    pass

com.close()