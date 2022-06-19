# Faça a implementação de um programa em Python usando a estrutura abstrata de dados para uma pilha sequencial,
# para as funções do menu: 

# 1) função que empilha os números primos de um inteiro qualquer

# 2) função que exclui um número primo

# 3) impressão na tela dos valores da pilha

# A leitura consiste em solicitar ao usuário um número inteiro não negativo, para, então, identificar 
# e empilhar os seus números primos. Sabe-se que números primos são os números naturais, ou seja, 
# números inteiros não negativos, que são divisíveis somente por dois divisores: o número 1 e ele mesmo. 
# Por exemplo, para o número 10, seriam empilhados os números primos 7, 5, 3 e 2.

# Obrigatória a validação quanto à pilha cheia ou vazia.

# ATENÇÃO: para implementações iguais ou com fortes indícios de cópia, ou para códigos que não executarem, 
# a pontuação da questão será zerada.

class Pilha():
    def __init__(self):
        self.__pilhaPrimos = []
    
    def push(self):
        num = int(input("Digite um número inteiro positivo: "))
        cont = 2
        while cont < num:
            if num % cont == 0:
                cont += 1
            else:
                if num % 3 == 0:
                    pass

    def printAll(self):
        if not self.__pilhaPrimos:
            print("Não há pilha para imprimir.")
            return False
        for num in self.__pilhaPrimos:
            print(num)

aPilha = Pilha()
aPilha.push()
aPilha.printAll()