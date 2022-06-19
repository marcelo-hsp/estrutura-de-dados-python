# 01) Construa um programa que insere nomes em uma fila, imprimindo a
# fila completa a cada inserção.
# 02) Altere o programa anterior para utilizar um menu com opções,
# permitindo inserção, exclusão e impressão de nomes em uma fila.
# 03) Inclua no programa anterior a opção de imprimir o primeiro elemento
# da fila.

class Node:
    """Nó de implementação para uma fila que se insere nomes."""
    def __init__(self):
        self.__nome = None
        self.__proxNome = None
    
    def setNome(self, nome):
        self.__nome = nome
    def setProximoNome(self, proxNome): 
        self.__proxNome = proxNome
    
    def getNome(self):
        return self.__nome
    def getProxNome(self):
        return self.__proxNome

class Fila:
    ''''''
    def __init__(self):
        self.__inicioFila = None
        self.__finalFila = None
    
    def push(self):
        novoNome = Node()
        if novoNome:
            novoNome.setNome(input("Digite um nome para colocar na fila: "))
            novoNome.setProximoNome(None) 
            if not self.__finalFila:
                self.__inicioFila = self.__finalFila = novoNome
            else:
                self.__finalFila.setProximoNome(novoNome)
                self.__finalFila = novoNome
            self.printAll()

    def pop(self):
        if self.__inicioFila:
            self.__inicioFila = self.__inicioFila.getProxNome()
            if not self.__inicioFila:
                self.__finalFila = None
        else:
            print("Fila vazia.")
    
    def printAll(self):
        if not self.__finalFila:
            print("Não há elementos cadastrados.")
            return False
        saida = ""
        temp = self.__inicioFila
        while temp:
            saida += temp.getNome() + "\t"
            temp = temp.getProxNome()
        print(saida)

    def printFirst(self):
        if not self.__finalFila:
            print("Não há elementos cadastrados.")
            return False
        print("O primeiro elemento da fila é: " + self.__inicioFila.getNome())

    """Fim da classe."""
filaTeste = Fila()

while True:
    print("\nMenu: ")
    print("[1] - Inserir um nome na fila (push)")
    print("[2] - Remover o primeiro elemento (pop)")
    print("[3] - Imprimir todos os nomes na fila")
    print("[4] - Imprimir o primeiro elemento da fila")
    print("[5] - Sair.")
    op = int(input("Digite uma opção do menu: "))
    if op == 1:
        filaTeste.push()
    elif op == 2:
        filaTeste.pop()
    elif op == 3:
        filaTeste.printAll()
    elif op == 4:
        filaTeste.printFirst()
    elif op == 5:
        break
    else:
        print("Opção digitada inválida.")