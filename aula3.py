#laços de repetição + listas
#problema 1 a N - imprime os valores de 1 a N
'''
input numero maximo
valor inicial = 1
loop de valor_inicial a numero_maximo
print valor
'''
numero_maximo = int(input('Digite o número máximo: '))
valor_inicial = int(input('Qual o valor inicial?'))
numeros_pulados = int(input('Quantos números vai pular entre os valores?'))
for numero in range(valor_inicial, numero_maximo + numeros_pulados, numeros_pulados): 
  print(numero)
nomes = ['Jhonatan', 'Cristian', 'Roberto', 'Camila']
for nome in nomes:
  print(nome)