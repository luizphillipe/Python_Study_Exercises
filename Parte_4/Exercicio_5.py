"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
consoantes foram lidas. Imprima as consoantes."""

Vetor = []
for caracteres in range (1,11):
    Max_String = input("Entre com os caracteres ")
    Vetor.append(Max_String)


print(Vetor)

vogal = ["a","e","i","o","u"]
for c in Vetor:
    if c not in vogal:
        print(c)