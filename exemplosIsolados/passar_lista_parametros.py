class mae():
    def __init__(self):
        self._filho = Filho()
        self.funcao_geral()
    def funcao1(self):
        print("funcao1")
    def funcao2(self):
        print("funcao2")
    def funcao3(self):
        print("funcao3")
    def funcao_geral(self):
        lista = [self.funcao1, self.funcao2, self.funcao3]
        self._filho.chamar_todo_mundo(*lista)

class Filho():
    def chamar_todo_mundo(self, *args):
        args[0]()
        args[1]()
        args[2]()
teste = mae()