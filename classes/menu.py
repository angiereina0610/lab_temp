# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 17:10:51 2022

@author: Angie Reina
"""

class Menu:
      def __init__(self, laboratorio):
        self.laboratorio=laboratorio
 

      def ver(self):
        print("BIENVENIDO AL LABORATORIO DE MONITOR DE TEMPERATURA".center(50,"*"))
        print("Laboratorio 3: "+self.laboratorio)
        print("1. Captura de datos")
        print("2. Configuracion de parametros")
        print("3. Reportes")
        print("4. Salir")
        op=input(">>>")
        return op
    

class Captura:
    def ver(self):
      print("Menu captura de datos".center(20,"*"))
      print("1. Escoger momento de captura ")
      print("2. Escoger momento de capura con grafica en tiempo real ")
      op=input(">>> ")
      return op

class Reportes:

    def ver(self):
      print("configuracion de parametros".center(20,"*"))
      print("1. Ver grafica de los datos capturados")
      print("2. Valor maximo")
      print("3. Valor minimo")
      print("4. Promedio de temperatura")
      op=int(input(">>> "))
      
      return op
  


  