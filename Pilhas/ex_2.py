class MinhaPilha:
  __pilha = None

  def __init__(self):
    self.__pilha=[]

  def push(self, elemento):
    self.__pilha.append(elemento)

  def pop(self):
    if self.__pilha:
      print("\nElemento removido: ", self.__pilha[-1])
      self.__pilha.pop()
    else:
      print("\nPilha vazia.")

  def print_top(self):
    if self.__pilha:
      print("\nElemento do topo:", self.__pilha[-1])
    else:
      print("\nNão há topo para imprimir, pilha vazia")

  def print_all(self):
    for elemento in self.__pilha:
      print(elemento + " ", end="")

  def excluir_todos_elementos(self):
    del self.__pilha[:]
    print("Todos os elementos da lista foram removidos.")

pilha= MinhaPilha()

while True:
  print("\n[1] - Incluir um novo nome na pilha")
  print("[2] - Excluir o nome do topo da pilha")
  print("[3] - Imprimir o nome do topo da pilha")
  print("[4] - Imprimir todos os nomes da pilha")
  print("[5] - Excluir todos os nomes da pilha")
  print("[6] - Sair")
  op = int(input("Digite a opção desejada: "))
  if op == 1:
    pilha.push(input("Digite uma letra para empilhar: "))
  elif op == 2:
    pilha.pop()
  elif op == 3:
    pilha.print_top()
  elif op == 4:
    pilha.print_all()
  elif op ==5:
    pilha.excluir_todos_elementos()
  elif op == 6:
    print("Saindo...")
    break
  else:
    print("Opção inválida.")
