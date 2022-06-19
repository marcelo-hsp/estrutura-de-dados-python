class Node:
    def __init__(self):
        self.numero = 0
        self.proxNumero = None
    
    def getNumero(self):
        return self.numero
        
    def getProxNumero(self):
        return self.proxNumero
        
    def setNumero(self, n):
        self.numero = n
        
    def setProxNumero(self, pn):
        self.proxNumero = pn

class Pilha:
    def __init__(self):
        self.topoNum = None
    
    def push(self, num):
        novoNum = Node()
        if novoNum:
            novoNum.setProxNumero(self.topoNum)
            novoNum.setNumero(num)
            self.topoNum = novoNum
    
    def pop(self):
        if not self.topoNum:
            print("Não há elementos para remover...")
        else:
            print("Removendo o elemento: " + str(self.topoNum.getNumero()))
            self.topoNum = self.topoNum.getProxNumero()
    
    def printAll(self):
        temp = self.topoNum
        msg = ""
        while temp:
            msg += str(temp.getNumero()) + "\t"
            temp = temp.getProxNumero()
        return msg
    """Fim da classe."""

def printGeral(positivos: Pilha, negativos: Pilha):
    """Função no escopo global do programa."""
    print("Positivos: ", end='')
    print(positivos.printAll())
    print("\nNegativos: ", end='')
    print(negativos.printAll())

pPilha = Pilha()
nPilha = Pilha()

while True:
    print("\n\nMENU")
    print("[1] - Inserir um número")
    print("[2] - Print as duas Pilhas")
    print("[3] - Sair")
    op = int(input("\nDigite uma opção: "))
    if op == 1:
        num = int(input("Digite um número para adicionar na lista: "))
        if num > 0:
            pPilha.push(num)
            printGeral(pPilha, nPilha)
        elif num < 0:
            nPilha.push(num)
            printGeral(pPilha, nPilha)
        elif num == 0:
            pPilha.pop()
            nPilha.pop()
            printGeral(pPilha, nPilha)
    elif op == 2:
        print("Positivos: ")
        print(pPilha.printAll())
        print("\nNegativos: ")
        print(nPilha.printAll())
    elif op == 3:
        print("Saindo...")
        break