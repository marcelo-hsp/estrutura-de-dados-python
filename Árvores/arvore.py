class Node:
    def __init__(self):
        self.__info = 0
        self.__direita = None
        self.__esquerda = None
        self.__raizPai = None   
    
    def getInfo(self):
        return self.__info
    def setInfo(self, info):
        self.__info = info
    
    def getDireita(self):
        return self.__direita
    def setDireita(self, direita):
        self.__direita = direita
    
    def getEsquerda(self):
        return self.__esquerda
    def setEsquerda(self, esquerda):
        self.__esquerda = esquerda

    def setRaizPai(self, raiz):
        self.__raizPai = raiz
    def getRaizPai(self):
        return self.__raizPai

class Arvore:
    def __init__(self):
        self.__raiz = None
    
    def inserir(self, aux: Node, n):
        if aux is None:
            aux = Node()
            aux.setInfo(n)
            aux.setRaizPai(None)
            self.__raiz = aux
        elif n < aux.getInfo():
            aux.setEsquerda(self.inserir(aux.getEsquerda(), n))
            aux.getEsquerda().setRaizPai(aux)
        else:
            aux.setDireita(self.inserir(aux.getDireita(), n))
            aux.getDireita().setRaizPai(aux)
        return aux

    def contar(self, raiz):
        if not self.__raiz:
            return
        if not raiz:
            ref = self.__raiz
        if raiz is None:
            ref = raiz
        if not self.ePai(ref):
            return 1
        else:
            n = self.contar(ref.getDireita()) + self.contar(ref.getEsquerda())
        return n
    
    def buscaElemento(self, raiz: Node, elemento: int):
        a = 0
        b = 0
        if not raiz:
            return 0
        else:
            if raiz.getInfo() == elemento:
                return 1
            else:
                if not raiz.getEsquerda() and not raiz.getDireita():
                    return 0
                a += self.buscaElemento(raiz.getEsquerda(), elemento)
                b += self.buscaElemento(raiz.getDireita(), elemento)
                return a + b

    def preOrdem(self, raiz: Node):
        if not self.__raiz:
            return
        if not self.ePai(raiz):
            print(str(raiz.getInfo()))
        else:
            print(str(raiz.getInfo()))
            if not raiz.getDireita() and raiz.getEsquerda():
                self.preOrdem(raiz.getEsquerda())
            elif raiz.getDireita() and not raiz.getEsquerda():
                self.preOrdem(raiz.getDireita())
            else:
                self.preOrdem(raiz.getEsquerda())
                self.preOrdem(raiz.getDireita())

    def ordem(self, raiz: Node):
        if not self.__raiz:
            return
        if self.ePai(raiz):
            if not raiz.getEsquerda():
                print(str(raiz.getInfo()))
                print(str(raiz.getDireita().getInfo()))
                if self.ePai(raiz.getDireita()):
                    self.ordem(raiz.getDireita())
            else:
                print(str(raiz.getEsquerda().getInfo()))
                print(str(raiz.getInfo()))    
                if self.ePai(raiz.getEsquerda()):
                    self.ordem(raiz.getEsquerda())
                if raiz.getDireita():
                    print(str(raiz.getDireita().getInfo()))
                    self.ordem(raiz.getDireita())
    
    def posOrdem(self, raiz: Node):
        if not self.__raiz:
            return
        if self.ePai(raiz):
            if raiz.getEsquerda() and not raiz.getDireita():
                print(str(raiz.getEsquerda().getInfo()))
                if self.ePai(raiz.getEsquerda()):
                    self.posOrdem(raiz.getEsquerda())
            elif not raiz.getEsquerda() and raiz.getDireita():
                print(str(raiz.getDireita().getInfo()))
                if self.ePai(raiz.getDireita()):
                    self.posOrdem(raiz.getDireita())
            elif raiz.getEsquerda() and raiz.getDireita():
                print(str(raiz.getEsquerda().getInfo()))
                if self.ePai(raiz.getEsquerda()):
                    self.posOrdem(raiz.getEsquerda())
                else:
                    print(str(raiz.getDireita().getInfo()))
                    if self.ePai(raiz.getDireita()):
                        print(str(raiz.getInfo()))
                        self.posOrdem(raiz.getDireita())
                    else:
                        print(str(raiz.getInfo()))
            else:
                print(str(raiz.getInfo()))

    def remove(self, raiz: Node, elemento):
        if not raiz:
            return 
        else:
            if raiz.getInfo() == elemento:
                if raiz.getRaizPai().getDireita() == raiz:
                    if self.ePai(raiz):
                        if not raiz.getDireita() and raiz.getEsquerda():
                            raiz.getRaizPai().setDireita(raiz.getEsquerda())
                        elif raiz.getDireita() and not raiz.getEsquerda():
                            raiz.getRaizPai().setDireita(raiz.getDireita())
                        else:
                            raiz.getRaizPai().setDireita(raiz.getDireita())
                    else:
                        raiz.getRaizPai().setDireita(None)
                else:
                    if self.ePai(raiz):
                        if not raiz.getDireita() and raiz.getEsquerda():
                            raiz.getRaizPai().setEsquerda(raiz.getEsquerda())
                        elif raiz.getDireita() and not raiz.getEsquerda():
                            raiz.getRaizPai().setEsquerda(raiz.getDireita())
                        else:
                            raiz.getRaizPai().setEsquerda(raiz.getDireita())
                    else:
                        raiz.getRaizPai().setEsquerda(None)
            else:
                self.remove(raiz.getDireita(), elemento)
                self.remove(raiz.getEsquerda(), elemento)

    def ePai(self, raiz: Node):
        if raiz.getDireita() or raiz.getEsquerda():
            return True
        else:
            return False
    
    def eFolha(self, raiz: Node):
        if not raiz.getRaizPai():
            return False
        else:
            return True

    def eFilhoEsquerdo(self, raiz: Node):
        if not self.eFolha(raiz):
            return False
        else:
            if raiz == raiz.getRaizPai().getEsquerda():
                return True
            else:
                return False
    
    def eFilhodDireito(self, raiz: Node):
        if not self.eFolha(raiz):
            return False
        else:
            if raiz == raiz.getRaizPai().getDireita():
                return True
            else:
                return False

def menu():
    try:
        print("MENU")
        print("[1] - Inserir")
        print("[2] - Imprimir em pré-ordem")
        print("[3] - Imprimir em intra-ordem")
        print("[4] - Imprimir em pós-ordem")
        print("[5] - Excluir")
        print("[9] - Sair")
        op = int(input("Digite uma opção válida: "))
        return op
    except ValueError:
        menu()

if __name__ == '__main__':
    raizRegistrada = False
    root = None
    raiz = None
    arvore = Arvore()
    op = menu()
    while op != 9:
        if op == 1:
            n = int(input("Digite um número inteiro: "))
            if not raizRegistrada:
                root = arvore.inserir(None, n)
                raiz = root
                raizRegistrada = True
            else:
                raiz = arvore.inserir(raiz, n)
        elif op == 2:
            arvore.preOrdem(root)
        elif op == 3:
            arvore.ordem(root)
        elif op == 4:
            arvore.posOrdem(root)
        elif op == 5:
            n = int(input("Digite o elemento que deseja excluir: "))
            if arvore.buscaElemento(root, n) == 0:
                print("Elemento não encontrado")
            else:
                arvore.remove(root, n)
        elif op == 9:
            break
        else:
            print("Opção inválida.")
        op = menu()