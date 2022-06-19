
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
    def __init__(self):
        self.__finalFila = None
    
    def push(self):
        novoNome = Node()
        if novoNome:
            novoNome.setNome(input("Digite um nome para colocar na fila: "))
            if not self.__finalFila:
                novoNome.setProximoNome(novoNome)
                self.__finalFila = novoNome
            else:
                novoNome.setProximoNome(self.__finalFila.getProxNome())
                self.__finalFila.setProximoNome(novoNome)
                self.__finalFila = novoNome
    
    def pop(self):
        if not self.__finalFila:
            print("Error")
            return False
        else:
            if self.__finalFila.getProxNome() is self.__finalFila.getProxNome().getProxNome():
                self.__finalFila.setProximoNome(None)
            else:
                self.__finalFila.setProximoNome(self.__finalFila.getProxNome().getProxNome())

    def printAll(self):
        if not self.__finalFila:
            print("Fila vazia")
            return False
        saida = '\nFila:\n'
        tempInicial = self.__finalFila.getProxNome()
        temp = self.__finalFila.getProxNome()
        while temp:
            saida += temp.getNome() + " "
            temp = temp.getProxNome()
            if temp is tempInicial:
                break
        print(saida)
    
    def printFirst(self):
        if not self.__finalFila:
            print("Não há elementos cadastrados.")
            return False
        print("O primeiro nome: " + self.__finalFila.getProxNome().getNome())

objeto = Fila()

while True:
    print("\nMenu: ")
    print("[1] - Inserir um nome na fila (push)")
    print("[2] - Remover o primeiro elemento (pop)")
    print("[3] - Imprimir todos os nomes na fila")
    print("[4] - Imprimir o primeiro elemento da fila")
    print("[5] - Sair.")
    op = int(input("Digite uma opção do menu: "))
    if op == 1:
        objeto.push()
    elif op == 2:
        objeto.pop()
    elif op == 3:
        objeto.printAll()
    elif op == 4:
        objeto.printFirst()
    elif op == 5:
        break
    else:
        print("Opção digitada inválida.")