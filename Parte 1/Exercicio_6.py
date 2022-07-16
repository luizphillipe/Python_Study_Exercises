'''Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor
e seu antecessor'''

numero = int(input("Digite o valor desejado: "))

antecessor = numero-1
sucessor = numero+1

print(f"O antecessor do numero {numero} é o {antecessor}")
print(f"O sucessor do numero {numero} é o {sucessor}")