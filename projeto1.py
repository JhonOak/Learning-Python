# Fatorial de um Número
'''
Crie um programa que recebe um número e imprime o fatorial daquele número
# Método 5Q's para montar um algoritimo:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o programa.)

1. Quais são os dados de Entrada Necessários?
2. O que devo fazer com esses dados?
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
5. Qual é a sequência de passos a serem feitas para chegar ao resultado esperado?

1: Um número.
2: Multiplicar por cada número anterior ao número escolhido até o número 1.
3: Apenas números inteiros não negativos.
4: Imprimir o fatorial do número escolhido.
5:
'''

while True:
  try:
    number = int(input("Qual número deseja fatorar? "))
    break
  except:
    print("Um NÚMERO seu idiota!")

factorial = 1
if number > 0:
  for previous in reversed(range(1,number+1)):
    factorial = factorial * previous
  print(factorial)
elif number == 0:
  print(factorial)
else:
  print("Apenas números inteiros não negativos.")
