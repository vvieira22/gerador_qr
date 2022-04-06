from tkinter import *
from turtle import width 

root = Tk()

class Aplicacao():
    def __init__(self,root):
        self._root = root
        self.configuracoes_abertura()
        self.tela_inicial_qr()
        self.widgets_frame1()
        root.mainloop()

    def configuracoes_abertura(self):
        self._root.title("Gerador de QR code") #texto barra superior
        self._root.configure(background="#6959CD")#cor background

        #=============abrir centralizado=============
        w = 800
        h = 600

        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        #============================================

        # self._root.geometry(f'{w}x{h}') #tamanho tela
        self._root.resizable(True, True) #responsivel vertical e horizontal
        self._root.maxsize(width=1920, height=1080) #maximo tela
        self._root.minsize(width=480, height=350) #minimo tela
    
    def tela_inicial_qr(self):
        self._frame_1 = Frame(self._root, bd=4, bg="#1E90FF", highlightbackground="#99208a", 
        highlightthickness=2)
        self._frame_1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def widgets_frame1(self):
        self._botao_limpar = Button(self._frame_1, text="Limpar", font=("Helvetica", 14))
        self._botao_limpar.place(relx=0.523, rely=0.95, relwidth=0.12, relheight=0.06 , anchor="w")

        self._botao_limpar = Button(self._frame_1, text="Gerar QR", font=("Helvetica", 14))
        self._botao_limpar.place(relx=0.5, rely=0.95, relwidth=0.12, relheight=0.06 , anchor="e")

    
 
Aplicacao(root)