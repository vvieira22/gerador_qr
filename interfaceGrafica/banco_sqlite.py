from ast import Raise
import os
import sqlite3
from tkinter import E

class bancoDadosQR():
    def __init__(self):
        os.chdir(os.path.dirname(__file__))
        self.diretorio_bd = os.getcwd()+"\\"+"lista_qrs.db"

        if(os.path.exists(self.diretorio_bd)):
            print("banco, já criado")            
        else:
            self.conectar_banco()
        self.criar_tabela() #vai tentar criar mesmo já tendo a tabela, para garantir que nunca falte
        self._lista_qrs = self.retornar_lista_qrs()

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
            VALUES (?, ?, ?)""", (self.codigo, self.hora_qr ,self.conteudo_qr))
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
        self._lista_qrs = lista_qrs
        return lista_qrs
    
    def excluir_qr(self, id):
        try:
            self.conectar_banco()
            
            self.cursor.execute("""DELETE from qrs where codigo = ?""", (int(id),))
            linhas_afetadas = self.cursor.rowcount
            self.conn.commit()
           
            self.desconectar_banco()

            return True if linhas_afetadas > 0 else False
        except sqlite3.Error as error:
            Exception("error to delete record from a sqlite table", error)
            self.desconectar_banco()

            return False
        '''exception nao esta funcionando, delete nao retorna 
        nada se nao conseguir, precisa verificar pelas linhas afetadas.'''
    def atualizar_qr(self, id, data_nova, conteudo_novo):
        try:
            self.conectar_banco()

            self.cursor.execute("""UPDATE qrs SET data_geracao = ?, conteudo_qr = ?
            WHERE codigo = ? """, (data_nova, conteudo_novo, id))
            linhas_afetadas = self.cursor.rowcount
            self.conn.commit()

            self.desconectar_banco()

            return True if linhas_afetadas > 0 else False

        except sqlite3.Error as error:
            Exception("error to update record from a sqlite table", error)
            self.desconectar_banco()
            return False