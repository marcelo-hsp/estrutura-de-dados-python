from inverte_palavra_e_verifica_palindromo import InvertePalavra_VerificaPalindromo

x = input("Digite uma palavra que deseja ver invertida: ")
objeto = InvertePalavra_VerificaPalindromo(x)
print("A palavra " + x + " invertida: ", end='')
objeto.printReverseWord()
print()