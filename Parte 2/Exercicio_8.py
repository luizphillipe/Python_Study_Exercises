'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 8.9 B
Entre 6.0 e 7.4 C
Entre 4.0 e 5.9 D
Entre 3.9 e zero E
O algoritmo deve mostrar as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
conceito for D ou E.'''

nome = input("Insira o nome do aluno: ")
disciplina_redacao = float(input("Insira a nota do aluno em redação: "))
disciplina_matematica = float(input("Insira a nota do aluno em matematica: "))

media = (disciplina_redacao + disciplina_matematica) / 2

if 9.0 <= media <= 10:
    print("A nota do aluno é A")
    print(f"O aluno {nome} está aprovado")
elif 7.5 < media <= 8.9:
    print("A nota do aluno é B")
    print(f"O aluno {nome} está aprovado")
elif 6.0 < media <= 7.4:
    print("A nota do aluno é C")
    print(f"O aluno {nome} está aprovado")
elif 4.0 < media <= 5.9:
    print("A nota do aluno é D")
    print(f"O aluno {nome }está reprovado")
elif 0 < media <= 3.9:
    print("A nota do aluno é E")
    print(f"O aluno {nome} está reprovado")

else:
    print("Insira notas válidas em um intervalo de 0 a 10")