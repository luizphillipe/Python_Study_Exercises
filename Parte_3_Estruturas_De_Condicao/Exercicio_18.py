"""Crie um algoritmo que leia uma quantidade não determinada de números inteiros. O programa deve calcular e escrever
a quantidade de números pares e ímpares e a média aritmética dos números pares.
A leitura deve ser encerrada quando for lido o número zero, que não deve ser considerado."""

quantidade_par = 0
quantidade_impar = 0
while True:
    N=int(input("Entre com um número: "))
    if N == 0: break
    if N%2 == 0:
        quantidade_par = quantidade_par + 1
    else:
        quantidade_impar = quantidade_impar + 1

print(quantidade_par)
print(quantidade_impar)