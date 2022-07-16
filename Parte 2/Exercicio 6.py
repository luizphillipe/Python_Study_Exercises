'''Faça um programa para a leitura de duas notas parciais de um aluno. O
programa deve calcular a média alcançada por aluno e apresentar:
◦ A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
◦ A mensagem "Reprovado", se a média for menor do que sete;'''

nome = input("Informe o nome do Aluno: ")

nota_redacao = int(input("Informe a nota do aluno em Redação: "))
nota_matematica = int(input("Informe a nota do aluno em Matematica: "))

media = (nota_redacao + nota_matematica) / 2
if media  >= 7:
    print(f"O Aluno {nome} foi aprovado nas duas disciplinas")

else:
    print(f"O Aluno {nome} está em dependência acadêmica")
