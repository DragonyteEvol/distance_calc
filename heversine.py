from tkinter import *
from functions import *
import tkinter.font as tkFont

root=Tk()
root.title("Distance Calc")
frame=Frame(root,bg="#0c4271")
frame.pack()
result=StringVar()
#FUNCTIONS
def runHev():
    global result
    result.set(str(heversine(cor_a.get(),cor_b.get()))+" mts")

#---------------------------------------------------


#MENU
def clearData():
    cor_a.delete(0,'end')
    cor_b.delete(0,'end')


barmenu = Menu(root,bg="#e4efe7",border=0,borderwidth=0)
root.config(menu=barmenu)

menu_archivo=Menu(barmenu,tearoff=0)
menu_archivo.add_command(label="Salir",command=closeProgram)


menu_edicion=Menu(barmenu,tearoff=0)
menu_edicion.add_command(label="Borrar Datos",command=clearData)

menu_ayuda=Menu(barmenu,tearoff=0)
menu_ayuda.add_command(label="Acerca de",command=about)
#datayuda.add_command(label="Acerca de",command=infoAdicional)

barmenu.add_cascade(label="Archivo",menu=menu_archivo)
barmenu.add_cascade(label="Edicion",menu=menu_edicion)
barmenu.add_cascade(label="Ayuda",menu=menu_ayuda)

#FONTS
fontExample = tkFont.Font(family="System", size=10, weight="bold")


# CORDENADA A
label_a=Label(frame,text="Coordenada A:",bg="#0c4271",fg="#fdfaf6")
label_a.configure(font=fontExample)
label_a.grid(row=0,column=0,padx=5)
cor_a=Entry(frame,borderwidth=0)
cor_a.grid(row=0,column=1,padx=5)


# CORDENADA B
label_b=Label(frame,text="Coordenada B:",bg="#0c4271",fg="#fdfaf6")
label_b.grid(row=1,column=0,padx=5)
label_b.configure(font=fontExample)
cor_b=Entry(frame,borderwidth=0)
cor_b.grid(row=1,column=1,padx=5)


#RESULT
label_c=Label(frame,textvariable=result,bg="#0c4271", fg="#fdfaf6")
label_c.configure(font=fontExample)
label_c.grid(row=3,column=0,columnspan=2)


#BUTTONS
button_go=Button(frame,text="Distancia",command=lambda:runHev(),overrelief="flat",borderwidth=0)
button_go.configure(font=fontExample)
button_go.grid(row=2,column=0,columnspan=2,pady=5)



root.mainloop()
