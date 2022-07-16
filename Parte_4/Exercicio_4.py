"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
multiplicação e os números"""

import numpy as np

Vetor = []
for notas in range (1,6):
        notas = float(input("Digite o valor da nota: "))
        Vetor.append(notas)
print(Vetor)

soma = sum(Vetor)
print("O valor da soma é: ", soma)

maximo = max(Vetor)
print("O produto máximo é", maximo)

minimo = min(Vetor)
print("O produto mínimo é", minimo)

ordenacao = sorted(Vetor)
print("A sequência de lista ordenada é de", ordenacao)

multiplicacao = np.prod(Vetor)
print("Os produtos multiplicados são", multiplicacao)