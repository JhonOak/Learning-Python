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

# 7
print("Digite cinco números:\n")
cnt = 0
sma = 0
while cnt < 5:
  cnt += 1
  num = float(input())
  if cnt == 1:
    man = num - 1
  if num > man:
    man = num
  if cnt == 5:
    print(f"\nMaior número: {man}")

# 8
print("Digite cinco números:\n")
cnt = 0
sma = 0
while cnt < 5:
  cnt += 1
  num = float(input())
  sma = sma + num
  med = sma / cnt
  if cnt == 5:
    print(f"\nSoma dos números: {sma} \nMédia dos números: {med}")

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

# 15
num = int(input("Digite o número de repetições Fibonacci: "))
lst = [0, 0]
fib = 1
cnt = 0
while cnt < num:
  fib = fib + lst[cnt]
  lst.append(fib)
  cnt += 1
  print(fib)

# 16
lst = [0, 0]
fib = 1
cnt = 0
while fib < 500:
  fib = fib + lst[cnt]
  lst.append(fib)
  cnt += 1
  print(fib)

# 17
num = int(input("Digite um número para saber seu fatorial: "))
fat = 1
cnt = 0
while cnt < num:
  cnt += 1
  fat = fat * cnt
print(fat)

# 18
n = int(input("Com quantos números deseja trabalhar? "))
print()
cnt = 0
sma = 0
while cnt < n:
  cnt += 1
  num = float(input(f"{cnt}º Número: "))
  sma = sma + num
  if cnt == 1:
    man = num - 1
    men = num + 1
  if num > man:
    man = num
  if num < men:
    men = num
  if cnt == n:
    print(f"\nSoma: {sma} \nMaior: {man} \nMenor: {men}")
    
# 19
n = int(input("Com quantos números deseja trabalhar? "))
print()
cnt = 0
sum = 0
while cnt < n:
  cnt += 1
  num = float(input(f"{cnt}º Número: "))
  while not 0 <= num <= 1000:
    num = float(input(f"Número inválido! Digite um número de 0 a 1000\n{cnt}º Número: "))
  sum = sum + num
  if cnt == 1:
    max = num - 1
    min = num + 1
  if num > max and 0 <= num <= 1000:
    max = num
  if num < min and 0 <= num <= 1000:
    min = num
  if cnt == n:
    print(f"\nSoma: {sum} \nMaior: {max} \nMenor: {min}")

# 20
while True:
  num = int(input("Digite um número para saber seu fatorial: "))
  fat = 1
  cnt = 0
  while cnt < num:
    cnt += 1
    fat = fat * cnt
  if 0 <= num < 16:
    print(f"{fat}\n")
  elif num < 0 or num >= 16:
    print("Apenas números de 0 a 15\n")

# 21
num = int(input("Digite um número para verificar se é Primo: "))
cnt = 0
div = 0
while cnt < num:
  cnt += 1
  prm = num % cnt
  if prm == 0:
    div += 1
  if cnt == num and div > 2:
    print(f"\n{num} não é Primo")
  elif cnt == num and div == 2:
    print(f"\n{num} é Primo")

# 22
num = int(input("Digite um número para verificar se é Primo: "))
lst = []
cnt = 0
div = 0
while cnt < num:
  cnt += 1
  prm = num % cnt
  if prm == 0:
    div += 1
    lst.append(cnt)
  if cnt == num and div > 2:
    print(f"\n{num} não é Primo, pois é divisivel por:")
    print(*lst, sep=', ')
  elif cnt == num and div == 2:
    print(f"\n{num} é Primo")

# 23
n = int(input("Digite um número para verificar os Primos de 1 a N: "))
lst = [1]
num, cnt, div, qdv = [0, 0, 0, 0]
while num < n:
  num += 1
  while cnt < num:
    cnt += 1
    prm = num % cnt
    qdv += 1
    if prm == 0:
      div += 1
    if num == cnt and div == 2:
      lst.append(num)
      cnt = 0
      div = 0
      break
    elif num == cnt and div != 2:
      cnt = 0
      div = 0
      break
  if num == n:
    print(f"\nDe 1 a {n} os seguintes números são primos:")
    print(*lst, sep=', ')
    print(f"\nForam executadas {qdv} divisões para encontras estes Primos.")

