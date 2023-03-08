# 1
vet = [1, 2, 3, 4, 5]
print(vet)

# 2
vet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vet.reverse()
print(vet)

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

# 3
vet = [9, 7.5, 8, 7.25]
med = sum(vet) / 4
print(vet, med)

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

