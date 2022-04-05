from tkinter import *
from turtle import width

root = Tk()

class Aplicacao():
    def __init__(self,root):
        self._root = root
        self.configuracoes_abertura()
        self.tela_inicial_qr()
        root.mainloop()
    def configuracoes_abertura(self):
        self._root.title("Texto barra Superior") #texto barra superior
        self._root.configure(background="#6959CD")#cor background
        self._root.geometry("800x680") #tamanho tela
        self._root.resizable(True, True) #responsivel vertical e horizontal
        self._root.maxsize(width=1920, height=1080) #maximo tela
        self._root.minsize(width=480, height=350) #minimo tela
    
    def tela_inicial_qr(self):
        self._frame_1 = Frame(self._root, bd=4, bg="#1E90FF", highlightbackground="#99208a", 
        highlightthickness=2)
        self._frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self._frame_2 = Frame(self._root, bd=4, bg="#1E90FF", highlightbackground="#99208a", 
        highlightthickness=2)
        self._frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.45)

Aplicacao(root)