# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 15:15:23 2022

@author: Angie Reina
"""

import serial
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
pause=False

try:
    global puerto
    puerto = serial.Serial("COM5",9600)
    puerto.close()
    puerto.open()
    print("Port is open")
except:
    print("Problemas abriendo puerto :( ")
    
def onclick(event):
    global pause
    print("pausa")
    pause=True


fig, ax=plt.subplots()
fig.canvas.mpl_connect("button_press_event", onclick)
y_data=[]

def update_data(i):
    if not pause:
        punto=puerto.readline().decode().strip()
        print(punto)
        y_data.append(punto)
        ax.clear()
        ax.plot(y_data)

ani= animation.FuncAnimation(fig,update_data)
plt.show()
