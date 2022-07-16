""". Faça um Programa que leia um vetor de 10 números reais e mostre-os na
ordem inversa.
"""

Vetor = []

for numeros in range (1,11):
    reais = int(input("Entre com os numeros reais: "))
    Vetor.append(reais)
print(Vetor)

Vetor.reverse()
print(Vetor)