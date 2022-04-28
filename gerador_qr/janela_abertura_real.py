import os
from tkinter import Button, Entry, Frame, Label, Tk
import tkinter
from helpers import Configuracoes
from PIL import Image, ImageTk

class JanelaAberturaReal():
    def __init__(self, root):
        largura = 1000
        altura = 800
        maximo_largura = 1920
        maximo_altura = 1080
        minimo_largura = 1000
        minimo_altura = 800
        redimencionavel = True
        movel = True 
        background = None
        
        Configuracoes().configuracoes_abertura(root, largura, altura, maximo_largura,
         maximo_altura, minimo_largura, minimo_altura,"Gerador de QR code", redimencionavel, movel, background)

    #TODO: ACERTAR O NOME DA CADA FRAME CORRETAMENTE PARA FAZER SENTIDO.
    def tela_inicial_qr(self, *args):
        self._frame_1 = Frame(args[0], bd=4, bg="#495866", highlightthickness=7,
        highlightbackground = "black", highlightcolor= "black")
        self.configs_tela_ini_qr = Configuracoes().configuracoes_abertura(args[0], 1000,800,1920,1080,1000,800,"Gerador de QR code", True, False)
        self._frame_1.grid()
        self._frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.widgets_janela_abertura(*args)

    def widgets_janela_abertura(self,*args):
        #BOTAO GERAR QR
        self._botao_gerar_qr = Button(self._frame_1, text = "Gerar QR", font = ("verdana", 14, 'bold'), bd = 5, bg = "#4e8ff3",
        fg = "black", command = args[7])
        self._botao_gerar_qr.place(relx=0.2, rely=0.95, relwidth=0.18, relheight=0.09 , anchor="center")
        
        #BOTAO SALVAR
        self._botao_salvar_qr = Button(self._frame_1, text ="Salvar   ", font = ("verdana", 14, 'bold'), bd = 5, image = args[4],
        compound = "right", bg = "#22f40b", fg = "black", command = args[1])
        self._botao_salvar_qr.place(relx = 0.4, rely = 0.95, relwidth = 0.18, relheight = 0.09 , anchor = "center")

        #BOTAO CARREGAR BANCO
        #chamar lambda no comando quando funções precisarem de parametros ou usarem () para serem chamadas.
        self._botao_abrir_banco = Button(self._frame_1, text="Banco  ", font=("verdana", 14, 'bold'), bd = 5, image = args[5],
        compound = "right", bg = "#cece5a", fg="black", command = args[2])
        self._botao_abrir_banco.place(relx=0.6, rely=0.95, relwidth=0.18, relheight=0.09 , anchor="center")

        #LABEL QR
        self._valor_qr = Entry(self._frame_1, font = ("verdana", 18))
        self._valor_qr.insert(-1, '')
        self._valor_qr.place(relx = 0.5, rely=0.85, relwidth = 0.66, relheight = 0.06 , anchor = "center")

        #BOTAO LIMPAR   
        self._botao_limpar = Button(self._frame_1, text="Limpar  ", font = ("verdana", 14, 'bold'), bd=5, image = args[6],
        compound = "right", bg = "#df5434", fg = "black", command = args[3])
        self._botao_limpar.place(relx = 0.8, rely = 0.95, relwidth = 0.18, relheight = 0.09 , anchor = "center")

    def mudar_status_janela(self, status):
        for widget in self._frame_1.winfo_children():
            widget.configure(state = status)
    
    def limpar_janela(self):
        self._frame_1.grab_release()
        self._frame_1.destroy()
        self._frame_1.update()
    
    def gerar_frame_qr(self):
        try:
            conteudo_qr = self._janela_abertura._valor_qr.get()
            
            if(conteudo_qr == ""):
                raise ValueError("QR vazio!")
            else: #GERAÇÃO DO QR EM CÓDIGO
                self._gerador_qr.gerar_qr_temporario(conteudo_qr)
                self._hora_ultimo_qr_gerado = self.pegar_data_e_hora()

            #GERAÇÃO DO QR NA TELA.
            scriptpath = os.path.abspath(__file__)
            scriptdir = os.path.dirname(scriptpath)
            imagepath = os.path.join(scriptdir, "imagens/" + "qr_temp.png")

            IMAGE_PATH = imagepath
            WIDTH, HEIGHT = 400, 400

            try:
                if(self.lbl.winfo_exists()):
                    self.limpar_entry_qr()
            except:
                pass

            img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT)))
            self.lbl = Label(self._root, image = img)
            self.lbl.place(relx = 0.5, rely = 0.65, anchor = 's')

        except ValueError as e:
            tkinter.messagebox.showerror(title="Um erro ocorreu!", message = e, parent = self._root)