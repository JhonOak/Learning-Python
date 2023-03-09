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
    
