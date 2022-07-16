"""9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e
mostre a soma dos quadrados dos elementos do vetor.
"""

#criar um vetor
#Inputar 10 números inteiros
#Soma dos quadrados

VetorA = []

for inteiros in range (1, 11):
    numeros = int(input("Digite o número inteiro: "))
    VetorA.append(numeros)

print(VetorA)

soma_elementos = 0
quadrado_elementos = 0
for I in VetorA:
 soma_elementos = soma_elementos+(I)
 quadrado_elementos = quadrado_elementos + (I ** 2)

print("O resultado da soma dos elementos é: ", soma_elementos)
print("O resultado da soma dos elementos por função é: ", sum(VetorA))
print("O resultado do quadrado dos elementos é: ", quadrado_elementos)


