from ast import Raise
from ctypes import alignment
import os
from time import time
from tkinter import *
from tkinter import ttk
from turtle import back
from banco_sqlite import bancoDadosQR
from tkinter import filedialog
import tkinter
from helpers import Configuracoes
from janela_abertura import JanelaAbertura
from janela_onde_salvar_qr import JanelaOndeSalvarQR
from janela_banco_qrs import TelaBancoDeQrs
from PIL import Image, ImageTk
from gerador_qr import QR

class Aplicacao(Configuracoes):
    def __init__(self, root):
        self._root = root 
        self.configs_iniciais()
        root.mainloop()

    def configs_iniciais(self):
        self._hora_ultimo_qr_gerado = ""
        self._banco = bancoDadosQR()
        self._gerador_qr = QR()
        self._banco.retornar_lista_qrs()
        self.carregar_imagem()
        Configuracoes().configuracoes_abertura(self._root, 1000, 800, 1920, 1080, 1000, 800,"Gerador de QR code", True, True)
        self.janelas_aplicacao()

    def chamar_janela_onde_salvar(self):
        self._janela_onde_salvar_qr = JanelaOndeSalvarQR()
        try:
            self.mudar_status_widgets_main("disabled")
            self._janela_onde_salvar_qr.tela_salvar_qr(self._root, self._imagem_salvar,
            self.cadastrar_qr_no_banco, self.salvar_qr_arquivo)
            self._root.wait_window(self._janela_onde_salvar_qr._janela_salvar_qr)
        finally:
            self.mudar_status_widgets_main("normal")
   
    def janelas_aplicacao(self):
        #JANELA ABERTURA
        self._janela_abertura = JanelaAbertura()

        parametros_janela_abertura = [self._root, self.chamar_janela_onde_salvar, 
        lambda : self.chamar_outra_janela("bancoQr"), lambda : self.limpar_qr_gerado(), 
        self._imagem_salvar, self._imagem_storage, self._imagem_lixeira, lambda : self.gerar_frame_qr()]
       
        self._janela_abertura.tela_inicial_qr(*parametros_janela_abertura)

        self._janela_banco_qrs = TelaBancoDeQrs()
    
    def limpar_qr_gerado(self):
        self.limpar_label(self._janela_abertura._valor_qr)
        self.lbl.destroy()

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
        hora_qr = self._hora_ultimo_qr_gerado
        
        if(valor_qr == ""):
            tkinter.messagebox.showerror(title="Erro!", message="QR vazio!!", parent = self._janela_onde_salvar_qr._janela_salvar_qr)
        elif(hora_qr == ""):
            tkinter.messagebox.showerror(title="Erro!", message="QR não gerado!", parent = self._janela_onde_salvar_qr._janela_salvar_qr)        
        else:
            codigo_qr = self.gerar_codigo_qr()
            try:
                self._banco.inserir_qr_no_banco(codigo_qr, valor_qr, hora_qr)
                tkinter.messagebox.showerror(title = "Sucesso!", message = "Cadastro realizado com sucesso!", parent = self._janela_onde_salvar_qr._janela_salvar_qr)
            except:
                    tkinter.messagebox.showerror(title = "Ocorreu um erro", message="Erro ao cadastrar, tente novamente.", parent = self._janela_onde_salvar_qr._janela_salvar_qr)
        self._janela_onde_salvar_qr.limpar_janela()
    
    def salvar_qr_arquivo(self):
        valor_qr = self._janela_abertura._valor_qr.get()
        hora_qr = self._hora_ultimo_qr_gerado

        if(valor_qr == ""):
            tkinter.messagebox.showerror(title="Erro!", message="QR vazio!!", parent = self._janela_onde_salvar_qr._janela_salvar_qr)
        elif(hora_qr == ""):
            tkinter.messagebox.showerror(title="Erro!", message="QR não gerado!", parent = self._janela_onde_salvar_qr._janela_salvar_qr)    
        else:
            try:
                data = [('png', '*.png')]
                imagem = self._gerador_qr.retornar_qr_temp()
                file = filedialog.asksaveasfile(mode="wb", filetypes=data, defaultextension=".png", initialfile = "gerador_qr")
                print(file)
                if(file):
                    imagem.save(file)
                print(file)
            except Exception as e:
                print(e)
        self._janela_onde_salvar_qr.limpar_janela()                
    def chamar_outra_janela(self, nomeJanela):
        if(nomeJanela=="bancoQr"):
            try:
                self.mudar_status_widgets_main("disabled")
                self._janela_banco_qrs.tela_qrs_do_banco(self._root, self._banco, self.carregar_qr_do_banco)
                self._janela_banco_qrs.inserir_lista_qrs_na_tabela(self._banco.retornar_lista_qrs())
                self._root.wait_window(self._janela_banco_qrs._janela_banco_qr)
            finally:
                self.mudar_status_widgets_main("normal")
        else:
            print("em andamento rs")

    def limpar_entry_qr(self):
        self.lbl.destroy()
        self._hora_ultimo_qr_gerado = ""

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
    
    def mudar_status_widgets_main(self, status):
        self._janela_abertura.mudar_status_janela(status)
    
    def carregar_qr_do_banco(self, conteudo):
        try:
            self.mudar_status_widgets_main("normal")
            self._janela_abertura._valor_qr.delete(0, END)
            self._janela_abertura._valor_qr.insert(0, conteudo)
            self.mudar_status_widgets_main("disabled")
            self.gerar_frame_qr()
        except:
            tkinter.messagebox.showerror(title="Um erro ocorreu!", message="Qr carregado!", parent=self._root)

root = Tk()
Aplicacao(root)