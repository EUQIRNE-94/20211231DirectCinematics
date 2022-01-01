# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 11:23:43 2021

@author: enriq
"""

import vpython as vs
 
def change(b): # Called by controls when button clicked
    if b.text == 'Click me':
        b.text = 'Try again'
    else:
        b.text = 'Click me'

c = vs.controls()
b = vs.button( pos=(0,0), width=60, height=60, text='Click me', bind=change)

