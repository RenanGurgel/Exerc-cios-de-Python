'''
levando em consideração a velocidade máxima permitida de 80km/h em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ele tomou uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima".

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
-velocidade(km)
2. O que devo fazer com estes dados?
-determinar se essa velocidade do usuário está abaixo, acima, muito acima ou dentro da velocidade máxima permitida.
3. Quais são as restrições deste problema?
-velocidade máxima permitida é de 80km/h
4. Qual é o resultado esperado?
-exibir a mensagem que corresponde ao nível da multa que a pessoa levou.
-caso esteja abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave" e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima".
5. Qual é a sequência de passos a serem feitos?
input velocidade
velocidade_maxima = 80 
if velocidade <= velocidade_maxima:
  print('não levou multa')
elif velocidade > velocidade_maxima e velocidade <= velocidade_maxima + 10:
  print('levou multa leve')
elif velocidade > velocidade_maxima + 11 e velocidade <= velocidade_maxima + 20:
  print('levou multa grave')
elif velocidade > velocidade_maxima + 20:
  print('levou multa gravíssima')
'''
velocidade = int(input('Digite sua velocidade: '))
velocidade_maxima = 80
velocidade_excedida = velocidade - velocidade_maxima
if velocidade <= velocidade_maxima:
  print(f'não levou multa pois a velocidade máxima permitida é {velocidade_maxima}km/h')
elif velocidade >= velocidade_maxima and velocidade <= velocidade_maxima + 10:
  print(f'levou multa leve pois a velocidade máxima permitida é {velocidade_maxima}km/h, além disso você ultrapassou apenas {velocidade_excedida}km/h da velocidade permitida')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
  print(f'levou multa grave pois a velocidade máxima permitida é {velocidade_maxima}km/h, além disso você ultrapassou {velocidade_excedida}km/h da velocidade permitida')
elif velocidade >= velocidade_maxima + 20:
  print(f'levou multa gravíssima pois a velocidade máxima permitida é {velocidade_maxima}km/h, além disso você ultrapassou {velocidade_excedida}km/h da velocidade permitida')