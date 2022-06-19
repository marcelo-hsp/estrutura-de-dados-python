from inverte_palavra_e_verifica_palindromo import InvertePalavra_VerificaPalindromo

x = input("Digite uma palvra que deseja saber se é ou não Palíndromo: ")
objeto = InvertePalavra_VerificaPalindromo(x)
print("A palavra " + x + ": ", end='')
objeto.verificaPalindromo()