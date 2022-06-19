class Node:
    __dividendo: int
    __quociente: int
    __resto: int
    __proxNum: int
    def __init__(self):
        self.__dividendo = None
        self.__quociente = None
        self.__resto = None
        self.__proxNum = None    
    def setDividendo(self, value):
        self.__dividendo = value
    def setQuociente(self, value):
        self.__quociente = value
    def setResto(self, value):
        self.__resto = value
    def setProxNum(self, value):
        self.__proxNum = value
    def getDividendo(self):
        return self.__dividendo
    def getQuociente(self):
        return self.__quociente
    def getResto(self):
        return self.__resto
    def getProxNum(self):
        return self.__proxNum

class PilhaBinaria:

    def __init__(self):
        self.__numero = None
    
    def push(self):
        num = int(input("Digite o número que deseja converter para binário: "))
        while num != 0:
            y = Node()
            if y:
                y.setProxNum(self.__numero)
                y.setDividendo(num)
                y.setQuociente(int(y.getDividendo()/2))
                y.setResto(y.getDividendo()%2)
                num = y.getQuociente()
                self.__numero = y
    
    def converteBinario(self):
        temp = self.__numero
        numConvertido = ""
        while temp:
            numConvertido += str(temp.getResto())
            temp = temp.getProxNum()
        print("Após a conversão para binário: " + numConvertido)

    def converteDecimal(self):
        temp = self.__numero
        numConvertido = ""
        while temp:
            numConvertido = str(temp.getDividendo())
            temp = temp.getProxNum()
        print("Após converter de binário para decimal (usando o encadeamento): " + numConvertido)

    def __del__(self):
        while self.__numero:
            self.__numero = self.__numero.getProxNum()

while True:
    print("Menu")
    print("[1] - inserir um número e converte-lo para binário e depois para decimal novamente: ")
    print("[2] - Sair")
    op = int(input("Digite uma opção: "))
    if op == 1:        
        aPilha = PilhaBinaria()
        aPilha.push()
        aPilha.converteBinario()
        aPilha.converteDecimal()
        del(aPilha)
    elif op == 2:
        print("Saindo...")
        break
    else:
        print("Opção digitada inválida.")