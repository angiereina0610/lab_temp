
from classes.menu import *
from classes.rangos import *
from classes.obtención import *
from classes.reporte import *
import sys
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

global pause
pause = False
global y_data
y_data = []


def onclick(event):
    global pause
    print("pausa")
    pause=True  
    

fig, ax=plt.subplots()
fig.canvas.mpl_connect("button_press_event", onclick)     

def update_data(i): 
    if not pause:
        
        dato=int(puerto.readline().decode().strip())
        print(dato)
        y_data.append(dato)
        ax.clear()
        ax.plot(y_data)
        time.sleep(1)
        
        
def main():
    menu = Menu("Escuela de Ingeniería")
    op=menu.ver()

    
    if op == "1":
        menu2=Captura()
        op2=menu2.ver()
        if op2=="1":
            obtencion()
            main()
        elif op2=="2":
            ani= animation.FuncAnimation(fig,update_data)
            plt.show()
            save_dato(y_data)
            main()
            
    elif op =="2":
        eq=definir_rangos()
        eq.save_parametros()  
        main()

            
    elif op=="3":
        menu2=Reportes()
        op2=menu2.ver()
        if op2==1:
            grafica()
            main()
        elif op2==2:
            valor_max()
            main()
        elif op2==3:
            valor_min()
            main()
        elif op2==4:
            prom_temp()
            main()

           
    elif op=="4":
        exit()
    else:
            print("Opción inválida")
            main()
        
    

if __name__=='__main__':
    main()
