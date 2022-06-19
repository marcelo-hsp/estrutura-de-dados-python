num = int(input('num: '))
cont = 2
n = 0

while (cont < num):
    if (num % cont) == 0:
        if (n == 0):
            print("nao e primo,\n multiplos ")
            print(cont)
            n += 1
            cont+=1
        else:
            print(cont)
            n+=1
            cont+=1
    else:
        print("é primo: ")
        cont +=1
    if n == 0:
        print("é primo")