from logging import root
from tkinter import E, END, Frame, Scrollbar, Toplevel, ttk
from configuroes import Configuracoes

class TelaBancoDeQrs():
    def tela_qrs_do_banco(self, frame_mae):
        self._janela_banco_qr = Toplevel(frame_mae)
        Configuracoes().configuracoes_abertura(self._janela_banco_qr, 900, 450, 900, 450, 900, 450, "Lista de QRS Cadastrados", False, False, "#495866")
        
        #configuracoes de foco, ainda em teste
        self._janela_banco_qr.grid()
        self._janela_banco_qr.transient(frame_mae)
        self._janela_banco_qr.focus_force()
        self._janela_banco_qr.grab_set()

        self._frame_teste = Frame(self._janela_banco_qr, bd=4, bg="#1f1f25", highlightthickness=7,
        highlightbackground = "#2b4361", highlightcolor= "#2b4361")
        self._frame_teste.place(relx=0.02, rely=0.02, relwidth=0.80, relheight=0.96)
        self.widgets_tela_qrs_do_banco()

    def widgets_tela_qrs_do_banco(self):
        #estilização pra ficar maroto e legal!
        # style=ttk.Style(root)
        # style.theme_use('clam')

        #tabela de qrs
        self._tabela_qrs = ttk.Treeview(self._frame_teste, height=3, columns=("coluna1, coluna3, coluna3"))
        self._tabela_qrs.heading("#0", text="")
        self._tabela_qrs.heading("#1", text="Código")
        self._tabela_qrs.heading("#2", text="Conteúdo")
        self._tabela_qrs.heading("#3", text="Data")

        self._tabela_qrs.column("#0", width=0)
        self._tabela_qrs.column("#1", width=5)
        self._tabela_qrs.column("#2", width=320)
        self._tabela_qrs.column("#3", width=110)
        self._tabela_qrs.place(relx=0.01, rely=0.00, relwidth=1, relheight= 1)

        #barra de rolagem
        self.barra_rolagem = Scrollbar(self._frame_teste)
        self._tabela_qrs.configure(yscroll = self.barra_rolagem.set)
        self.barra_rolagem.place(relx=0.98, rely=0.001, relwidth=0.03, relheight=1)
        
    def inserir_lista_qrs_na_tabela(self, lista_qrs):
        self._tabela_qrs.delete(*self._tabela_qrs.get_children())

        for registro in lista_qrs:
            self._tabela_qrs.insert("", END, values=registro)