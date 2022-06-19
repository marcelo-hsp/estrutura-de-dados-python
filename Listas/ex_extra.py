# Altere o programa da semana anterior (fila encadeada) para manipular as crianças em uma lista. 

# Você vai perceber que fica bem mais simples. Isso porque, conforme conversado na aula anterior, 
# não deveria ter sido programado em uma fila, nós forçamos isso. É importante escolher a estrutura correta para cada situação.

# Pense em como programar antes de iniciar a edição. Tem partes do código que podem ser completamente reutilizadas, 
# partes que necessitam de pequenos ajustes e partes que é menos confuso se apagar e criar novamente. 

# - Decida o que vai manter, o que vai ajustar e o que vai remover. 

# - Em seguida percorra o código editando o que é necessário e apagando o que decidiu remover. 
# Adicione "pass"onde julgar necessário para poder ir testando o código conforme edita.

# - Adicione as novas linhas de código para manipular as crianças na lista.

class Node:
    """Nó de implementação para uma lista que se insere nomes de crianças."""
    def __init__(self):
        self.__nome = None
        self.__proxNome = None
    
    def setNome(self, nome):
        self.__nome = nome
    def setProximoNome(self, proxNome): # não utilizável
        self.__proxNome = proxNome
    
    def getNome(self):
        return self.__nome
    def getProxNome(self):
        return self.__proxNome

class Lista:
    """Crianças."""
    def __init__(self):
        self.__inicioLista = None
        self.__finalLista = None
    
    def pushInicio(self):
        novaCrianca = Node()
        if novaCrianca:
            novaCrianca.setNome(input("Digite o nome da criana a ser adicionada no início da lista: "))
            novaCrianca.setProximoNome(self.__inicioLista)
            if not self.__inicioLista:
                self.__finalLista = novaCrianca
                self.__inicioLista = novaCrianca
            else:
                self.__inicioLista = novaCrianca
    
    def pushFim(self):
        novaCrianca = Node()
        if novaCrianca:
            novaCrianca.setNome(input("Digite o nome da criança a ser adicionada no fim da lista: "))
            if not self.__finalLista:
                self.__finalLista = novaCrianca
                self.__inicioLista = novaCrianca
            else:
                self.__finalLista.setProximoNome(novaCrianca)
                self.__finalLista = novaCrianca
    
    def pop(self):
        if not self.__finalLista:
            print("Lista vazia.")
            return
        else:
            self.printAll()
            crianca = input("Digite o nome da criança que deseja remover da lista: ")
            criancaAnterior = self.__inicioLista
            if criancaAnterior.getNome().upper() == crianca.upper():
                self.__inicioLista = self.__inicioLista.getProxNome()
                if not self.__inicioLista:
                    self.__finalLista = self.__inicioLista
                return
            
            while criancaAnterior.getProxNome():
                if criancaAnterior.getProxNome().getNome().upper() == crianca.upper():
                    criancaAnterior.setProximoNome(criancaAnterior.getProxNome().getProxNome())
                    if criancaAnterior.getProxNome() == None:
                        self.__finalLista = criancaAnterior
                    break
                criancaAnterior = criancaAnterior.getProxNome()
    
    def popAll(self):
        if not self.__finalLista:
            print("Lista vazia.")
            return
        self.__finalLista = self.__inicioLista = None

    def printAll(self):
        if not self.__finalLista:
            print("Lista vazia.")
            return
        else:
            str = ""
            temp = self.__inicioLista
            while temp:
                str += "[" + temp.getNome() + "]" + "\n"
                temp = temp.getProxNome()
            print(str)

objetoLista = Lista()
while True:
    print("[1] - Inserir uma criança no início da lista")
    print("[2] - Inserir uma criança no fim da lista")
    print("[3] - Excluir uma criança qualquer da lista")
    print("[4] - Excluir todas as crianças da lista")
    print("[5] - Imprimir a lista de crianças inteira")
    print("[6] - Sair")
    op = int(input("Digite uma opção do menu acima: "))
    if op == 1:
        objetoLista.pushInicio()
    if op == 2:
        objetoLista.pushFim()
    if op == 3:
        objetoLista.pop()
    if op == 4:
        objetoLista.popAll()
    if op == 5:
        objetoLista.printAll()
    if op == 6:
        break
    else:
        print("Opção digitada inválida")