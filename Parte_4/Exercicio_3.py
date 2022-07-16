"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela"""

lista_notas = []
for notas in range (0,4):
    Nota=float(input("Digite o valor da nota: "))
    lista_notas.append(Nota)

print(lista_notas)

soma = 0
for elements in lista_notas:
    soma = (elements+soma)
soma = (soma/4)

print(soma)