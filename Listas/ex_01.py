# Construa um programa para manipular inteiros em
# uma lista simplesmente encadeada e não ordenada:
# 1 – Inserir no final da lista 
# 2 – Inserir no início da lista
# 3 – Excluir um elemento
# 4 – Consultar a lista
# 5 – Esvaziar a lista

class Node:
    """Nó de implementação de uma Lista que manipula inteiros."""
    def __init__(self):
        self.__numeroInteiro = 0
        self.__proxNumero = None
    
    def setNumero(self, numero):
        self.__numeroInteiro = numero
    def getNumero(self):
        return self.__numeroInteiro
    def setProxNumero(self, proxNumero):
        self.__proxNumero = proxNumero
    def getProxNumero(self):
        return self.__proxNumero
    
class Lista:
    """Classe de implementação de uma lista."""
    def __init__(self):
        self.__inicioLista = None
        self.__finalLista = None
    
    def pushFinalLista(self):
        temp = Node()
        if temp:
            temp.setNumero(int(input("Digite um número para adicionar no final da lista: ")))
            if not self.__finalLista:
                self.__finalLista = temp
                self.__inicioLista = temp
            else:
                self.__finalLista.setProxNumero(temp)
                self.__finalLista = temp
    
    def pushComecoLista(self):
        temp = Node()
        if temp:
            temp.setNumero(int(input("Digite um número para adicionar ao começo da lista: ")))
            temp.setProxNumero(self.__inicioLista)
            if not self.__inicioLista:
                self.__finalLista = temp
                self.__inicioLista = temp
            else:
                self.__inicioLista = temp

    def pop(self):
        if not self.__finalLista:
            print("Lista vazia.") 
            return
        # PRINT ALL HERE
        self.printAll()
        x = int(input("Digite o número que deseja excluir da lista: "))
        elemento_anterior = self.__inicioLista

        # Verifica o se o elemento a ser excluído já é o primeiro objeto da lista
        if elemento_anterior.getNumero() == x:
            self.__inicioLista = self.__inicioLista.getProxNumero()
            if not self.__inicioLista:
                self.__finalLista = None
            return
        
        # Caso elemento desejado não seja o primeiro da lista
        while elemento_anterior.getProxNumero():
            if elemento_anterior.getProxNumero().getNumero() == x:
                elemento_anterior.setProxNumero(elemento_anterior.getProxNumero().getProxNumero())
                if elemento_anterior.getProxNumero() == None:
                    self.__finalLista = elemento_anterior
                break
            elemento_anterior = elemento_anterior.getProxNumero()
    
    def popAll(self):
        if not self.__finalLista:
            print("Lista vazia.")
            return
        self.__inicioLista = None
        self.__finalLista = None
    
    def printAll(self):
        if not self.__finalLista:
            print("Lista vazia.")
            return
        out = ""
        temp = self.__inicioLista
        while temp:
            out += 'objeto: ' + str(temp) + ' Valor: ' + str(temp.getNumero()) + ' Próximo objeto: ' + str(temp.getProxNumero()) + '\n'
            temp = temp.getProxNumero()
        print(out)

objetoLista = Lista()
while True:
    print("[1] - Inserir no início da lista")
    print("[2] - Inserir no fim da lista")
    print("[3] - Excluir um elemento qualquer da lista")
    print("[4] - Excluir todos os elementos da lista")
    print("[5] - Imprimir a lista inteira")
    print("[6] - Sair")
    op = int(input("Digite uma opção do menu acima: "))
    if op == 1:
        objetoLista.pushComecoLista()
    if op == 2:
        objetoLista.pushFinalLista()
    if op == 3:
        objetoLista.pop()
    if op == 4:
        objetoLista.popAll()
    if op == 5:
        objetoLista.printAll()
    if op == 6:
        break
    else:
        print("Opção digitada inválida")