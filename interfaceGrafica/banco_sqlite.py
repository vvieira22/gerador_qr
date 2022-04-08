import os
import sqlite3

class bancoDadosQR():
    def __init__(self):
        self._lista_cod_qr = []
        self._lista_valor_qrs = []
        os.chdir(os.path.dirname(__file__))
        self.diretorio_bd = os.getcwd()+"\\"+"lista_qrs.db"

        if(os.path.exists(self.diretorio_bd)):
            print("banco, já criado")            
        else:
            self.conectar_banco()
        self.criar_tabela() #vai tentar criar mesmo já tendo a tabela, para garantir que nunca falte

    def conectar_banco(self):
        self.conn = sqlite3.connect("lista_qrs.db")
        self.cursor = self.conn.cursor()

    def desconectar_banco(self):
        self.conn.close()

    def criar_tabela(self):
        self.conectar_banco() #se conecta ao banco
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS qrs (
            codigo INTERGER PRIMARY KEY,
            data_geracao CHAR(30) NOT NULL, 
            conteudo_qr CHAR(150)
            );
        """)    
        self.conn.commit()
        self.desconectar_banco()
        
    def inserir_qr_no_banco(self, codigo, conteudo_qr, hora_qr):
        self.codigo = codigo
        self.conteudo_qr = conteudo_qr
        self.hora_qr = hora_qr

        self.conectar_banco()
        self.cursor.execute(""" INSERT INTO qrs (codigo, data_geracao, conteudo_qr)
            VALUES (?, ?, ?)""", (self.codigo, self.conteudo_qr, self.hora_qr))
        self.conn.commit()
        self.desconectar_banco()

    def retornar_lista_qrs(self):
        self.conectar_banco()

        lista = self.cursor.execute(""" SELECT * FROM qrs
            ORDER BY codigo; """)
        lista_qrs = []
        for registro in lista:
            lista_qrs.append(registro)
        self.desconectar_banco()
        return lista_qrs
