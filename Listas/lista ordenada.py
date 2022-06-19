# Lista simplesmente encadeada e ordenada
    # Exemplo
class No:
    def __init__(self):
        self.__numInteiro = 0
        self.__prox = None
    def setNum(self, n):
        self.__numInteiro = n
    def getNum(self):
        return self.__numInteiro
    def getProx(self):
        return self.__prox
    def setProx(self, prox):
        self.__prox = prox

class Lista:
    def __init__(self):
        self.__ini = None
        self.__fim = None

    def push(self):
        Temp = No()
        if Temp:
            Temp.setNum(int(input("Digite um número: ")))
            # Primeiro
            if not self.__ini:
                Temp.setProx(None)
                self.__ini = self.__fim = Temp
            elif Temp.getNum() <= self.__ini.getNum():    # insere no inicio
                Temp.setProx(self.__ini)
                self.__ini = Temp
            elif Temp.getNum() >= self.__fim.getNum():    # insere no final
                self.__fim.setProx(Temp)
                self.__fim = Temp
                Temp.setProx(None)
            else:
                pant = self.__ini
                while True:
                    if Temp.getNum() <= pant.getProx().getNum():  # no meio
                        Temp.setProx(pant.getProx())
                        pant.setProx(Temp)
                        break
                    pant = pant.getProx()

    def pop(self):
        if not self.__fim:
            print("Lista Vazia!")
            return
        self.print_all()
        x = int(input("Deseja excluir qual elemento? "))
        temp = self.__ini
        if temp.getNum() == x:
            self.__ini = self.__ini.getProx()
            if not self.__ini:
                self.__fim = None
            return
        while temp.getProx():
            if temp.getProx().getNum() == x:
                temp.setProx(temp.getProx().getProx())
                if not temp.getProx():
                    self.__fim = temp
                break
            temp = temp.getProx()

    def pop_all(self):
        if not self.__ini:
            print("Lista Vazia!")
            return
        self.__ini = self.__fim = None
        print("Todos os itens da lista removidos!")

    def print_all(self):
        if not self.__ini:
            print("Lista Vazia!")
            return
        saida = ""
        temp_no = self.__ini
        while temp_no:
            saida += "[" + str(temp_no.getNum()) + "] "
            temp_no = temp_no.getProx()
        print(saida)

objetoLista = Lista()
while True:
    print("[1] - Inserir um elemento na lista")
    print("[3] - Excluir um elemento qualquer da lista")
    print("[4] - Excluir todos os elementos da lista")
    print("[5] - Imprimir a lista inteira")
    print("[6] - Sair")
    op = int(input("Digite uma opção do menu acima: "))
    if op == 1:
        objetoLista.push()
    if op == 3:
        objetoLista.pop()
    if op == 4:
        objetoLista.pop_all()
    if op == 5:
        objetoLista.print_all()
    if op == 6:
        break
    else:
        print("Opção digitada inválida")