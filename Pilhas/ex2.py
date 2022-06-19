class Node:

    def __init__(self):
        self.__nomeAluno = None
        self.__notaAluno = None
        self.__proxAluno = None
    
    def getNomeAluno(self):
        return self.__nomeAluno
    
    def getNotaAluno(self):
        return self.__notaAluno

    def getProxAluno(self):
        return self.__proxAluno

    def setNomeAluno(self, nome):
        self.__nomeAluno = nome
    
    def setNotaAluno(self, nota):
        self.__notaAluno = nota
    
    def setProxAluno(self, prox):
        self.__proxAluno = prox
    
class PilhaAluno:

    def __init__(self):
        self.alunoTopo = None
    
    def push(self):
        novoAluno = Node()
        if novoAluno:
            novoAluno.setNomeAluno(input("Digite o nome do aluno: "))
            novoAluno.setNotaAluno(float(input("Digite uma nota para o aluno: ")))
            novoAluno.setProxAluno(self.alunoTopo)
            self.alunoTopo = novoAluno
    
    def pop(self):
        if not self.alunoTopo:
            print("Não há aluno(s) cadastrados.")
        else:
            self.alunoTopo = self.alunoTopo.getProxAluno()
    
    def printAll(self):
        if not self.alunoTopo:
            print("Não há aluno(s) cadastrados.")
        else:
            temp = self.alunoTopo
            while temp:
                print("Aluno: " + temp.getNomeAluno() + "\tNota: " + str(temp.getNotaAluno()))
                temp = temp.getProxAluno()

    def printTopo(self):
        if not self.alunoTopo:
            print("Não há alunos cadastrados...")
        else:
            print("O aluno do topo: " + self.alunoTopo.getNomeAluno() + " \tNota: " + str(self.alunoTopo.getNotaAluno()))

    def calculaMedia(self):
        if not self.alunoTopo:
            print("Não há alunos cadastrados...")
        else:
            temp = self.alunoTopo
            somaNota = 0
            cont = 0
            while temp:
                somaNota += temp.getNotaAluno()
                cont += 1
                temp = temp.getProxAluno()
            print("A média das notas é: " + str((somaNota/cont)))
   
    """Fim da classe."""

aPilha = PilhaAluno()

while True:
    print("MENU")
    print("[1] - Inserir Aluno e nota")
    print("[2] - Exibir aluno e nota")
    print("[3] - Excluir aluno e nota")
    print("[4] - Imprimir aluno do topo")
    print("[5] - Imprimir média das notas")
    print("[7] - Sair")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        aPilha.push()
    elif opcao == 2:
        aPilha.printAll()
    elif opcao == 3:
        aPilha.pop()
    elif opcao == 4:
        aPilha.printTopo()
    elif opcao == 5:
        aPilha.calculaMedia()
    elif opcao == 7:
        break
    else:
        print("Opção inválida.")