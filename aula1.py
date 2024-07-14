# escreva um programa que imprima o valor hora de uma base com base no seu salário e na suas horas trabalhadas por mês
salario_mensal = input('Qual é o seu salário mensal?')
horas_trabalhadas_por_mes = input('Quantas horas você trabalha por mês?')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print('seu valor hora é de')
print(valor_hora)