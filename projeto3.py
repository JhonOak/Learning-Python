'''
Projeto - Medidor de Velocidade

Levando em consideração a velocidade máxima permitida de 80km/h em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ela tomou uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km/h acima, deve exibir "levou multa leve", caso esteja entre 11 a 20km/h acima da velocidade máxima, exibir "levou multa grave", e caso esteja acima de 20km/h acima da velocidade máxima, exibir "levou multa gravíssima"

# Método 5Q's para montar um algoritimo:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o programa.)

1. Quais são os dados de Entrada Necessários?
2. O que devo fazer com esses dados?
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
5. Qual é a sequência de passos a serem feitas para chegar ao resultado esperado?

1: Velocidade máxima e velocidade fornecida pelo usuário
2: Comparar a velocidade fornecida pelo usuário com a velocidade máxima e exibir se não foi dado multa, multa leve, grave ou gravíssima.
3: Dados apenas em números.
4: Identificar se houve multa e caso sim qual multa
5:
'''

max_speed = 80
while True:
  try:
    speed = int(input("Qual foi a velocidade do motorista? "))
    break
  except:
    print("Digite apenas números.")
if speed <= max_speed:
  print("Não houve multa.")
elif speed > max_speed and speed <= max_speed + 10:
  print("Levou multa leve")
elif speed > max_speed + 10 and speed <= max_speed + 20:
  print("Levou multa grave")
elif speed > max_speed + 20:
  print("Levou multa gravíssima")

'''
Desenvolvimento para Desktop
Desenvolvimento Web
Desenbolvimento de App Mobile
Automação de Processos
Análise de Dados
'''