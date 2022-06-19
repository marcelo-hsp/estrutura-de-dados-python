class Pilha():
    def __init__(self):
        self.__pilha = []
       
    def push(self):
        num = int(input("Digite um numero: "))
        primo = True
        for i in range(num, 1, -1):
            j = 2
            while j < i:
                resto = i%j
                if (resto == 0):
                    primo = False
                    break
                j +=1
                
            if (primo):
                self.__pilha.append(i)
        
            primo = True
    
    def printAll(self):
        if not self.__pilha:
            print("Pilha vazia")
            return False
        for i in self.__pilha:
            print(str(i) + "\t", end='')
    
    def pop(self):
        if not self.__pilha:
            print("Pilha vazia")
            return False
        self.__pilha.pop()

    def __del__(self):
        if not self.__pilha:
            print("Pilha vazia")
            return False
        while self.__pilha:
            self.__pilha.pop()

aPilha = Pilha()

while True:
    print('''\n MENU
    [1] - inserir numero
    [2] - imprimir todos os numeros
    [3] - remover um numero
    [4] - deletar
    [5] - sair
    ''')
    op = int(input("Digite uma opção: "))
    if op==1:
        aPilha.push()
    elif op == 2:
        aPilha.printAll()
    elif op == 3:
        aPilha.pop()
    elif op == 4:
        del(aPilha)
        aPilha = Pilha()
    elif op == 5:
        break
    else:
        print("error")
