# Exercícios de Estrutura de Repetição:
# https://wiki.python.org.br/EstruturaDeRepeticao

# 1
nta = float(input("Digite uma nota de 0 a 10: "))
while 0 > nta > 10:
  nta = float(input('''Valor inválido!
Digite uma nota de 0 a 10: '''))

# 2
usr = str(input("Digite seu nome de usuário: "))
psw = str(input("Senha: "))
while psw == usr:
  usr = str(input('''
Erro, a senha não pode ser igual ao usuário.
Digite seu nome de usuário: '''))
  psw = str(input("Senha: "))

# 3
nme = str(input('''Digite as informações requisitadas. 

Nome: '''))
while len(nme) < 4:
  nme = str(input('''Nome inválido, deve ter mais de três caracteres.

Nome: '''))
idd = int(input("Idade: "))
while 0 > idd > 150:
  idd = str(input('''Idade inválida, deve ser de 0 a 150.

Idade: '''))
slr = float(input("Salário: "))
while slr < 0:
  slr = float(input('''Salário inválido, deve ser maior que zero.

Salário: '''))
sxo = str(input("Sexo (Use f ou m): "))
while sxo != "f" and sxo != "m":
  sxo = str(input('''Sexo inválido, use apenas as seguintes letras:
f - Feminino
m - Masculino

Sexo: '''))
if sxo == "f":
  gen = "a"
elif sxo == "m":
  gen = "o"
ecv = str(input("Estado Civil (Use s, c, v ou d): "))
while ecv != "s" and ecv != "c" and ecv != "v" and ecv != "d":
  ecv = str(input(f'''Estado Civil inválido, use apenas as seguintes letras:
s - Solteir{gen}
c - Casad{gen}
v - Viuv{gen}
d - Divorciad{gen}

Estado Civil: '''))

# 4
pop = [80000, 200000, 0.03, 0.015, 0]
while pop[0] < pop[1]:
  pop[4] += 1
  pop[0] = pop[0] + (pop[0] * pop[2])
  pop[1] = pop[1] + (pop[1] * pop[3])
print(f"Levará {pop[4]} anos para População do País A ultrapassar a do País B.")

# 5 Incompleto, pulei, volto depois kkk
#pop = [float(input("Digite a População do País A: ")), float(input("Digite a População do País B: ")), float(input("Digite em Porcentagem a Taxa de Crescimento do País A: ")), float(input("Digite em Porcentagem a Taxa de Crescimento do País B: ")), 0]
# while pop[0] < pop[1]:
#  pop[4] = pop[4] + 1
#  pop[0] = pop[0] + (pop[0] * pop[2] / 100)
#  pop[1] = pop[1] + (pop[1] * pop[3] / 100)
#print(f"Levará {pop[4]} anos para População do País A ultrapassar a do País B.")

while True:
  txt = ["A", "B", "Digite a População do País ", "Digite em Porcentagem a Taxa de Crescimento do País "]
  pop = [float(input(f"{txt[2]}{txt[0]}: ")), float(input(f"{txt[2]}{txt[1]}: ")), float(input(f"{txt[3]}{txt[0]}: ")), float(input(f"{txt[3]}{txt[0]}: ")), 0]
  if pop[0] < pop[1] and pop[2] < pop[3]:
    print("País A nunca vai ultrapassar o País B com uma Taxa de Crescimento menor.")
  elif pop[0] > pop[1] and pop[2] > pop[3]:
    print("País B nunca vai ultrapassar o País A com uma Taxa de Crescimento menor.")
  pop[4] = pop[4] + 1
  pop[0] = pop[0] + (pop[0] * pop[2] / 100)
  pop[1] = pop[1] + (pop[1] * pop[3] / 100)
  if pop[0] < pop[1] and pop[2] > pop[3]:
    print(f"Levará {pop[4]} anos para População do País A ultrapassar a do País B.")
  elif pop[0] > pop[1] and pop[2] < pop[3]:
    print(f"Levará {pop[4]} anos para População do País B ultrapassar a do País A.")
    
 # 6
num = 0
while num < 20:
  num += 1
  print(num, end = ' ') # <- Exibe na horizontal       print(num) <- Exibe na vertical
  
# 9
for num in range(1, 50, 2):
  print(num)
  
# 10
n = [int(input("Digite o 1º número:")), int(input("Digite o 2º número:"))]
for num in range(n[0], n[1]+1):
  print(num)
 
# 11
n = [int(input("Digite o 1º número: ")), int(input("Digite o 2º número: "))]
sum = 0
for num in range(n[0], n[1]+1):
  sum += num
  print(num)
print(f"Soma dos números gerados: {sum}") 

# 12
num = int(input("Digite um número no qual deseja saber a tabuada: "))
cnt = 0
while cnt < 10:
  cnt += 1
  tab = num * cnt
  print(f"{num} x {cnt} = {tab}")
  
# 13
num = [int(input("Digite o número base: ")), int(input("Digite o expoente: "))]
mlt = 1
cnt = 0
while cnt < num[1]:
  cnt += 1
  mlt = mlt * num[0]
print(mlt)

# 14
print("Digite a seguir dez números inteiros:")
cnt = [0, 0, 0]
lst = []
while cnt[2] < 10:
  lst.append(int(input()))
  poi = lst[cnt[2]] % 2
  if poi == 0:
    cnt[0] += 1
  elif poi == 1:
    cnt[1] += 1
  cnt[2] += 1
print(f"{cnt[0]} Números Pares e {cnt[1]} Impares")
