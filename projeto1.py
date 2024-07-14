'''
crie um programa que recebe um número e imprime o seu fatorial
5Q's
1. Quais são os dados de entrada necessários?
2. O que devo fazer com estes dados?
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
5. Qual é a sequência de passos a serem feitas para chegar ao resultado esperado?
'''
numero = int(input('Digite um número que você deseja o fatorial:'))
if numero > 0:
  fatorial = 1
  for item in range(1,numero + 1):
    fatorial = fatorial * item
  print(f'O fatorial de {numero} é {fatorial}')
elif numero == 0:
  print('O fatorial de 0 é 1')
elif numero < 0:
  print('não existe fatorial de número negativo')