from tkinter import *
import tkinter
from datetime import datetime

color1 = "#3d3d3d"
color2 = "#8A2BE2"
color3 = "#000000"

fundo = color3
cor = color2

janela= Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE) #impossibilita alterar o tamanho da janela
janela.configure(bg=color3)

def relogio():
    tempo= datetime.now() #hora da maquina

    hora= tempo.strftime("%H:%M:%S")
    dia= tempo.strftime("%A")
    data = tempo.day
    mes = tempo.strftime("%b")
    ano= tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia + "  " + str(data) + "/" + str(mes) + "/" + str(ano))

l1= Label(janela, text="", font=("Arial 80"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2= Label(janela, text="", font=("Arial 20"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=S, padx=5)

relogio()
janela.mainloop()