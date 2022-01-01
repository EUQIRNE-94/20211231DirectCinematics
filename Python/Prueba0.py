# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:06:06 2021

@author: enriq
"""

import vpython as vp
import time

# vp.scene.backgorund = vp.color.cyan
vp.scene.autoscale = False
vp.scene.range = 5
vp.scene.width = 1600
vp.scene.height = 800

ball = vp.sphere(pos=vp.vector(0,0,0),radius=1,color=vp.color.red)
xArrow = vp.arrow(pos = vp.vector(0,0,0),axis= vp.vector(1,0,0),shaftwidth = 0.05, color = vp.color.red)
yArrow = vp.arrow(pos = vp.vector(0,0,0),axis= vp.vector(0,1,0),shaftwidth = 0.05, color = vp.color.green)
zArrow = vp.arrow(pos = vp.vector(0,0,0),axis= vp.vector(0,0,1),shaftwidth = 0.05, color = vp.color.blue)

time.sleep(1)

framerate = 30
t = 0
deltat = 1/framerate
while t < 2:
    # vp.scene.background = vp.color.cyan
    vp.rate(framerate)
    ball.pos = ball.pos + vp.vector(1,0,0)*deltat
    t = t + deltat
