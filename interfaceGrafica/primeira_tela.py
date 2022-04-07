from tkinter import *
import os
from tkinter import filedialog
from turtle import title

root = Tk()

class limparTela():
    def limpa_tela(self):
            self._valor_qr.delete(0, END)   

class Aplicacao(limparTela):
    def __init__(self,root):
        self._root = root 
        self.carregar_imagem()
        self.configuracoes_abertura(self._root, 1000,800,1920,1080,1000,800,"Gerador de QR code", True, True)
        self.tela_inicial_qr()
        self.widgets_frame1()
        root.mainloop()

# TODO: POSSIVEL PONTO DE MELHORIA, TA MUITO ESTRANHO, CARREGAR E DPS LER A IMAGEM DNV
    def importar_imagem(self, caminho_imagem_com_formato):
        scriptpath = os.path.abspath(__file__) # get the complete absolute path to this script
        scriptdir = os.path.dirname(scriptpath) # strip away the file name
        imagepath = os.path.join(scriptdir, "imagens/" +str(caminho_imagem_com_formato)) # join together the scriptdir and the name of the image  
        return PhotoImage(file=imagepath) # make the image with the full path

    def carregar_imagem(self):
        self._imagem_lixeira = self.importar_imagem("trash.png")
        self._imagem_salvar = self.importar_imagem("salvar.png")
        self._imagem_storage = self.importar_imagem("storage.png")

    def configuracoes_abertura(self, janela, largura, altura, max_l, max_a, min_l, min_a, nome_janela, redimencional, movel):
        janela.title(nome_janela) #texto barra superior
        janela.configure(background="#f6f5ef")#cor background

        #=============abrir centralizado=============
        w = largura
        h = altura

        ws = janela.winfo_screenwidth()
        hs = janela.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
        #============================================

        # self._root.geometry(f'{w}x{h}') #tamanho tela
        if(redimencional):
            janela.resizable(True, True)
        else:
            janela.resizable(False, False)
            
        if(movel):
            janela.maxsize(width=max_l, height=max_a) #maximo tela
            janela.minsize(width=min_l, height=min_a) #minimo tela
        else:
            janela.geometry(f'{w}x{h}')
    
    def tela_inicial_qr(self):
        self._frame_1 = Frame(self._root, bd=4, bg="#495866", highlightthickness=7,
        highlightbackground = "black", highlightcolor= "black")
        self._frame_1.grid()
        self._frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
    
    def tela_salvar_qr(self):
        newWindow = Toplevel(self._root)
        self.configuracoes_abertura(newWindow, 400,250,400,350,400,350, "Como deseja salvar o QR?", False, False)
        
        self._botao_salvar_arquivo = Button(newWindow, text=" Salvar em Arquivo    ", font=("verdana", 12, 'bold'), bd=5, image=self._imagem_salvar,
        compound="right", bg = "#75a7a1", fg="black")
        self._botao_salvar_arquivo.place(relx=0.5, rely=0.30, relwidth=0.75, relheight=0.27, anchor="center")

        self._botao_salvar_no_banco = Button(newWindow, text=" Salvar no Banco    ", font=("verdana", 12, 'bold'), bd=5, image=self._imagem_salvar,
        compound="right", bg = "#34dfc9", fg="black")
        self._botao_salvar_no_banco.place(relx=0.5, rely=0.70, relwidth=0.75, relheight=0.27 , anchor="center")

        newWindow.grid()
        newWindow.transient(self._root)
        newWindow.focus_force()
        newWindow.grab_set()

    def widgets_frame1(self):
        #BOTAO GERAR QR
        self._botao_limpar = Button(self._frame_1, text="Gerar QR", font=("verdana", 14, 'bold'), bd=5,bg = "#4e8ff3",
        fg="black")
        self._botao_limpar.place(relx=0.2, rely=0.95, relwidth=0.18, relheight=0.09 , anchor="center")
        
        #BOTAO SALVAR
        self._botao_limpar = Button(self._frame_1, text="Salvar   ", font=("verdana", 14, 'bold'), bd=5, image=self._imagem_salvar,
        compound="right", bg = "#22f40b", fg="black", command=self.tela_salvar_qr)
        self._botao_limpar.place(relx=0.4, rely=0.95, relwidth=0.18, relheight=0.09 , anchor="center")

        #BOTAO CARREGAR BANCO
        self._botao_limpar = Button(self._frame_1, text="Banco  ", font=("verdana", 14, 'bold'), bd=5, image=self._imagem_storage,
        compound="right", bg = "#cece5a", fg="black")
        self._botao_limpar.place(relx=0.6, rely=0.95, relwidth=0.18, relheight=0.09 , anchor="center")

        #BOTAO LIMPAR   
        self._botao_limpar = Button(self._frame_1, text="Limpar  ", font=("verdana", 14, 'bold'), bd=5, image=self._imagem_lixeira,
        compound="right", bg = "#df5434", fg="black", command=self.limpa_tela)
        self._botao_limpar.place(relx=0.8, rely=0.95, relwidth=0.18, relheight=0.09 , anchor="center")

        #label
        self._valor_qr = Entry(self._frame_1, font=("verdana", 18))
        self._valor_qr.insert(-1, '')
        self._valor_qr.place(relx=0.5, rely=0.85, relwidth=0.66, relheight=0.06 , anchor="center") 

        #pegar diretorio para salvar a imagem qr
        # folder_path = filedialog.askdirectory()
        # print(folder_path)

Aplicacao(root)