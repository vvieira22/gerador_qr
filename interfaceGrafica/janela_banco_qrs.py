from cgitb import text
from difflib import context_diff
from logging import root
from tkinter import E, END, Button, Entry, Frame, Label, Scrollbar, Toplevel, ttk
import tkinter
from helpers import Configuracoes

class TelaBancoDeQrs():
    def tela_qrs_do_banco(self, frame_mae, banco_qr, carregar_qr_do_banco):
        self._frame_mae = frame_mae
        self._banco_qr = banco_qr
        self._carregar_qr_do_banco = carregar_qr_do_banco
        self._janela_banco_qr = Toplevel(frame_mae)
        Configuracoes().configuracoes_abertura(self._janela_banco_qr, 900, 450, 900, 450, 900, 450, "Lista de QRS Cadastrados", False, False, "#495866")

        self._janela_banco_qr.transient(frame_mae)
        self._janela_banco_qr.focus_force()
        
        self._frame_janela_banco_qrs = Frame(self._janela_banco_qr, bd=4, bg="#1f1f25", highlightthickness=7,
        highlightbackground = "#2b4361", highlightcolor= "#2b4361")
        self._frame_janela_banco_qrs.place(relx=0.02, rely=0.02, relwidth=0.80, relheight=0.96)
        self.widgets_tela_qrs_do_banco()

    def widgets_tela_qrs_do_banco(self):
        #estilização pra ficar maroto e legal!
        # style=ttk.Style(root)
        # style.theme_use('clam')

        #tabela de qrs
        self._tabela_qrs = ttk.Treeview(self._frame_janela_banco_qrs, height=3, columns=("coluna1, coluna3, coluna3"))
        self._tabela_qrs.heading("#0", text="")
        self._tabela_qrs.heading("#1", text="Código")
        self._tabela_qrs.heading("#2", text="Data")
        self._tabela_qrs.heading("#3", text="Conteúdo")

        self._tabela_qrs.column("#0", width=0)
        self._tabela_qrs.column("#1", width=5)
        self._tabela_qrs.column("#2", width=110)
        self._tabela_qrs.column("#3", width=320)
        self._tabela_qrs.place(relx=0, rely=0.00, relwidth=1, relheight= 1)

        self._tabela_qrs.bind("<Double-1>", self.click_duplo_tabela)

        #barra de rolagem
        self.barra_rolagem = Scrollbar(self._frame_janela_banco_qrs)
        self._tabela_qrs.configure(yscroll = self.barra_rolagem.set)
        self.barra_rolagem.place(relx=0.98, rely=0.001, relwidth=0.03, relheight=1)
        
        #CÓDIGO
        self._lb_codigo = Label(self._janela_banco_qr, text = "Código", bg = '#dfe3ee', fg = '#107db2')
        self._lb_codigo.place(relx = 0.9, rely = 0.09, relwidth = 0.07, relheight = 0.1, anchor = "center")

        self._entry_codigo = Label(self._janela_banco_qr, font=("verdana", 12))
        self._entry_codigo.place(relx = 0.9, rely = 0.19, relwidth = 0.05, relheight = 0.06, anchor = "center")

        #Conteúdo
        self._lb_conteudo = Label(self._janela_banco_qr, text = "Conteúdo", bg = '#dfe3ee', fg = '#107db2')
        self._lb_conteudo.place(relx = 0.9, rely = 0.29, relwidth = 0.07, relheight = 0.1, anchor = "center")

        self._entry_conteudo = Entry(self._janela_banco_qr, font=("verdana", 10))
        self._entry_conteudo.insert(-1, '')
        self._entry_conteudo.place(relx = 0.91, rely = 0.39, relwidth = 0.18, relheight = 0.06, anchor = "center")

        #Hora
        self._lb_data = Label(self._janela_banco_qr, text = "Data", bg = '#dfe3ee', fg = '#107db2')
        self._lb_data.place(relx = 0.9, rely = 0.49, relwidth = 0.07, relheight = 0.1, anchor = "center")

        self._entry_data = Entry(self._janela_banco_qr, font=("verdana", 10))
        self._entry_data.insert(-1, '')
        self._entry_data.place(relx = 0.91, rely = 0.59, relwidth = 0.18, relheight = 0.06, anchor = "center")

        #BOTAO ATUALIZAR
        self._botao_atualizar = Button(self._janela_banco_qr, text="Atualizar  ", font=("verdana", 10, 'bold'), bd=5,
        compound="right", bg = "#21b4ea", fg="black", command= self.atualizar_qr_do_banco)
        self._botao_atualizar.place(relx = 0.91, rely = 0.69, relwidth = 0.18, relheight = 0.1, anchor = "center")

        #BOTAO EXCLUIR
        self._botao_excluir = Button(self._janela_banco_qr, text="Excluir  ", font=("verdana", 10, 'bold'), bd=5,
        compound="right", bg = "#ea2121", fg="black", command= self.excluir_qr_do_banco)
        self._botao_excluir.place(relx = 0.91, rely = 0.81, relwidth = 0.18, relheight = 0.1, anchor = "center")

        #BOTAO CARREGAR
        self._botao_excluir = Button(self._janela_banco_qr, text="Carregar  ", font=("verdana", 10, 'bold'), bd=5,
        compound="right", bg = "#76ec7b", fg="black", command= self.carregar_qr_para_memoria)
        self._botao_excluir.place(relx = 0.91, rely = 0.925, relwidth = 0.18, relheight = 0.1, anchor = "center")

    def inserir_lista_qrs_na_tabela(self, lista_qrs):
        self._tabela_qrs.delete(*self._tabela_qrs.get_children())

        for registro in lista_qrs:
            self._tabela_qrs.insert("", END, values=registro)
    
    def limpar_campos(self):
        self._entry_codigo.config(text="")
        self._entry_conteudo.delete(0, 'end')
        self._entry_data.delete(0, 'end')

    def click_duplo_tabela(self, event):
        self.limpar_campos()

        for n in self._tabela_qrs.selection():
            col1, col2, col3 = self._tabela_qrs.item(n, 'values')
            self._entry_codigo.config(text=col1)
            self._entry_data.insert(END, col2)
            self._entry_conteudo.insert(END, col3)
        
    def excluir_qr_do_banco(self):
        try:
            codigo = int(self._entry_codigo['text'])
            for qr in self._banco_qr._lista_qrs:
                if (int(qr[0]) == codigo):
                    if (self._banco_qr.excluir_qr(codigo)):
                        self.limpar_campos()
                        tkinter.messagebox.showinfo(title="Sucesso!", message="Qr removido com sucesso!", parent=self._frame_janela_banco_qrs)
                        tabela_atualizada = self._banco_qr.retornar_lista_qrs()
                        self.inserir_lista_qrs_na_tabela(tabela_atualizada)
                        return None
                    self.limpar_campos()
                    tkinter.messagebox.showerror(title="Um erro ocorreu!", message="Qr não removido!", parent=self._frame_janela_banco_qrs)
                    return None
        except:
            self.limpar_campos()
            tkinter.messagebox.showerror(title="QR não selecionado", message="Por Favor selecione um registro\ncom duplo clique.", parent=self._frame_janela_banco_qrs)
    
    def atualizar_qr_do_banco(self):
        try:
            codigo = int(self._entry_codigo['text'])
            for qr in self._banco_qr._lista_qrs:
                if (int(qr[0]) == codigo):
                    conteudo_novo = self._entry_conteudo.get()
                    data_nova = self._entry_data.get()

                    if(qr[1] == data_nova and qr[2] == conteudo_novo):
                        tkinter.messagebox.showerror(title="Um erro ocorreu!", message="Para realizar a alteração\n altere algo!", parent=self._frame_janela_banco_qrs)
                        return None
                    else:
                        if (self._banco_qr.atualizar_qr(codigo, data_nova, conteudo_novo)):
                            self.limpar_campos()
                            tkinter.messagebox.showinfo(title="Sucesso!", message="Qr atualizado com sucesso!", parent=self._frame_janela_banco_qrs)
                            tabela_atualizada = self._banco_qr.retornar_lista_qrs()
                            self.inserir_lista_qrs_na_tabela(tabela_atualizada)
                            return None
                        self.limpar_campos()
                        tkinter.messagebox.showerror(title="Um erro ocorreu!", message="Qr não atualizado!", parent=self._frame_janela_banco_qrs)
                        return None
        except:
            self.limpar_campos()
            tkinter.messagebox.showerror(title="QR não selecionado", message="Por Favor selecione um registro\ncom duplo clique.", parent=self._frame_janela_banco_qrs)
    
    def carregar_qr_para_memoria(self):
        try:
            codigo = int(self._entry_codigo['text'])
            for qr in self._banco_qr._lista_qrs:
                if (int(qr[0]) == codigo):
                    conteudo = self._entry_conteudo.get()
                    self._carregar_qr_do_banco(conteudo)
                    tkinter.messagebox.showinfo(title="Sucesso!", message="Qr carregado", parent=self._frame_janela_banco_qrs)
                    self._janela_banco_qr.grab_release()
                    self._janela_banco_qr.destroy()
                    self._janela_banco_qr.update()
        except:
            tkinter.messagebox.showerror(title="QR não selecionado", message="Por Favor selecione um registro\ncom duplo clique.", parent=self._frame_janela_banco_qrs)