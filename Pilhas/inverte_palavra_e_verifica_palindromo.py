class InvertePalavra_VerificaPalindromo():
    """Classe utilizada na resolução dos exercícios 3 e 4"""

    palavra_em_lista = []
    lista_inversa = []
    bkp_palavra = []

    def __init__(self, palavra):
        self.reverseWord(palavra)

    def reverseWord(self, palavra):
        for letra in palavra:
            self.palavra_em_lista.append(letra)
            self.bkp_palavra.append(letra)     
        while self.palavra_em_lista:
            self.lista_inversa.append(self.palavra_em_lista.pop())
    
    def verificaPalindromo(self):
        if self.bkp_palavra[:] == self.lista_inversa[:]:
            print("é um palíndromo")
        else:
            print("Não é um palíndromo")
    
    def printReverseWord(self):
        for letra in self.lista_inversa:
            print(letra, end="")
    
    """Fim da classe."""