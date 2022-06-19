class Node:
    """implementação da classe Node."""
    def __init__(self):
        self.letra = None
        self.proxLetra = None
    
    def setLetra(self, l):
        self.letra = l
    
    def getLetra(self):
        return self.letra
    
    def setProxLetra(self, proxL):
        self.proxLetra = proxL
    
    def getProxLetra(self):
        return self.proxLetra


class PilhaPalindromo:
    """Implementação da classe Pilha para verificar se é Palíndromo"""
    def __init__(self):
        self.palavra = None
        self.bkp_palavra = None
        
    def push(self):
        string = input("Digite uma string que deseja ver se é palindromo: ")
        for l in string:
            novaPalavra = Node()
            if novaPalavra:
                novaPalavra.setLetra(l)
                novaPalavra.setProxLetra(self.palavra)
                self.palavra = novaPalavra
        for l in reversed(string):
            novaPalavraInvertida = Node()
            if novaPalavraInvertida:
                novaPalavraInvertida.setLetra(l)
                novaPalavraInvertida.setProxLetra(self.bkp_palavra)
                self.bkp_palavra = novaPalavraInvertida
    
    def printAll(self):
        if not self.palavra:
            print("Não há o que imprimir.")
            return 0
        temp = self.palavra
        temp2 = self.bkp_palavra
        while temp:
            print(str(temp.getLetra()), end='')
            temp = temp.getProxLetra()
        print()
        while temp2:
            print(str(temp2.getLetra()), end='')
            temp2 = temp2.getProxLetra()

    def verificaPalindromo(self):
        if not self.palavra:
            print("Não há palavra para verificar.")
            return 0
        temp = self.palavra
        temp2 = self.bkp_palavra
        palindromo = False
        while temp:
            if temp.getLetra() == temp2.getLetra():
                palindromo = True
                temp = temp.getProxLetra()
                temp2 = temp2.getProxLetra()
            else:
                palindromo = False
                break
        if palindromo:
            print("A palavra " + self.printPalavra() + " é um palíndromo!")
        else:
            print("A palavra " + self.printPalavra() + " não é um palíndromo!")

    def printPalavra(self):
        temp = self.bkp_palavra
        palavra = ''
        while temp:
            palavra += temp.getLetra()
            temp = temp.getProxLetra()
        return palavra

    def printPalavraInvertida(self):
        temp = self.palavra
        temp2 = self.bkp_palavra
        palavraInvertida = ''
        palavra = ''
        while temp:
            palavraInvertida += temp.getLetra()
            temp = temp.getProxLetra()
            palavra += temp2.getLetra()
            temp2 = temp2.getProxLetra()    
        print("A palavra " + palavra + " invertida fica: " + palavraInvertida)

    def __del__(self):
        while self.palavra:
            self.palavra = self.palavra.getProxLetra()
        while self.bkp_palavra:
            self.bkp_palavra = self.bkp_palavra.getProxLetra()
    """Fim da classe."""

while True:
    print("MENU:")
    print("[1] - Inserir uma palavra e verificar se é palíndromo")
    print("[2] - sair")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        aPilha = PilhaPalindromo()
        aPilha.push()
        aPilha.printPalavraInvertida()
        aPilha.verificaPalindromo()
        del(aPilha)
    elif opcao == 2:
        print("Saindo...")
        break
    else:
        print("Opção digitada inválida.")