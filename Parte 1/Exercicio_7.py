'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz
quadrada.'''

valor = float(input("Digite o valor 1: "))
operacao_dobro = (valor*2)
operacao_triplo = (valor*3)
operacao_raiz = (valor**(1/2))

nome = (input("Qual seu nome?: "))

print(f"{nome}, O dobro do numero {valor} resulta em {operacao_dobro} ")
print(f"O triplo do numero {valor} resula em {operacao_triplo}")
print(f"A raiz quadrada do numero {valor} resulta em {operacao_raiz}")