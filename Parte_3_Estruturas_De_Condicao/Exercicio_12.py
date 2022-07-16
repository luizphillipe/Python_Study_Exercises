"""Criar um programa que imprima todos os números de 1 até 100, inclusive, e a
soma de todos eles."""

soma = 0
for numeros in range (1, 101):
    print(numeros)
    soma=soma+numeros

print(soma)