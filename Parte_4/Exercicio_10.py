"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que
determine quantos alunos com mais de 13 anos possuem altura inferior à
média de altura desses alunos"""

#idade e altura 30 alunos
#alunos com mais de 13 anos
#altura inferir a media

from random import randint, uniform

alunos = []
for lista_alunos in range (30):
    idade = randint(10,18)
    altura = uniform(1, 2)

    grupo_aluno = (idade, altura)
    alunos.append(grupo_aluno)
print(alunos)

soma = 0
for aluno in alunos:
    soma = soma+aluno[1]
print(soma/30)
media_altura_alunos = (soma/30)

for aluno in alunos:
    if aluno[0] > 13:
        if aluno[1] < media_altura_alunos:
            print(aluno)

