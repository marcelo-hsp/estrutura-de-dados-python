class Node():
    """Nó para implementar a inversão da palavra com pilha encadeada."""
    def __init__(self):
        self.__letra = None
        self.__proximaLetra = None
    
    def setLetra(self, l):
        self.__letra = l
    
    def getLetra(self):
        return self.__letra
    
    def setProximaLetra(self, l):
        self.__proximaLetra = l
    
    def getProximaLetra(self):
        return self.__proximaLetra

    """Fim do nó"""

class PilhaInvertePalara():
    """Pilha encadeada para definição de PUSH, POP e PRINT"""
    def __init__(self):
        self.__palavra = None
    
    def push(self, string):
        # string = input("Digite uma palavra para vê-la invertida: ")
        for letra in string:
            novaPalavra = Node()
            if novaPalavra:
                novaPalavra.setLetra(letra)
                novaPalavra.setProximaLetra(self.__palavra)
                self.__palavra = novaPalavra
        
    def printPalavraInvertida(self):
        if not self.__palavra:
            return "Não foi inserido palavra."
        else:
            temp = self.__palavra
            palavra = ""
            while temp:
                palavra += temp.getLetra()
                temp = temp.getProximaLetra()
        return palavra
    """Fim da classe."""
aPilha = PilhaInvertePalara()
aPilha.push("batata")
print(aPilha.printPalavraInvertida())