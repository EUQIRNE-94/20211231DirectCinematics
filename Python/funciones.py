# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 13:34:34 2021

@author: enriq
"""

import numpy as np

def DH (a,alpha,theta,d):
    
    alpha = np.deg2rad(alpha)
    theta = np.deg2rad(theta)
    
    M = np.array([[np.cos(theta), -np.sin(theta)*np.cos(alpha),  np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
                  [np.sin(theta),  np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
                  [0             ,  np.sin(alpha)               ,  np.cos(alpha)               , d],
                  [0,0,0,1]])
    
    return M

def rotX(M):
    theta = np.deg2rad(-90)
    MM = np.array([[1,0,0,0],
                   [0,np.cos(theta),-np.sin(theta),0],
                   [0,np.sin(theta),np.cos(theta),0],
                   [0,0,0,1]])@M
    
    return MM