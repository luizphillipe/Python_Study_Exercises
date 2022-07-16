'''Uma empresa resolveu dar um aumento de salário aos seus colaboradores e
deseja te contratar para desenvolver o programa que calculará os reajustes. O
programa deve receber, via teclado, o salário de um colaborador. O percentual
de reajuste é dado segundo os critérios abaixo:
◦ salários até R$ 1500,00 (incluindo) : aumento de 20%
◦ salários entre R$ 1500,01 e R$ 2700,00 : aumento de 15%
◦ salários entre R$ 2700,01 e R$ 3500,00 : aumento de 10%
◦ salários de R$ 3500,01 em diante : aumento de 8%
Após o cálculo do reajuste, informe na tela:
◦ o salário antes do reajuste;
◦ o percentual de reajuste aplicado;
◦ o valor do aumento;
◦ o novo salário, após o reajuste'''

colaborador = input("Informe o nome do colaborador: ")
colaborador_salario = float(input("Informe o salário do colaborador: "))

if colaborador_salario <= 1500:
    reajuste = 0.2
    novo_salario = colaborador_salario * (1+reajuste)
elif 1500.1 < colaborador_salario <= 2700:
    reajuste = 0.15
    novo_salario = colaborador_salario * (1+reajuste)
elif 2700.1 < colaborador_salario <= 3500:
    reajuste = 0.10
    novo_salario = colaborador_salario * (1+reajuste)
else:
    reajuste = 0.08
    novo_salario = colaborador_salario * (1+reajuste)


print(f"O salário antes do reajuste: {colaborador_salario}")
print(f"O reajuste foi de: {reajuste*100}%")
print(f"O valor do aumento foi de {novo_salario - colaborador_salario} ")
print(f"O valor do novo salário é de {novo_salario}")