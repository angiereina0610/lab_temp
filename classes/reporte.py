# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 15:15:11 2022

@author: Angie Reina
"""

from datetime import datetime
import time
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


def get_all_temp():
    a=open("database/Datos.csv","r")
    datos=a.readlines()
    return datos


def grafica():
    datos=get_all_temp()
    y_axis=[]
    datos_0=";".join(datos)
    datos_0=datos_0.split(";")

    for i in range(len(datos_0)):
        e=datos_0[i].split(" ")
        y_axis.append(int(e[2]))
    print(y_axis)

    x_axis=[]
    for i in range(len(datos_0)):
        e=datos_0[i].split(" ")
        x_axis.append(e[1])
    print(x_axis)
    plt.plot(x_axis, y_axis)
    plt.show()
    

def valor_max():
    datos=get_all_temp()
    vec=[]
    datos_0=";".join(datos)
    datos_0=datos_0.split(";")

    for i in range(len(datos_0)):
        e=datos_0[i].split(" ")
        vec.append(int(e[2]))
    maxi=max(vec)
    maxi_ub=[]

    for n in range(len(vec)):
        if vec[n] == maxi:
            maxi_ub.append(n)

    for i in range(len(maxi_ub)):
        g=datos_0[maxi_ub[i]].split(" ")
        print("El valor maximo de temperatura es "+str(g[2])+" en la fecha "+g[0]+" a la hora "+g[1])
        print("")


def valor_min():
    datos=get_all_temp()
    vec=[]
    datos_0=";".join(datos)
    datos_0=datos_0.split(";")

    for i in range(len(datos_0)):
        e=datos_0[i].split(" ")
        vec.append(int(e[2]))
    mini=min(vec)
    mini_ub=[]

    for n in range(len(vec)):
        if vec[n] == mini:
            mini_ub.append(n)
 
    for i in range(len(mini_ub)):
        g=datos_0[mini_ub[i]].split(" ")
        print("El valor minimo de temperatura es "+str(g[2])+" en la fecha "+g[0]+" a la hora "+g[1])
        print("")

#-------------------------------------------------------------------------------------------------------------
def prom_temp():
    datos=get_all_temp()
    vec=[]
    datos_0=";".join(datos)
    datos_0=datos_0.split(";")

    for i in range(len(datos_0)):
        e=datos_0[i].split(" ")
        vec.append(int(e[2]))
    suma = 0

    for valor in vec:
        suma = suma + valor
    prom_t= suma / len(vec)
    datos_para=get_all_parametros()
    vec_para=[]
    datos_para=datos_para[0].split(";")

    for i in range (len(datos_para)):
        vec_para.append(int(datos_para[i]))

    if prom_t>= vec[0] and prom_t <=vec[1]:
        temp=" DE HIPOTERMIA"
    elif prom_t >=vec[2] and prom_t <= vec[3]:
        temp ="NORMAL"
    elif prom_t >=vec[4] and prom_t <= vec[5]:
        temp="DE FIEBRE"
    print("El promedio de temperaturas es de: "+str(prom_t)+" grados centigrados")
    print("")
  

#-------------------------------------------------------------------------------------------------------------
def get_all_parametros():
    a=open("database/Parametros.csv","r")
    datos=a.readlines()
    return datos
