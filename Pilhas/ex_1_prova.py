# Faça a implementação de um programa em Python usando a estrutura abstrata de dados para uma pilha encadeada, 
# das opções do menu:

# 1) função para inserir os dados referente a um cartão de crédito;
# 2) função para remover um cartão cadastrado;
# 3) função para imprimir todos os cartões cadastrados.

# Obrigatória a validação quanto à pilha vazia.

# Cartão de Crédito = Número; Nome Impresso; Mês Validade; Ano Validade; Código de Segurança.

# ATENÇÃO: para implementações iguais ou com fortes indícios de cópia, a pontuação da questão será zerada.

class NodeCartaoDeCredito():
    """Implementação do nó para aplicar a pilha encadeada"""
    def __init__(self):
        self.__numCartao = 0
        self.__nomeCartao = None
        self.__mesValidade = 0
        self.__anoValidade = 0
        self.__codSeguranca = 0
        self.__proxCartao = None

    def setNumeroCartao(self, numero):
        self.__numCartao = numero
    def setNomeCartao(self, nome):
        self.__nomeCartao = nome
    def setMesValidade(self, mes):
        self.__mesValidade = mes
    def setAnoValidade(self, ano):
        self.__anoValidade = ano
    def setCodSeguranca(self, cod):
        self.__codSeguranca = cod
    def setProximoCartao(self, prox):
        self.__proxCartao = prox
    
    def getNumeroCartao(self):
        return self.__numCartao
    def getNomeCartao(self):
        return self.__nomeCartao
    def getMesValidade(self):
        return self.__mesValidade
    def getAnoValidade(self):
        return self.__anoValidade
    def getCodSeguranca(self):
        return self.__codSeguranca
    def getProxCartao(self):
        return self.__proxCartao
    """Fim da classe"""

class PilhaCartao():
    """Pilha encadeada para gerenciamento de cartões."""
    def __init__(self):
        self.__cartaoAtual = None
    
    def cadastraCartao(self): # push
        novoCartao = NodeCartaoDeCredito()
        if novoCartao:
            novoCartao.setProximoCartao(self.__cartaoAtual)
            novoCartao.setNumeroCartao(int(input("Digite o número do cartão de crédito: ")))
            novoCartao.setNomeCartao(input("Digite o nome do cliente do cartão de crédito: "))
            novoCartao.setMesValidade(int(input("Digite um mês (numeral) de validade do cartão de crédito: ")))
            novoCartao.setAnoValidade(int(input("Digite um ano de validade do cartão de crédito: ")))
            novoCartao.setCodSeguranca(int(input("Digite o código de segurança do cartão de crédito: ")))
            self.__cartaoAtual=novoCartao
    
    def printAllCartoes(self):
        """Impressão de todos os cartões de créditos cadastrados no momento."""
        if not self.__cartaoAtual:
            print("Não há cartões cadastrados.")
            return False
        temp = self.__cartaoAtual
        while temp:
            print("Número do Carão: " + str(temp.getNumeroCartao()))
            print("Nome: " + temp.getNomeCartao())
            print("Mês de validade: " + str(temp.getMesValidade()))
            print("Ano de Validade: " + str(temp.getAnoValidade()))
            print("Codigo de segurança: " + str(temp.getCodSeguranca()))
            temp = temp.getProxCartao()
    
    def removeCartao(self): # pop
        """Remoção de um cartão da lista de cadastrados."""
        if not self.__cartaoAtual:
            print("Não há cartões cadastrados.")
            return False
        print("Removendo o cartão de número: " + str(self.__cartaoAtual.getNumeroCartao()))
        self.__cartaoAtual = self.__cartaoAtual.getProxCartao()
    """Fim da classe."""    

cartaoDeCredito = PilhaCartao()

while True:
    print(''' MENU
    [1] - Cadastrar um cartão de crédito
    [2] - Imprimir todos os cartões cadastrados
    [3] - Remover um cartão cadastrado
    [4] - Sair
    ''')
    op = int(input("Digite uma opção do menu acima: "))
    if op == 1:
        cartaoDeCredito.cadastraCartao()
    elif op == 2:
        cartaoDeCredito.printAllCartoes()
    elif op == 3:
        cartaoDeCredito.removeCartao()
    elif op == 4:
        print("Encerrando o programa.")
        break
    else:
        print("Opção digitada inválida.")