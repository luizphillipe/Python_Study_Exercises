'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro.'''

nome = (input("Digite o seu nome: "))
senha = str(input("Digite a sua senha: "))

if nome.upper() == senha.upper():
    print("Erro: A senha não pode ser igual o seu nome.")