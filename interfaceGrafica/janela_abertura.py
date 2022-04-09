from tkinter import Button, Entry, Frame
from configuroes import Configuracoes

#FRAME 1 (Janela de Abertura
class JanelaAbertura():
    def tela_inicial_qr(self, *args):
        self._frame_1 = Frame(args[0], bd=4, bg="#495866", highlightthickness=7,
        highlightbackground = "black", highlightcolor= "black")
        self.configs_tela_ini_qr = Configuracoes().configuracoes_abertura(args[0], 1000,800,1920,1080,1000,800,"Gerador de QR code", True, True)
        self._frame_1.grid()
        self._frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.widgets_frame1(*args)

    def widgets_frame1(self,*args):
        #BOTAO GERAR QR
        # TODO: gerar o qr
        self._botao_gerar_qr = Button(self._frame_1, text="Gerar QR", font=("verdana", 14, 'bold'), bd=5,bg = "#4e8ff3",
        fg="black")
        self._botao_gerar_qr.place(relx=0.2, rely=0.95, relwidth=0.18, relheight=0.09 , anchor="center")
        
        #BOTAO SALVAR
        self._botao_salvar_qr = Button(self._frame_1, text="Salvar   ", font=("verdana", 14, 'bold'), bd=5, image=args[4],
        compound="right", bg = "#22f40b", fg="black", command= args[1])
        self._botao_salvar_qr.place(relx=0.4, rely=0.95, relwidth=0.18, relheight=0.09 , anchor="center")

        #BOTAO CARREGAR BANCO
        #chamar lambda no comando quando funções precisarem de parametros ou usarem () para serem chamadas.
        self._botao_abrir_banco = Button(self._frame_1, text="Banco  ", font=("verdana", 14, 'bold'), bd=5, image=args[5],
        compound="right", bg = "#cece5a", fg="black", command=args[2])
        self._botao_abrir_banco.place(relx=0.6, rely=0.95, relwidth=0.18, relheight=0.09 , anchor="center")

        #LABEL QR
        self._valor_qr = Entry(self._frame_1, font=("verdana", 18))
        self._valor_qr.insert(-1, '')
        self._valor_qr.place(relx=0.5, rely=0.85, relwidth=0.66, relheight=0.06 , anchor="center")

        #BOTAO LIMPAR   
        self._botao_limpar = Button(self._frame_1, text="Limpar  ", font=("verdana", 14, 'bold'), bd=5, image=args[6],
        compound="right", bg = "#df5434", fg="black", command= args[3])
        self._botao_limpar.place(relx=0.8, rely=0.95, relwidth=0.18, relheight=0.09 , anchor="center")

        #pegar diretorio para salvar a imagem qr
        # folder_path = filedialog.askdirectory()
        # print(folder_path)