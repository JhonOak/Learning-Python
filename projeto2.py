# Chute um número
'''
Crie um programa que ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.
# Método 5Q's para montar um algoritimo:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o programa.)

1. Quais são os dados de Entrada Necessários?
2. O que devo fazer com esses dados?
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
5. Qual é a sequência de passos a serem feitas para chegar ao resultado esperado?

1: Um número gerado aleatóriamente e chutes do usuário
2: Comparar o número gerado com o número chutado até que o usuário acerte o número aleatírio
3: Apenas números inteiros entre 1 e 10.
4: Que o algoritimo compare e identifique se o número chutado é igual, maior ou menor que número aleatório
5:
'''

import random
random = random.randint(1,100)
win = False
while win == False:
  while True:
    try:
     kick = int(input("Chute um número entre 1 e 100: "))
     break
    except:
      print("Apenas números inteiros entre um e 100.")
  if kick > random:
    print("Chutou alto.")
  elif kick < random:
    print("Chutou baixo.")
  elif kick == random:
    win = True
    print("Acertou Miserável!")