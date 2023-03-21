# Exercícios com Listas
# https://wiki.python.org.br/ExerciciosListas

# 1
vet = [1, 2, 3, 4, 5]
print(vet)

# 2
vet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vet.reverse()
print(vet)

'''# 3
vet = [9, 7.5, 8, 7.25]
med = sum(vet) / 4
print(vet, med)'''

# 3
print("Digite quatro notas:")
vet = []
cnt, sma = 0, 0
while cnt < 4:
  vet.append(float(input()))
  sma = sma + vet[cnt]
  cnt += 1
print("\nNotas digitadas: ", end='')
print(*vet, sep=', ')
print(f"Média: {sma / 4}")

# 4
print("Digite dez caracteres:")
cs = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vet, vcs = [], []
cnt, qcs = 0, 0
while cnt < 10:
  vet.append(str(input()))
  if vet[cnt] in list(cs):
    qcs += 1
    vcs.append(vet[cnt])
  cnt += 1
print(f"\nQuantidade de consoantes: {qcs}\nLista de consoantes: ", end='')
print(*vcs, sep=', ')



# 5
lst, par, imp = [], [], []
cnt = 0
for i in range(1, 60, 3):
  lst.append(i)
while cnt < len(lst):
  rst = lst[cnt] % 2
  if rst == 0:
    par.append(lst[cnt])
  elif rst != 0:
    imp.append(lst[cnt])
  cnt += 1
print(f"{lst}\n{par}\n{imp}")

# 6
cnt = [0, 0]
vet = []
sma = 0
while cnt[0] < 10:
  cnt[0] += 1
  cnt[1] = 0
  if cnt[0] > 1:
    print()
  while cnt[1] < 4:
    cnt[1] += 1
    nta = int(input(f"Digite a {cnt[1]}ª nota do {cnt[0]}º aluno: "))
    sma = sma + nta
    if cnt[1] == 4:
      if sma / 4 >= 7:
        vet.append(sma / 4)
      sma = 0
print(f"\n{len(vet)} dos 10 Alunos ficaram com média igual ou maior que 7.")

# 8 t erro
cnt = 0
vet_i, vet_a = [], []
while cnt < 5:
  cnt += 1
  idd = int(input(f"Digite a idade da {cnt[0]}ª Pessoa: "))
  vet_i.append(idd)
  alt = float(input(f"Digite a altura da {cnt[0]}ª Pessoa: "))
  vet_a.append(alt)
print(f"{vet_i}\n{vet_a}")

# 9
import random
vet_a, vet_b = [], []
cnt = 0
while cnt < 10:
  cnt += 1
  num = random.randint(1, 10)
  vet_a.append(num)
  num = num ** 2
  vet_b.append(num)
print(f"{vet_a}\n{vet_b}\n{sum(vet_b)}")

# 10
import random
vet_a, vet_b, vet_c = [], [], []
cnt = 0
while cnt < 10:
  cnt += 1
  num = random.randint(0, 9)
  vet_a.append(num)
  vet_c.append(num)
  num = random.randint(0, 9)
  vet_b.append(num)
  vet_c.append(num)
print(f"{vet_a}\n{vet_b}\n{vet_c}")

# 11
import random
vet_a, vet_b, vet_c, vet_d = [], [], [], []
cnt = 0
while cnt < 10:
  cnt += 1
  num = random.randint(0, 9)
  vet_a.append(num)
  vet_d.append(num)
  num = random.randint(0, 9)
  vet_b.append(num)
  vet_d.append(num)
  num = random.randint(0, 9)
  vet_c.append(num)
  vet_d.append(num)
print(f"{vet_a}\n{vet_b}\n{vet_c}\n{vet_d}")

# 12
import random
cnt, alt, cnt_a = 0, 0, 0
vet_i, vet_a = [], []
while cnt < 30:
  cnt += 1
  idd = random.randint(12, 17)
  vet_i.append(idd)
  while alt < 1.4:
    alt = 1 + random.random()
  vet_a.append(round(alt, 2))
  alt = 0
