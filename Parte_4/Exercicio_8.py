"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor
impar. Imprima os três vetores"""

#armazenar 20 numeros inteiros em um vetor
#os pares em um vetor par
#impares em um vetor impar
#imprimir os 3 vetores

Vetor = []

for inteiros in range (1,21):
    numeros = int(input("Entre com os números: "))
    Vetor.append(numeros)

Par = []
for elemento in Vetor:
    if elemento %2 == 0:
        Par.append(elemento)

Impar = []
for elemento in Vetor:
    if elemento %2 != 0:
        Impar.append(elemento)

print("Todos os elementos da lista são", Vetor)
print("Todos os elementos pares são:", Par)
print("Todos os elementos ímpares são:", Impar)