# Laços de Repetição + Lista
'''
print("carregando")
print("carregando")
print("carregando")
'''

for word in range(1,4):
  print("carregando")

for item in range(1,21):
  print(item)
for item in range(1,20,2):
  print(item)


names = ["Jhon","Will","Well","Jude","Cris","Gabi","Edu"]

for name in names:
  print(name)

# Problema 1 a N - Imprima valores de 1 a N

max_number = int(input("Insira o número máximo: "))
initial_value = 1
for number in range(initial_value,max_number + 1):
  print (number)