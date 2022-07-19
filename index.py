from tkinter import *
import tkinter
from datetime import datetime
import pyglet
pyglet.font.add_file("digital-7.ttf")

cor1 = "#3d3d3d"  
cor2 = "#fafcff"  
cor3 = "#21c25c"  
cor4 = "#eb463b"  
cor5 = "#dedcdc"  
cor6 = "#3080f0"  

fundo=cor1
cor=cor2

janela=Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=False,height=False)
janela.configure(bg=cor1)

def relogio():

    tempo=datetime.now()

    hora=tempo.strftime("%H:%M:%S")
    dia_semana=tempo.strftime("%A")
    dia=tempo.day
    mes=tempo.strftime("%B")
    ano=tempo.strftime("%Y")
    
    label_1.config(text=hora)
    label_1.after(200,relogio)
    label_2.config(text=dia_semana+"  " + str(dia) + "/" + str(mes)+ "/" + str (ano))

label_1=Label(janela,text="",font=("digital-7 100"),bg=fundo,fg=cor)
label_1.grid(row=0,column=0,sticky=NW,padx=5)


label_2=Label(janela,text="",font=("digital-7 17"),bg=fundo,fg=cor)
label_2.grid(row=1,column=0,sticky=NW,padx=5)

relogio()

janela.mainloop
