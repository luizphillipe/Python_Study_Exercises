'''10.Faça um código Python que leia duas notas de um aluno, calcule e exiba a
média aritmética das notas.'''

nota_matematica = float(input("Digite a nota de Matemática: "))
nota_geografia = float(input("Digite a nota de Geografia: "))

media_curso = ((nota_matematica+nota_geografia)/2)

print(f"A média do aluno no curso foi de {media_curso}")