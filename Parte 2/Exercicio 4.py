'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme
a letra escrever: F - Feminino, M – Masculino'''

Letra = str(input("Digite um genero: "))
if Letra.upper() == 'F':
    print("O genero é do sexo feminino")
elif Letra.upper() == 'M':
    print("O genero é do sexo masculino")
else:
    print("Nenhuma outra opção disponível")