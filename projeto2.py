'''
Escreva um programa que, ao iniciar gera um número aletório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor

5Q's
1. Quais são os dados de entrada necessários?
 -Número escolhido pelo usuário de 1 a 10
 -Número aleatório de 1 a 10 gerado pela máquina
2. O que devo fazer com estes dados?
 -Comparar o número escolhido pelo usuário com o número aleatório gerado pela máquina
 -Se o número escolhido pelo usuário for igual ao número aleatório gerado pela máquina, deve informar que o usuário acertou o chute.
 -Se o número escolhido pelo usuário for maior que o número aleatório gerado pela máquina, deve informar que o usuário chutou alto.
 -Se o número escolhido pelo usuário for menor que o número aleatório, deve informar que o usuário chutou baixo.
3. Quais são as restrições deste problema?
 -O número gerado tem do usuário tem que ser entre 1 a 10
 -O número gerado pela máquina tem que ser entre 1 a 10
4. Qual é o resultado esperado?
 -Indicar ao usuário se o número escolhido pelo usuário é igual, menor ou maior ao número aleatório gerado pela máquina.
5. Qual é a sequência de passos a serem realizados para chegar ao resultado esperado?
valor aleatório de 1 a 10
Chute do usuário = int(input('Digite um número de 1 a 10'))
if chute > valor_aleatorio:
print(chute é maior que o valor gerado)
elif chute < valor_aleatorio:
print(chute é menor que o valor gerado)
elif chute = valor_aleatorio:
print(você acertou)
'''
from random import randint
valor_aleatorio = randint(1,10)
acertou = False
while(acertou == False):  
  chute = int(input('Digite um número de 1 a 10:  '))
  if chute == valor_aleatorio:
    print('você acertou')
    acertou = True
  elif chute > valor_aleatorio:
    print('você chutou alto')
    print(f'O valor gerado pela máquina foi {valor_aleatorio}')
  elif chute < valor_aleatorio:
    print('você chutou baixo')
    print(f'O valor gerado pela máquina foi {valor_aleatorio}')
  
