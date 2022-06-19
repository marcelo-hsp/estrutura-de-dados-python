class InvertePalavra_VerificaPalindromo():
    """Classe utilizada na resolução do exercício 3 e 4"""

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
    
    def __del__(self):
        self.palavra_em_lista = []
        self.lista_inversa = []
        self.bkp_palavra = []
    """Fim da classe."""

while True:
    print("\n[1] - Entrar com uma palavra e vê-la inversamente")
    print("[2] - Entrar com uma palavra e verificar se é um palíndromo")
    print("[3] - Sair")
    op = int(input("Digite uma opção: "))
    if op == 1:
        palavra = input("Digite uma palavra: ")
        objeto = InvertePalavra_VerificaPalindromo(palavra)
        objeto.printReverseWord()
        del(objeto)
    elif op == 2:
        palavra = input("Digite uma palavra: ")
        objeto2 = InvertePalavra_VerificaPalindromo(palavra)
        objeto2.verificaPalindromo()
        del(objeto2)
    elif op == 3:
        print("Saindo...")
        break
    else:
        print("Opção digitada inválida.")