'''
Problema: calcule a média de um aluno baseado nas suas 4 últimas provas, e verificar se foi aprovado
Critério: será aprovado se o aluno obtiver média maior ou igual a 7
'''
nota1 = int(input('Digite a nota da primeira prova: '))
nota2 = int(input('Digite a nota da segunda prova: '))
nota3 = int(input('Digite a nota da terceira prova: '))
nota4 = int(input('Digite a nota da quarta prova: '))
media = (nota1 + nota2 + nota3 + nota4) // 4
if media >= 7:
  print(f'Parabéns você foi aprovado! Sua média foi de: {media}')
elif media < 7:
  print(f'Infelizmente você foi reprovado! Sua média foi de: {media}')