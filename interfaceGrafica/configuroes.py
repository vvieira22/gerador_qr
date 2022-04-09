from tkinter import END

class Configuracoes():
    def configuracoes_abertura(self, janela, largura, altura, max_l, max_a, min_l, min_a, nome_janela, redimencional, movel, background = None):
        janela.title(nome_janela) #texto barra superior
        
        if(background==None):
            janela.configure(background="#f6f5ef")#cor background
        else:
            janela.configure(background=background)#cor background
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

    def limpar_label(self, label):
        label.delete(0, END)