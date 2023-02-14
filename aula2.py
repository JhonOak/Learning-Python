# if, elif e else
'''
E ae Jonathan, bora dar uma saída hoje?
Se eu terminar meu trabalho, eu consigo.
'''

work_finished = False
if work_finished == True:
  print("Opa! Borda dar uma saída.")
else:
  print("Não posso sair agora.")

'''
Ei, você consegue me ajudar a mover essas caixas lá pra fora hoje a Tarde?
Sim, mas se não der, pede pro meu irmão te ajudar.
'''

free_to_help = True
if free_to_help == True:
  print("Ok, posso ajudar hoje sim.")
else:
  print("Peça pro meu irmão te ajudar.")


'''Eu cheguei atrasado na aula, ainda posso entrar?
Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrário irá tomar uma suspensão.'''

print("Quantas vezes chegou já chegou atrasado na minha aula? Não adianta mentir.")
times_late = input("Resposta: ")
if int(times_late) >= 3:
  print("Está suspenso, fora da minha sala de aula!")
elif int(times_late) == 1:
  print("Entra, mas caso atrase mais duas vezes, será suspenso.")
elif int(times_late) == 2:
  print("Entra, se atrasar mais uma vez, suspensão!")
else:
  print("Pode entrar.")


first_value = input("Insira o primeiro valor: ")
second_value = input("Insira o segundo valor: ")
if int(first_value) > int(second_value):
  print("O primeiro valor é maior.")
elif int(first_value) == int(second_value):
  print("Os valores são iguais")
else:
  print("O segundo valor é maior.")












