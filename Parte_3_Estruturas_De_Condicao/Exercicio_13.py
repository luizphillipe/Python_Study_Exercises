""".Faça um programa que leia 5 números inteiros positivos e informe a soma e a
média dos números."""
soma=0
for inteiros in range (0,5):
    a = int(input("Informe os 5 números: "))
    soma=soma+a
print("A soma dos números é: ", soma)

media=soma/5
print("A média dos números é", media)