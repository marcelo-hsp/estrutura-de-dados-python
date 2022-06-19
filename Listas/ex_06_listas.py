# Construa um programa que, a partir de lista encadeada L desordenada,
# tenha uma função que cria uma nova lista Kordenada, com os
# mesmos nósda lista L.
# A funçãoremove os elementos da lista L, e insere-os na lista K,
# que dessa forma torna-se uma lista ordenada (em ordem crescente).
# Observações:
# •Não devem ser criados nós extras, deve-se utilizar os mesmos nós
# alocados para a lista L.
# •No final do processo, a lista L estará vazia e a lista Kconterá os nós
# anteriormente alocados para a lista L.

class Node:
    def __init__(self):
        self.__numeroInteiro = 0
        self.__proximoNumero = None
    
    def setNumeroInteiro(self, numeroInteiro):
        self.__numeroInteiro = numeroInteiro
    def getNumeroInteiro(self):
        return self.__numeroInteiro
    def setProximoNumero(self, proximoNumero):
        self.__proximoNumero = proximoNumero
    def getProximoNumero(self):
        return self.__proximoNumero

class Lista:
    def __init__(self):
        self.__inicioLista = None
        self.__fimLista = None
    
    def pushInicio(self):
        novoNum = Node()
        if novoNum:
            novoNum.setNumeroInteiro(int(input("Digite um número inteiro: ")))
            novoNum.setProximoNumero(self.__inicioLista)
            if not self.__inicioLista:
                self.__inicioLista = novoNum
                self.__fimLista = novoNum
            else:
                self.__inicioLista = novoNum
    
    def pushFim(self):
        novoNum = Node()
        if novoNum:
            novoNum.setNumeroInteiro(int(input("Digite um número para inserir no final da lista: ")))
            if not self.__fimLista:
                self.__inicioLista = novoNum
                self.__fimLista = novoNum
            else:
                self.__fimLista.setProximoNumero(novoNum)
                self.__fimLista = novoNum
    
    def pushOrdenado(self, listaDesordenada):
        for elemento in listaDesordenada: # atentar para essa parte
            novaListaOrdenada = Node()
            if novaListaOrdenada:
                novaListaOrdenada.setNumeroInteiro(elemento.getNumeroInteiro())
                novaListaOrdenada.setProximoNumero(self.__inicioLista)
                if not self.__inicioLista:
                    self.__inicioLista = novaListaOrdenada
                    self.__fimLista = novaListaOrdenada
                elif novaListaOrdenada.getNumeroInteiro() < self.__inicioLista.getNumeroInteiro():
                    novaListaOrdenada.setProximoNumero(self.__inicioLista)
                    self.__inicioLista = novaListaOrdenada
                elif novaListaOrdenada.getNumeroInteiro() > self.__fimLista.getNumeroInteiro():
                    self.__fimLista.setProximoNumero(novaListaOrdenada)
                    self.__fimLista = novaListaOrdenada
                else:
                    ref_ant = self.__inicioLista
                    while True:
                        if novaListaOrdenada.getNumeroInteiro() < ref_ant.getProximoNumero().getNumeroInteiro():
                            novaListaOrdenada.setProximoNumero(ref_ant.getProximoNumero())
                            ref_ant.setProximoNumero(novaListaOrdenada)
                            break
                        ref_ant = ref_ant.getProximoNumero()

    def getAll(self):
        if not self.__inicioLista:
            return
        elementos = []
        temp = self.__inicioLista
        while temp:
            elementos.append(temp)
            if temp.getProximoNumero() is None:
                break
            temp = temp.getProximoNumero()
        return elementos

    def printAll(self):
        if not self.__inicioLista:
            print("Lista vazia.")
            return
        temp = self.__inicioLista
        while temp:
            print("->" + str(temp.getNumeroInteiro()))
            temp = temp.getProximoNumero()

lista_K = Lista()
lista_L = Lista()

while True:
    print("MENU")
    print("[1] - Push inicio lista")
    print("[2] - Push fim")
    print("[3] - print all lista original")
    print("[4] - Ordenar lista em uma nova")
    print("[5] - print all lista ordenada")
    print("[6] - Test getall")
    print("[0] - sair")
    op = int(input("Digite uma opção do menu acima: "))
    if op == 1:
        lista_K.pushInicio()
    elif op == 2:
        lista_K.pushFim()
    elif op == 3:
        lista_K.printAll()
    elif op == 4:
        lista_L.pushOrdenado(lista_K.getAll())
    elif op == 5:
        lista_L.printAll()
    elif op == 6:
        for i in lista_K.getAll():
            print(str(i.getNumeroInteiro()))
    
    elif op == 0:
        break