# 24
n = int(input("Insira o número de termos da média: "))
cnt = 0
sma = 0
while cnt < n:
  cnt += 1
  num = float(input(f"{cnt}º Termo: "))
  sma = sma + num
  med = sma / n
  if cnt == n:
    print(f"\nMédia: {med}")
    
# 25
n = int(input("Insira a idade dos participantes: "))
cnt = 0
sma = 0
rst = "Esta turma é "
while cnt < n:
  cnt += 1
  num = float(input(f"{cnt}º Idade: "))
  sma = sma + num
  med = sma / n
  if 0 < med <= 25.26 and n == cnt:
    print(f"\n{rst}Jovem")
  elif 25.26 < med <= 60 and n == cnt:
    print(f"\n{rst}Adulta")
  elif med > 60 and n == cnt:
    print(f"\n{rst}Idosa")

# 26
elt = int(input("Qual o número total de Eleitores? "))
print('''
Use os seguintes códigos para votar:
1 - Candidato 1
2 - Candidato 2
3 - Candidato 3
''')
cnt = 0
cd1, cd2, cd3, win = [0, 0, 0, 0]
nm1, nm2, nm3, nmv = ["Candidato 1", "Candidato 2", "Candidato 3", 0]
while cnt < elt:
  cnt += 1
  vto = int(input(f"{cnt}º Eleitor, digite seu voto: "))
  if vto == 1:
    cd1 += 1
  elif vto == 2:
    cd2 += 1
  elif vto == 3:
    cd3 += 1
  elif not 1 <= vto <= 3:
    print("Voto inválido, use apenas os códigos informados.")
    cnt -= 1
  if elt == cnt and cd1 > win:
    win = cd1
    nmv = nm1
  if elt == cnt and cd2 > win:
    win = cd2
    nmv = nm2
  if elt == cnt and cd3 > win:
    win = cd3
    nmv = nm3
  if elt == cnt:
    print(f"{nmv} venceu a eleição.")

# 29
qnt = int(input("Qual a quantidade de itens? "))
prc = 1.99
tot, cnt = [0, 0]
while cnt < qnt:
  cnt += 1
  tot = tot + prc
  if cnt == qnt:
    print(f"\nValor a ser pago: R$ {tot:.2f}")

# 30
qnt = int(input("Quantos pães? "))
prc = 0.18
tot, cnt = [0, 0]
while cnt < qnt:
  cnt += 1
  tot = tot + prc
  if cnt == qnt:
    print(f"\nValor a ser pago: R$ {tot:.2f}")

# 32
num = cnt = int(input("Fatorial: "))
lst = []
fat = 1
cnt += 1
while cnt > 1:
  cnt -= 1
  fat = fat * cnt
  lst.append(cnt)
  if cnt == 1:
    print(f"{num}! = ", end='') 
    print(*lst, sep=' x ', end='')
    print(f" = {fat}")
    
# 34
num = int(input("Digite um número para verificar se é Primo: "))
cnt = 0
div = 0
while cnt < num:
  cnt += 1
  prm = num % cnt
  if prm == 0:
    div += 1
  if cnt == num and div > 2:
    print(f"\n{num} não é Primo")
  elif cnt == num and div == 2:
    print(f"\n{num} é Primo")
    
# 35
n = int(input("Digite um número para verificar os Primos de 1 a N: "))
lst = [1]
num, cnt, div, qdv = [0, 0, 0, 0]
while num < n:
  num += 1
  while cnt < num:
    cnt += 1
    prm = num % cnt
    qdv += 1
    if prm == 0:
      div += 1
    if num == cnt and div == 2:
      lst.append(num)
      cnt = 0
      div = 0
      break
    elif num == cnt and div != 2:
      cnt = 0
      div = 0
      break
  if num == n:
    print(f"\nDe 1 a {n} os seguintes números são primos:")
    print(*lst, sep=', ')
    print(f"\nForam executadas {qdv} divisões para encontras estes Primos.")
    
# 49
n = int(input())
lst = []
cnt = 0
trm = [1, 1]
while cnt < n:
  lst.append(str(f"{trm[0]}/{trm[1]}"))
  cnt += 1
  trm[0] += 1
  trm[1] += 2
  if cnt == n:
    print(lst)  
