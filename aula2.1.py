'''
Eu cheguei atrasado na aula, ainda posso entrar?
Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrário você terá que tomar uma suspensão.
'''
numero_de_atrasos = input ('Quantas vezes você chegou atrasado?')
if int(numero_de_atrasos) >= 3:
  print('Você está suspenso')
elif int(numero_de_atrasos) == 1:
 print('pode entrar, porém caso tome mais 2 faltas, irá ser suspenso')
elif int(numero_de_atrasos) == 2:
 print('pode entrar, porém caso tome mais 1 falta, irá ser suspenso')