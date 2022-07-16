"""1. Crie um programa que permita somar todos os elementos de uma lista."""

lista = [0,1,2,3,4,5,6]
print(lista)

soma = 0
for elements in lista:
    soma = elements+soma
    print(elements)

print(soma)
print(sum(lista))