med = round(sum(vet_a) / 30, 2)
cnt = 0
while cnt < 30:
  if vet_i[cnt] > 13 and vet_a[cnt] < med:
    cnt_a += 1
  cnt += 1
print(f"{vet_i}\n{vet_a}\n{med}\n{cnt_a}")

# 13
import random
cnt = 0
vet, vet_m = [], ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
while cnt < 12:
  cnt += 1
  tmp = random.randint(19, 31) + round(random.random(), 2)
  vet.append(tmp)
med = round(sum(vet) / 12, 2)
cnt = 0
while cnt < 12:
  if cnt == 0:
    print(f"Meses com Temperatura acima da Média ({med}ºC): \n\n")
  if vet[cnt] > med:
    print(f"{vet_m[cnt]} - {vet[cnt]}ºC\n")
  cnt += 1
print()

# 15
import random
vet = []
cnt = [0, 0, 0, 0]
loop = True
while loop is True:
  num = random.randint(-1, 10)
  if num == -1:
    loop = False
  elif num != -1:
    cnt[0] += 1
    vet.append(num)
sma = sum(vet)
med = round(sma / cnt[0])
while cnt[1] < cnt[0]:
  if vet[cnt[1]] > med:
    cnt[2] += 1
  if vet[cnt[1]] < 7:
    cnt[3] += 1
  cnt[1] += 1
print(f"a) Foram lidos {cnt[0]} valores.\n")
print ("b) ", end='')
print(*vet, sep=', ', end='\n')
vet.reverse()
print(f"\nc)")
print(*vet, sep='\n')
print(f"\nd) Soma dos valores: {sma}\n")
print(f"e) Média dos valores: {med}\n")
print(f"f) Quantidade de valores acima da média: {cnt[2]}\n")
print(f"g) Quantidade de valores abaixo de 7: {cnt[3]}\n")
print("g) Encerre o programa com uma mensagem")

# 16
import random, math
zny, fnc = 200, 10
vet = []
cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while cnt[0] < fnc:
  cnt[0] += 1
  cms = round(random.randint(0, 10000) * 0.09, 2)
  pag = zny + cms
  vet.append(pag)
  i = math.ceil(cms / 100)
  cnt[i] += 1
print(f'''Quantidade de funcionários: {fnc}

Quantidades que receberam determinadas faixas de pagamento: 

$200 - $299   : {cnt[1]}
$300 - $399   : {cnt[2]}
$400 - $499   : {cnt[3]}
$500 - $599   : {cnt[4]}
$600 - $699   : {cnt[5]}
$700 - $799   : {cnt[6]}
$800 - $899   : {cnt[7]}
$900 - $999   : {cnt[8]}
Acima de $1000: {cnt[9]}

{vet}''')

# extra - password
import string
ok = False
tst = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
while ok == False:
  vrf = [0, 0, 0, 0]
  psw = str(input("Defina sua senha: "))
  vet = [i for i in psw]
  crt, cnt = len(vet), 0
  while cnt < crt:
    tnc = 0
    while tnc < 4:
      if vet[cnt] in tst[tnc]:
        vrf[tnc] += 1
      tnc +=1
    cnt += 1
  if vrf[0] > 0 and vrf[1] > 0 and vrf[2] > 0 and vrf[3] > 0:
    print("\nSenha aceita, obrigado.\n")
    ok == True
  elif vrf[0] == 0 or vrf[1] == 0 or vrf[2] == 0 or vrf[0] == 0:
    print("\nSenha recusada. \nPor favor, digite uma senha contendo pelo menos uma letra minúscula, uma maiúscula, um número e um carctere especial.\n")

# 18
print("Use de 1 a 23 para votar no melhor jogador e 0 para encerrar a votação.\nEnquete: Quem foi o melhor jogador?\n")
vto = None
jgd = []
vts = []
while vto != "0":
  vto = str(input("Número do jogador: "))
  if vto not in jgd and vto != "0":
    jgd.append(vto)
    vts.append(1)
  elif vto in jgd:
    vts[jgd.index(vto)] += 1
print(jgd,vts)
