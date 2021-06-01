import math
import sys
from tkinter import font, messagebox
#CALCULOS
def splitCoor(string):
    index=string.index(",")
    coor_x = float(string[:index])
    coor_y = float(string[index+1:])
    return [coor_x,coor_y]


def validateCoor(string):
    if(string.find(",")==-1):
        return False
    else:
        return splitCoor(string)

def heversine(string_1,string_2):
    #ARRAY DE CORDENADAS
    coor_a=validateCoor(string_1)
    coor_b=validateCoor(string_2)

    #CODICION DE EJECUCION
    if(coor_b==False or coor_a==False):
        return False #SI HAY UN ERROR EN LA VALIDACION
    else:
        #VARIABLES LATITUD Y LONGITUD
        lat_1=coor_a[0]
        lon_1=coor_a[1]
        lat_2=coor_b[0]
        lon_2=coor_b[1]

        #VARIABLES MATEMATICAS
        dlat=lat_2-lat_1
        rad=math.pi/180
        dlon=lon_2-lon_1
        r_heart=6374.795477598

        #FUNCION HEVERSINE
        a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat_1)*math.cos(rad*lat_2)*(math.sin(rad*dlon/2))**2
        distancia=2*r_heart*math.asin(math.sqrt(a))
        return distancia*1000

#FUNCIONES MENU
def closeProgram():
    sys.exit()

def about():
    messagebox.showinfo("DragonyteEvol","2020")

