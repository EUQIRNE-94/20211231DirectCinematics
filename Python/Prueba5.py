# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 10:55:28 2021

@author: enriq
"""

# using VPython (visual) and Tkinter together
# with the help of Python module thread
# tested with VPython 5.4.1 and Python 2.7.1 by vegaseat

import vpython as vs
import tkinter as tk
import threading

# will be global
sphere = None

def vthread():
    global sphere
    vs.scene.title = "Sphere in space (3D drag with right mouse button)"
    vs.scene.autoscale = False
    sphere = vs.sphere(pos=vs.vector(0, 0, 0), color=vs.color.green)

def move_sphere_incr_x(event=None):
    """moves along the x axis incrementing x"""
    sphere.pos = sphere.pos + vs.vector(1, 0, 0)

def move_sphere_decr_x(event=None):
    """moves along the x axis decrementing x"""
    sphere.pos = sphere.pos - vs.vector(1, 0, 0)

def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        vs.scene.delete()

root = tk.Tk()
w = 300
h = 200
x = 450
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
root.title("Control Sphere from here")

b_incr_x = tk.Button(root, text="move on x axis increment x")
# bind passes an event to function
b_incr_x.bind("<Button-1>", move_sphere_incr_x)
b_incr_x.grid(row=0, column=0, padx=20, pady=10)

b_decr_x = tk.Button(root, text="move on x axis decrement x")
# bind passes an event to function
b_decr_x.bind("<Button-1>", move_sphere_decr_x)
b_decr_x.grid(row=1, column=0, padx=10)

# use thread to do run VPython and Tkinter simultaneously
# thread.start_new_thread(function, args)
# args is an empty tuple here
kk = threading.Thread(target=vthread())
kk.start()
# sphere = thread.start_new_thread(vthread, ())

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()