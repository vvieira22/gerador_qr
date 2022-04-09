from ctypes import alignment
import os
from tkinter import *
from tkinter import ttk
from turtle import back
from banco_sqlite import bancoDadosQR
from tkinter import filedialog
import tkinter
from configuroes import Configuracoes
from janela_abertura import JanelaAbertura
from janela_onde_salvar_qr import JanelaOndeSalvarQR
from janela_banco_qrs import TelaBancoDeQrs

class Aplicacao(Configuracoes):
    def __init__(self, root):
        self._root = root 
        self.configs_iniciais()
        root.mainloop()

    def configs_iniciais(self):
        self._banco = bancoDadosQR()
        self._banco.retornar_lista_qrs()
        self.carregar_imagem()
        Configuracoes().configuracoes_abertura(self._root, 1000,800,1920,1080,1000,800,"Gerador de QR code", True, True)
        self.janelas_aplicacao()
        # self.tela_inicial_qr()

    def chamar_janela_onde_salvar(self):
        self._janela_onde_salvar_qr = JanelaOndeSalvarQR()
        self._janela_onde_salvar_qr.tela_salvar_qr(self._root, self._imagem_salvar,
        self.cadastrar_qr_no_banco)

    def janelas_aplicacao(self):
        #JANELA ABERTURA
        self._janela_abertura = JanelaAbertura()

        parametros_janela_abertura = [self._root, self.chamar_janela_onde_salvar, 
        lambda : self.chamar_outra_janela("bancoQr"), lambda : self.limpar_label(self._janela_abertura._valor_qr), 
        self._imagem_salvar, self._imagem_storage, self._imagem_lixeira]
       
        self._janela_abertura.tela_inicial_qr(*parametros_janela_abertura)

        self._janela_banco_qrs = TelaBancoDeQrs()
    
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

    def gerar_codigo_qr(self):
        lista_qrs = self._banco.retornar_lista_qrs()
        lista_indices = []
        for registro in lista_qrs:
            lista_indices.append(registro[0])
        if(not lista_indices):
            return 1
        return max(lista_indices)+1
    
    def cadastrar_qr_no_banco(self):
        valor_qr = self._janela_abertura._valor_qr.get()
        if(valor_qr == ""):
            tkinter.messagebox.showerror(title="Erro!", message="QR vazio!!")
        else:
            codigo_qr = self.gerar_codigo_qr()
            valor_qr = self._janela_abertura._valor_qr.get()
            # hora_qr = self._hora_ultimo_qr()
            try:
                self._banco.inserir_qr_no_banco(codigo_qr, valor_qr, "horamaisnafrente")
                tkinter.messagebox.showerror(title="Sucesso!", message="Cadastro realizado com sucesso!")
                self.limpar_label(self._janela_abertura._valor_qr)
            except:
                tkinter.messagebox.showerror(title="Ocorreu um erro", message="Erro ao cadastrar, tente novamente.")
        self._janela_onde_salvar_qr.limpar_janela()
    
    def chamar_outra_janela(self, nomeJanela):
        if(nomeJanela=="bancoQr"):
            self._janela_banco_qrs.tela_qrs_do_banco(self._root)
            self._janela_banco_qrs.inserir_lista_qrs_na_tabela(self._banco.retornar_lista_qrs())
        else:
            print("em andamento rs")

root = Tk()
Aplicacao(root)
