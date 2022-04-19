from pickle import FALSE
from tkinter import Button, Toplevel, filedialog
from helpers import Configuracoes

class JanelaOndeSalvarQR():
    def tela_salvar_qr(self, janela_mae, imagem, cadastrar_qr_no_banco, salvar_qr_como_imagem):
        self._janela_salvar_qr = Toplevel(janela_mae)        
        Configuracoes().configuracoes_abertura(self._janela_salvar_qr, 400,250,400,350,400,350, "Como deseja salvar o QR?", False, False)
        self.widgets_frame2(imagem, cadastrar_qr_no_banco, salvar_qr_como_imagem)

        self._janela_salvar_qr.transient(janela_mae)
        
    def widgets_frame2(self, imagem, cadastrar_qr_no_banco, salvar_qr_como_imagem):
        self._botao_salvar_arquivo = Button(self._janela_salvar_qr, text=" Salvar em Arquivo    ", font=("verdana", 12, 'bold'), bd=5, image=imagem,
        compound="right", bg = "#75a7a1", fg="black", command = salvar_qr_como_imagem)
        self._botao_salvar_arquivo.place(relx=0.5, rely=0.30, relwidth=0.75, relheight=0.27, anchor="center")

        self._botao_salvar_no_banco = Button(self._janela_salvar_qr, text=" Salvar no Banco    ", font=("verdana", 12, 'bold'), bd=5, image=imagem,
        compound="right", bg = "#34dfc9", fg="black", command = cadastrar_qr_no_banco)
        self._botao_salvar_no_banco.place(relx=0.5, rely=0.70, relwidth=0.75, relheight=0.27 , anchor="center")
    
    def limpar_janela(self):
        self._janela_salvar_qr.grab_release()
        self._janela_salvar_qr.destroy()
        self._janela_salvar_qr.update()
        