# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 13:46:44 2021

@author: enriq
"""

import numpy as np
import funciones as fx
import vpython as vp
import time

# vp.scene.autoscale = False
# vp.scene.range = 1.5
vp.scene.width = 1600
vp.scene.height = 800

dh = np.array([[0,90   ,0,57.4],
               [100,0  ,0,0],
               [100,0  ,0,0],
               [100,-90,0,0]])

xArrow = vp.arrow(pos = vp.vector(0,0,0),axis= vp.vector(100,0,0),shaftwidth = 0.5, color = vp.color.red)
yArrow = vp.arrow(pos = vp.vector(0,0,0),axis= vp.vector(0,100,0),shaftwidth = 0.5, color = vp.color.blue)
zArrow = vp.arrow(pos = vp.vector(0,0,0),axis= vp.vector(0,0,-100),shaftwidth = 0.5, color = vp.color.green)

T1 = fx.DH(dh[0,0],dh[0,1],dh[0,2],dh[0,3])
T2 = fx.DH(dh[1,0],dh[1,1],dh[1,2],dh[1,3])
T3 = fx.DH(dh[2,0],dh[2,1],dh[2,2],dh[2,3])
T4 = fx.DH(dh[3,0],dh[3,1],dh[3,2],dh[3,3])

T1_2 = T1@T2
T1_3 = T1_2@T3
T1_4 = T1_3@T4

ball0 = vp.sphere(pos=vp.vector(0,0,0),radius=10,color=vp.color.white)

ball1 = vp.sphere(pos=vp.vector(T1[0,3],T1[2,3],T1[1,3]),radius=10,color=vp.color.red)
rod1 = vp.cylinder(pos=vp.vector(0,0,0),axis=vp.vector(T1[0,3],T1[2,3],T1[1,3]),color=vp.color.red,radius=5)

ball2 = vp.sphere(pos=vp.vector(T1_2[0,3],T1_2[2,3],T1_2[1,3]),radius=10,color=vp.color.green)
rod2 = vp.cylinder(pos=vp.vector(T1[0,3],T1[2,3],T1[1,3]),axis=vp.vector(T1_2[0,3]-T1[0,3],T1_2[2,3]-T1[2,3],T1_2[1,3]-T1[1,3]),color=vp.color.green,radius=5)

ball3 = vp.sphere(pos=vp.vector(T1_3[0,3],T1_3[2,3],T1_3[1,3]),radius=10,color=vp.color.blue)
rod3 = vp.cylinder(pos=vp.vector(T1_2[0,3],T1_2[2,3],T1_2[1,3]),axis=vp.vector(T1_3[0,3]-T1_2[0,3],T1_3[2,3]-T1_2[2,3],T1_3[1,3]-T1_2[1,3]),color=vp.color.blue,radius=5)

ball4 = vp.sphere(pos=vp.vector(T1_4[0,3],T1_4[2,3],T1_4[1,3]),radius=7.5,color=vp.color.purple)
rod3 = vp.cylinder(pos=vp.vector(T1_3[0,3],T1_3[2,3],T1_3[1,3]),axis=vp.vector(T1_4[0,3]-T1_3[0,3],T1_4[2,3]-T1_3[2,3],T1_4[1,3]-T1_3[1,3]),color=vp.color.purple,radius=5)
