"""Crie um algoritmo para ler uma letra do alfabeto e mostrar uma mensagem: se
é vogal ou consoante"""

Letra = input("Digite uma letra: ")

vogal = ["a","e","i","o","u"]
if Letra in vogal: print("é uma vogal")
else:
    print ("É uma consoante")