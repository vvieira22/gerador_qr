from tkinter import END
from datetime import datetime
from pytz import timezone

#Tools and Helpers.

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
    
    def pegar_data_e_hora(self):
        #necessita do pacote pytz, é mais preciso e "adptável".
        #ok, era pra ser rj, só dessa vez eu deixo sp =)
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone("America/Sao_Paulo")
        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
        
        return data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M:%S')

   
# https://stackoverflow.com/questions/60413086/lock-a-main-tkinter-window-in-python-and-keep-the-x-button-running
# https://stackoverflow.com/questions/39689046/tkinter-only-allow-one-toplevel-window-instance

#TODO: DESATIVAR TODAS OS WIDGETS QUANDO ABRIR A JANELA PARA EVITAR USAR O FOCO FORÇADO.