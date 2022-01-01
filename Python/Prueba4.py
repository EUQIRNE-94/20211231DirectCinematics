# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:50:35 2021

@author: enriq
"""

import sys
import numpy as np
import funciones as fx
import vpython as vp
import time
import serial

com = serial.Serial("COM6",115200)
time.sleep(1)


# vp.scene.autoscale = False
# vp.scene.range = 1.5
vp.scene.width = 1600
vp.scene.height = 800

dh = np.array([[0,90   ,0,57.4],
               [100,0  ,0,0],
               [100,0  ,0,0],
               [100,-90,0,0]])
cero = np.array([509,170,522,524])

xArrow = vp.arrow(pos = vp.vector(0,0,0),axis= vp.vector(100,0,0),shaftwidth = 0.5, color = vp.color.red)
yArrow = vp.arrow(pos = vp.vector(0,0,0),axis= vp.vector(0,100,0),shaftwidth = 0.5, color = vp.color.green)
zArrow = vp.arrow(pos = vp.vector(0,0,0),axis= vp.vector(0,0,100),shaftwidth = 0.5, color = vp.color.blue)

T1 = fx.DH(dh[0,0],dh[0,1],dh[0,2]-90,dh[0,3])
T2 = fx.DH(dh[1,0],dh[1,1],dh[1,2],dh[1,3])
T3 = fx.DH(dh[2,0],dh[2,1],dh[2,2],dh[2,3])
T4 = fx.DH(dh[3,0],dh[3,1],dh[3,2],dh[3,3])

T1_2 = T1@T2
T1_3 = T1_2@T3
T1_4 = T1_3@T4

ball0 = vp.sphere(pos=vp.vector(0,0,0),radius=10,color=vp.color.white)

ball1 = vp.sphere(pos=vp.vector(T1[0,3],T1[1,3],T1[2,3]),radius=10,color=vp.color.red)
rod1 = vp.cylinder(pos=vp.vector(0,0,0),axis=vp.vector(T1[0,3],T1[1,3],T1[2,3]),color=vp.color.red,radius=5)

ball2 = vp.sphere(pos=vp.vector(T1_2[0,3],T1_2[1,3],T1_2[2,3]),radius=10,color=vp.color.green)
rod2 = vp.cylinder(pos=vp.vector(T1[0,3],T1[1,3],T1[2,3]),axis=vp.vector(T1_2[0,3]-T1[0,3],T1_2[1,3]-T1[1,3],T1_2[2,3]-T1[2,3]),color=vp.color.green,radius=5)

ball3 = vp.sphere(pos=vp.vector(T1_3[0,3],T1_3[1,3],T1_3[2,3]),radius=10,color=vp.color.blue)
rod3 = vp.cylinder(pos=vp.vector(T1_2[0,3],T1_2[1,3],T1_2[2,3]),axis=vp.vector(T1_3[0,3]-T1_2[0,3],T1_3[1,3]-T1_2[1,3],T1_3[2,3]-T1_2[2,3]),color=vp.color.blue,radius=5)

ball4 = vp.sphere(pos=vp.vector(T1_4[0,3],T1_4[1,3],T1_4[2,3]),radius=7.5,color=vp.color.purple)
rod4 = vp.cylinder(pos=vp.vector(T1_3[0,3],T1_3[1,3],T1_3[2,3]),axis=vp.vector(T1_4[0,3]-T1_3[0,3],T1_4[1,3]-T1_3[1,3],T1_4[2,3]-T1_3[2,3]),color=vp.color.purple,radius=5)


com.read_until()
com.read_until()

t0 = time.time()
tant = 0
try:
    while True:
        tact = time.time() - t0
        if (com.inWaiting() > 0):
            ## Obtener datos de MCU
            data = com.read_until()
            data_clean = data[0:len(data)-2].decode()
            valuesF = np.array(data_clean.split(","),dtype=float)
            
            ## Separar datos a su respetivo elemento
            torso = (valuesF[1] - cero[0])*0.2643
            hombro = (valuesF[2] - cero[1])*0.2469
            codo = (valuesF[3] - cero[2])*0.2524
            muñeca = (valuesF[4] - cero[3])*0.2459
            
            # print(torso,hombro,codo,muñeca)
            
            ## Actualizar cinematica direta
            T1 = fx.DH(dh[0,0],dh[0,1],torso-90,dh[0,3])
            T2 = fx.DH(dh[1,0],dh[1,1],hombro,dh[1,3])
            T3 = fx.DH(dh[2,0],dh[2,1],codo,dh[2,3])
            T4 = fx.DH(dh[3,0],dh[3,1],muñeca,dh[3,3])

            T1_2 = T1@T2
            T1_3 = T1_2@T3
            T1_4 = T1_3@T4
            
            ## Actualizar interfaz

            ball2.pos = vp.vector(T1_2[0,3],T1_2[1,3],T1_2[2,3])
            rod2.pos = vp.vector(T1[0,3],T1[1,3],T1[2,3])
            rod2.axis = vp.vector(T1_2[0,3]-T1[0,3],T1_2[1,3]-T1[1,3],T1_2[2,3]-T1[2,3])

            ball3.pos = vp.vector(T1_3[0,3],T1_3[1,3],T1_3[2,3])
            rod3.pos = vp.vector(T1_2[0,3],T1_2[1,3],T1_2[2,3])
            rod3.axis = vp.vector(T1_3[0,3]-T1_2[0,3],T1_3[1,3]-T1_2[1,3],T1_3[2,3]-T1_2[2,3])

            ball4.pos = vp.vector(T1_4[0,3],T1_4[1,3],T1_4[2,3])
            rod4.pos = vp.vector(T1_3[0,3],T1_3[1,3],T1_3[2,3])
            rod4.axis = vp.vector(T1_4[0,3]-T1_3[0,3],T1_4[1,3]-T1_3[1,3],T1_4[2,3]-T1_3[2,3])
            
            # if (tact >= 5):
            #     break
            
except KeyboardInterrupt:
    pass

com.close()
