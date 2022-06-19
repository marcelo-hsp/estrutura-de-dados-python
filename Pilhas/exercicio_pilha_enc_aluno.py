class Node:
	"""Uma classe que armazenará os nós de uma pilha encadeada."""
	def __init__(self):
		self.__proxAluno = None
		self.__notaAluno = None
	
	def setProximoAluno(self, aluno):
		self.__proxAluno = aluno
	
	def getProximoAluno(self):
		return self.__proxAluno
	
	def setNota(self, nota):
		self.__notaAluno = nota
	
	def getNota(self):
		return self.__notaAluno
    
class Pilha:
	"""A classe que armazenará os endereçamentos de memória para apontar nos métodos de Node"""
	def __init__(self):
		self.__AlunoTopo = None

	def push(self, nota):
		novoAluno = Node()
		if novoAluno:
			novoAluno.setProximoAluno(self.__AlunoTopo)
			novoAluno.setNota(nota)
			self.__AlunoTopo = novoAluno
	
	def concatenaPilhas(self, aluno):
		if not self.__AlunoTopo:
			self.__AlunoTopo = Node()
			#self.__AlunoTopo.setProximoAluno(None)
		else:
			self.__AlunoTopo.setProximoAluno(aluno)

	# def pop(self):
	# 	if not self.__AlunoTopo:
	# 		print("Sem alunos cadastrados.")
	# 	else:
	# 		self.__AlunoTopo = self.__AlunoTopo.getNota()
	
	def printAll(self):
		if not self.__AlunoTopo:
 			print("Pilha vazia...")
		else:
			temp = self.__AlunoTopo
			while temp:
				print(str(temp.getNota()))
				 
	# def printTopoElemento(self):
	# 	return str(self.__AlunoTopo.getNomeAluno())
	# """Fim de classe."""		

	# def somaTudo(self):
	# 	if not self.__AlunoTopo:
	# 		print("Não há nada a ser somado...Pilha vazia...")
	# 	else:
	# 		temp = self.__AlunoTopo
	# 		soma = 0
	# 		while temp:
	# 			soma += temp.getNomeAluno()
	# 			temp = temp.getNota()
	# 	return str(soma)
	
	# def fazMedia(self):
	# 	if not self.__AlunoTopo:
	# 		print("Não há média a ser feita...Pilha vazia...")
	# 	else:
	# 		temp = self.__AlunoTopo
	# 		cont = 0
	# 		soma = 0
	# 		while temp:
	# 			soma += temp.getNomeAluno()
	# 			temp = temp.getNota()
	# 			cont += 1
	# 	return str(soma / cont)

pilhaMeninos = Pilha()
pilhaMeninas = Pilha()
pilhaConcat = Pilha()

pilhaMeninos.push(10.0)
pilhaMeninas.push(10.0)
pilhaConcat.concatenaPilhas(pilhaMeninos)
pilhaConcat.concatenaPilhas(pilhaMeninas)
pilhaConcat.printAll()



# while True:
# 	print("[MENU]")
# 	print("[1] - Inserir uma nota na pilha de meninos")
# 	print("[2] - Inserir uma nota na pilha de meninas")
# 	print("[3] - Concatenar pilha")
# 	print("[4] - Imprimir o elemento do topo")
# 	print("[5] - Imprimir a soma dos elementos")
# 	print("[6] - Imprimir a média dos elementos")
# 	print("[7] - Sair")
# 	opcao = int(input("Digite a opção que deseja: "))