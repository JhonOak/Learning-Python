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

