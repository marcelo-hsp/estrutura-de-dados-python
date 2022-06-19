class Node:
    """Nó de implementação Lista Encadeada."""
    def __init__(self):
        self.__nomeAluno = None
        self.__idadeAluno = None
        self.__proxAluno = None
    
    def getNomeAluno(self):
        return self.__nomeAluno
    
    def getIdadeAluno(self):
        return self.__idadeAluno

    def getProxAluno(self):
        return self.__proxAluno

    def setNomeAluno(self, nome):
        self.__nomeAluno = nome
    
    def setIdadeAluno(self, age):
        self.__idadeAluno = age
    
    def setProxAluno(self, prox):
        self.__proxAluno = prox
    
class PilhaAluno:
    """Pilha encadeada."""
    def __init__(self):
        self.alunoTopo = None
    
    def push(self):
        novoAluno = Node()
        if novoAluno:
            novoAluno.setNomeAluno(input("Digite o nome do aluno: "))
            novoAluno.setIdadeAluno(int(input("Digite a idade do aluno: ")))
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
                print("Aluno: " + temp.getNomeAluno() + "\tIdade: " + str(temp.getIdadeAluno()))
                temp = temp.getProxAluno()

    def printTopo(self):
        if not self.alunoTopo:
            print("Não há alunos cadastrados...")
        else:
            print("O aluno do topo: " + self.alunoTopo.getNomeAluno() + " \tIdade: " + str(self.alunoTopo.getIdadeAluno()))

    def somaIdades(self):
        if not self.alunoTopo:
            print("Não há alunos cadastrados...")
        else:
            temp = self.alunoTopo
            somaIdade = 0
            while temp:
                somaIdade += temp.getIdadeAluno()
                temp = temp.getProxAluno()
        return "A soma das idades é " + str(somaIdade) + " anos."

    def calculaMedia(self):
        if not self.alunoTopo:
            print("Não há alunos cadastrados...")
        else:
            temp = self.alunoTopo
            somaIdade = 0
            cont = 0
            while temp:
                somaIdade += temp.getIdadeAluno()
                cont += 1
                temp = temp.getProxAluno()
            print("A média das idades é: " + str((somaIdade/cont)))
    """Fim da classe."""

aPilha = PilhaAluno()

while True:
    print("MENU")
    print("[1] - Inserir Aluno e idade")
    print("[2] - Exibir aluno e idade")
    print("[3] - Excluir aluno e idade")
    print("[4] - Imprimir aluno do topo")
    print("[5] - Imprimir soma das idades")
    print("[6] - Imprimir média das idades")
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
        print(aPilha.somaIdades())
    elif opcao == 6:
        aPilha.calculaMedia()
    elif opcao == 7:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")