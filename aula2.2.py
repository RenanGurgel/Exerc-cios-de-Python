'''
encontre o maior entre 2 números
'''
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')
if primeiro_valor == segundo_valor:
  print(f'Os valores são iguais {primeiro_valor} = {segundo_valor}')
elif primeiro_valor > segundo_valor:
  print (f'O {primeiro_valor} valor é maior')
elif primeiro_valor < segundo_valor:
  print (f'O {segundo_valor} valor é maior')