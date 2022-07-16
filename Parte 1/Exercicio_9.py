'''Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
que cada litro de tinta pinta uma áa de 2 metros quadrados.'''


largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))

calculo = (largura*altura)
calculo_litros = (calculo/2)
print(f"a área da parede resulta em {calculo}")
print(f"Será necessário o total de {calculo_litros} litros de tinta")