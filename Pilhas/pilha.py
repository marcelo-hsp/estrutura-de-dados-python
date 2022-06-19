class Node:
	"""Uma classe que armazenará os nós de uma pilha encadeada."""
	def __init__(self):
		self.__valor = 0
		self.__prox = None
	
	def setValor(self, n):
		self.__valor = n
	
	def getValor(self):
		return self.__valor
	
	def setProx(self, obj):
		self.__prox = obj
	
	def getProx(self):
		return self.__prox

class Pilha:
	"""A classe que armazenará os endereçamentos de memória para apontar nos métodos de Node"""
	def __init__(self):
		self.__topo = None
	
	def push(self):
		novo = Node()
		if novo:
			novo.setValor(int(input('Digite um valor para armazenar na lista: ')))
			novo.setProx(self.__topo)
			self.__topo = novo
		
	def pop(self):
		if not self.__topo:
			print("Pilha Vazia...")
		else:
			self.__topo = self.__topo.getProx()
	
	def printAll(self):
		if not self.__topo:
			print("Pilha vazia...")
		else:
			temp = self.__topo
			msg = "\nPilha:\n"
			while temp:
				msg += str(temp.getValor()) + '\n'
				temp = temp.getProx()
			print(msg)

	def printTopoElemento(self):
		return str(self.__topo.getValor())
	"""Fim de classe."""		

	def somaTudo(self):
		if not self.__topo:
			print("Não há nada a ser somado...Pilha vazia...")
		else:
			temp = self.__topo
			soma = 0
			while temp:
				soma += temp.getValor()
				temp = temp.getProx()
		return str(soma)
	
	def fazMedia(self):
		if not self.__topo:
			print("Não há média a ser feita...Pilha vazia...")
		else:
			temp = self.__topo
			cont = 0
			soma = 0
			while temp:
				soma += temp.getValor()
				temp = temp.getProx()
				cont += 1
		return str(soma / cont)

aPilha = Pilha()

while True:
	print("[MENU]")
	print("[1] - Inserir um elemento")
	print("[2] - Remover um Elemento")
	print("[3] - Imprimir todos os elementos")
	print("[4] - Imprimir o elemento do topo")
	print("[5] - Imprimir a soma dos elementos")
	print("[6] - Imprimir a média dos elementos")
	print("[7] - Sair")
	opcao = int(input("Digite a opção que deseja: "))
	if opcao == 1:
		aPilha.push()
	elif opcao == 2:
		aPilha.pop()
	elif opcao == 3:
		aPilha.printAll()
	elif opcao == 4:
		print("O elemento do topo: " + aPilha.printTopoElemento())
	elif opcao == 5:
		print("A soma dos elementos é: " + aPilha.somaTudo())
	elif opcao == 6:
		print("A média dos elementos é: " + aPilha.fazMedia())
	elif opcao == 7:
		break
	else:
		print("Opção inválida.")