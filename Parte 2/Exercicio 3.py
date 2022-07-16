'''Faça um Programa que peça dois números e imprima o maior deles. Caso
sejam iguais, nada deverá ser exibido.'''

numeroA = int(input("Digite o númeroA: "))
numeroB = int(input("Digite o númeroB: "))

if numeroA > numeroB:
    print("O númeroA é maior que o numeroB ")

elif numeroA == numeroB:
    print(" ")

else:
    print("O númeroB é maior que o numeroA ")
