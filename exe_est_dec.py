# Exercícios de Estrutura de Decisão
# https://wiki.python.org.br/EstruturaDeDecisao

# 1 - Exiba o maior de dois números
num_1 = float(input("Digite um número: "))
num_2 = float(input("Agora o segundo número: "))
if num_1 > num_2:
    print("O maior número é:", num_1)
elif num_1 < num_2:
    print("O maior número é:", num_2)
else:
    print("Os números são iguais")

# 2 - Exiba se o número é positivo ou negativo
num = float(input("Digite um número positivo ou negativo: "))
if num > 0:
    print(num, "é positivo")
elif num < 0:
    print(num, " é negativo")
else:
    print("Zero é um número não positivo ou negativo")

# 3 - Exiba Masculino e Feminino
sexo = input("Digite seu sexo utilizando F ou M: ")
if sexo == "F" or sexo == "f":
    print("Feminino")
elif sexo == "M" or sexo == "m":
    print("Masculino")
else:
    print("Sexo inválido")

# 4 - Exiba se é vogal ou consoante
vog = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
con = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "B",
       "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
letra = input("Digite uma letra: ")
if letra in vog:
    print("A letra", letra, "é uma vogal")
elif letra in con:
    print("A letra", letra, "é uma consoante")
else:
    print("Caractere inválido")

# 5 - Exiba Aprovado, Reprovado ou Aprovado com empenho com base na média
sem_1 = float(input("Qual foi a nota do 1º Semestre? "))
sem_2 = float(input("Qual foi a nota do 2º Semestre? "))
med = (sem_1 + sem_2) / 2
if med == 10:
    print("Aprovado com Empenho!")
elif med >= 7:
    print("Aprovado")
elif med < 7:
    print("Reprovado")
else:
    print("Entrada inválida")

# 6 - Exiba o maior entre três numeros
num_1 = float(input("Digite o 1º número a ser comparado: "))
num_2 = float(input("Digite o 2º número a ser comparado: "))
num_3 = float(input("Digite o 3º número a ser comparado: "))
if num_1 >= num_2 and num_1 >= num_3:
    print(num_1, "foi o maior número dos três.")
elif num_2 >= num_1 and num_2 >= num_3:
    print(num_2, "foi o maior número dos três.")
elif num_3 >= num_1 and num_3 >= num_2:
    print(num_3, "foi o maior número dos três.")

# 7 - Exiba o maior e o menor entre três numeros
num_1 = float(input("Digite o 1º número a ser comparado: "))
num_2 = float(input("Digite o 2º número a ser comparado: "))
num_3 = float(input("Digite o 3º número a ser comparado: "))
if num_1 >= num_2 and num_1 >= num_3 and num_2 <= num_1 and num_2 <= num_3:
    print(num_1, "foi o maior e", num_2, "foi o menor.")
elif num_1 >= num_2 and num_1 >= num_3 and num_3 <= num_1 and num_3 <= num_2:
    print(num_1, "foi o maior e", num_3, "foi o menor.")
elif num_2 >= num_1 and num_2 >= num_3 and num_1 <= num_2 and num_1 <= num_3:
    print(num_2, "foi o maior e", num_1, "foi o menor.")
elif num_2 >= num_1 and num_2 >= num_3 and num_3 <= num_1 and num_3 <= num_2:
    print(num_2, "foi o maior e", num_3, "foi o menor.")
elif num_3 >= num_1 and num_3 >= num_2 and num_1 <= num_2 and num_1 <= num_3:
    print(num_3, "foi o maior e", num_1, "foi o menor.")
elif num_3 >= num_1 and num_3 >= num_2 and num_2 <= num_1 and num_2 <= num_3:
    print(num_3, "foi o maior e", num_2, "foi o menor.")
elif num_1 == num_2 and num_2 == num_3:
    print(num_1, "foi o maior e o menor número, pois os três são iguais.")

# 8 - Exiba o produto com menor preço
pro_1 = float(input("Qual o preço do 1º produto? "))
pro_2 = float(input("Qual o preço do 2º produto? "))
pro_3 = float(input("Qual o preço do 3º produto? "))
if pro_1 < pro_2 and pro_1 < pro_3:
    print("Você deve comprar o 1º produto")
elif pro_2 < pro_1 and pro_2 < pro_3:
    print("Você deve comprar o 2º produto")
elif pro_3 < pro_1 and pro_3 < pro_2:
    print("Você deve comprar o 3º produto")
elif pro_1 == pro_2:
    print("Você deve comprar o 1º ou 2º produto, pois são o mesmo preço")
elif pro_1 == pro_3:
    print("Você deve comprar o 1º ou 3º produto, pois são o mesmo preço")
elif pro_2 == pro_3:
    print("Você deve comprar o 2º ou 3º produto, pois são o mesmo preço")
elif pro_1 == pro_2 and pro_1 == pro_3:
    print("Você pode comprar qualquer dos produtos, pois os preços são iguais")

# 9 - Peça e exiba três números em ordem decrescente
num_1 = float(input("Digite o 1º número a ser ordenado: "))
num_2 = float(input("Digite o 2º número a ser ordenado: "))
num_3 = float(input("Digite o 3º número a ser ordenado: "))
if num_1 >= num_2 and num_1 >= num_3 and num_2 >= num_3:
    print("Em ordem decrecente:", num_1, ",", num_2, "e", num_3)
elif num_1 >= num_2 and num_1 >= num_3 and num_3 >= num_2:
    print("Em ordem decrecente:", num_1, ",", num_3, "e", num_2)
elif num_2 >= num_1 and num_2 >= num_3 and num_1 >= num_3:
    print("Em ordem decrecente:", num_2, ",", num_1, "e", num_3)
elif num_2 >= num_1 and num_2 >= num_3 and num_3 >= num_1:
    print("Em ordem decrecente:", num_2, ",", num_3, "e", num_1)
elif num_3 >= num_1 and num_3 >= num_2 and num_1 >= num_2:
    print("Em ordem decrecente:", num_3, ",", num_1, "e", num_2)
elif num_3 >= num_1 and num_3 >= num_2 and num_2 >= num_1:
    print("Em ordem decrecente:", num_3, ",", num_2, "e", num_1)

# 10 - Exiba mensagem de bom dia, tarde ou noite dependendo do turno.
print("Digite M para Matutino")
print("Digite V para Vespertino")
print("Digite N para Noturno")
turno = input("Em qual turno você estuda? ")
if turno == "m" or turno == "M":
    print("Bom dia!")
elif turno == "v" or turno == "V":
    print("Boa tarde!")
elif turno == "n" or turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")

# 11 - Aumento de salário nas Organizaçes Tabajara
sal = float(input("Quanto é o seu salário?" ))
aum = [0.2,0.15,0.1,0.05]
sal_a = [sal * aum[0], sal * aum[1], sal * aum[2], sal * aum[3]]
if sal > 0 and sal <= 280:
    print("Seu salário era de R$", sal)
    print("Você recebeu um aumento de", aum[0] * 100, "%")
    print("O valor do seu aumento foi de R$", sal_a[0])
    print("Seu salário agora é de R$", sal + sal_a[0])
elif sal > 280 and sal <= 700:
    print("Seu salário era de R$", sal)
    print("Você recebeu um aumento de", aum[1] * 100, "%")
    print("O valor do seu aumento foi de R$", sal_a[1])
    print("Seu salário agora é de R$", sal + sal_a[1])
elif sal > 700 and sal <= 1500:
    print("Seu salário era de R$", sal)
    print("Você recebeu um aumento de", aum[2] * 100, "%")
    print("O valor do seu aumento foi de R$", sal_a[2])
    print("Seu salário agora é de R$", sal + sal_a[2])
elif sal > 1500:
    print("Seu salário era de R$", sal)
    print("Você recebeu um aumento de", aum[3] * 100, "%")
    print("O valor do seu aumento foi de R$", sal_a[3])
    print("Seu salário agora é de R$", sal + sal_a[3])
else:
    print("Valor inválido")

# 12 - Programa para calculo de folha de pagamento
vlr_hr = float(input("Qual o valor da sua hora de trabalho? "))
hr_trb = float(input("Quantas horas você trabalha por mês? "))
sal = round(vlr_hr * hr_trb, 2)
ir = [round(0.05 * sal, 2), round(0.1 * sal, 2), round(0.2 * sal, 2)]
inss = round(0.1 * sal, 2)
fgts = round(0.11 * sal, 2)
desc = [round(inss + ir[0], 2), round(inss + ir[1], 2), round(inss + ir[2], 2)]
sal_l = [round(sal - inss - ir[0], 2), round(sal - inss - ir[1], 2), round(sal - inss - ir[2], 2), round(sal - inss, 2)]
if sal > 0 and sal <= 900:
    print("+ Salário Bruto     : R$", sal)
    print("- IR                : Isento")
    print("- INSS (10%)        : R$", inss)
    print("- FGTS (11%)        : R$", fgts)
    print("- Total de Descontos: R$", inss)
    print("= Salário Líquido   : R$", sal_l[3])
elif sal > 900 and sal <= 1500:
    print("+ Salário Bruto     : R$", sal)
    print("- IR    (5%)        : R$", ir[0])
    print("- INSS (10%)        : R$", inss)
    print("- FGTS (11%)        : R$", fgts)
    print("- Total de Descontos: R$", desc[0])
    print("= Salário Líquido   : R$", sal_l[0])
elif sal > 1500 and sal <= 2500:
    print("+ Salário Bruto     : R$", sal)
    print("- IR   (10%)        : R$", ir[1])
    print("- INSS (10%)        : R$", inss)
    print("- FGTS (11%)        : R$", fgts)
    print("- Total de Descontos: R$", desc[1])
    print("= Salário Líquido   : R$", sal_l[1])
elif sal > 2500:
    print("+ Salário Bruto     : R$", sal)
    print("- IR   (20%)        : R$", ir[2])
    print("- INSS (10%)        : R$", inss)
    print("- FGTS (11%)        : R$", fgts)
    print("- Total de Descontos: R$", desc[2])
    print("= Salário Líquido   : R$", sal_l[2])
else:
    print("Valor inválido")

# 13 - Programa que le numero e exibe o dia da semana
num = int(input("Digite de 1 a 7 para exibir dias da semana: "))
dia = [0, "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
if num >= 1 and num <= 7:
    print(dia[num])
else:
    print("Valor inválido")

# 14 - Notas semestrais, média, conceito e aprovado/reprovado
sem = [float(input("Qual foi a 1ª nota no Semestre? ")), float(input("Qual foi a 2ª nota no Semestre? "))]
sem_m = round((sem[0] +sem[1]) / 2, 2)
cnct = ["A", "B", "C", "D", "E"]
aprp = ["Aprovado", "Reprovado"]
if sem_m >= 9 and sem_m <= 10:
  print("Suas notas foram:", sem[0], "e", sem[1])
  print("Sua média foi   :", sem_m)
  print("Seu conceito foi:", cnct[0])
  print("Você foi        :", aprp[0])
elif sem_m >= 7.5 and sem_m < 9:
  print("Suas notas foram:", sem[0], "e", sem[1])
  print("Sua média foi   :", sem_m)
  print("Seu conceito foi:", cnct[1])
  print("Você foi        :", aprp[0])
elif sem_m >= 6 and sem_m < 7.5:
  print("Suas notas foram:", sem[0], "e", sem[1])
  print("Sua média foi   :", sem_m)
  print("Seu conceito foi:", cnct[2])
  print("Você foi        :", aprp[0])
elif sem_m >= 4 and sem_m < 6:
  print("Suas notas foram:", sem[0], "e", sem[1])
  print("Sua média foi   :", sem_m)
  print("Seu conceito foi:", cnct[3])
  print("Você foi        :", aprp[1])
elif sem_m >= 0 and sem_m < 4:
  print("Suas notas foram:", sem[0], "e", sem[1])
  print("Sua média foi   :", sem_m)
  print("Seu conceito foi:", cnct[4])
  print("Você foi        :", aprp[1])
else:
  print("Valor inválido")

# 15 - Peça três lados de um triângulo, exiba se é possível e qual é o tipo de triângulo
print("Digite os três lados do triângulo: ")
tri = [float(input()), float(input()), float(input())]
if tri[0] + tri[1] > tri[2] and tri[0] + tri[2] > tri[1] and tri[1] + tri[2] > tri[0]:
  print("É possível um triângulo com esses valores")
  if tri[0] == tri[1] == tri[2]:
    print("Tipo de Triângulo: Equilátero")
  elif tri[0] == tri[1] or tri[0] == tri[2] or tri[1] == tri[2]:
    print("Tipo de Triângulo: Isósceles")
  elif tri[0] != tri[1] != tri[2]:
    print("Tipo de Triângulo: Escaleno")
elif tri[0] + tri[1] <= tri[2] or tri[0] + tri[2] <= tri[1] or tri[1] + tri[2] <= tri[0]:
  print("Não é possível um triângulo com esses valores")
else:
  print("Valores inválidos")

# 16 - Calculadora de raízes de equação do 2º grau
import math
print("Digite os valores de a, b e c para uma equação ax² + bx + c")
a = float(input())
b = float(input())
c = float(input())
delta = (b ** 2) - (4 * a * c)
x_1 = (-b + math.sqrt(delta)) / 2 * a
x_2 = (-b - math.sqrt(delta)) / 2 * a
if a == 0:
  print("Esta equação não é do segundo grau.")
elif b == 0:
  x_1 = math.sqrt(-c / a)
  x_2 = - math.sqrt(-c / a)
  print(f"As raízes desta equação são {x_1} e {x_2}.")
elif c == 0:
  x_1 = 0
  x_2 = -b / a
  print(f"As raízes desta equação são {x_1} e {x_2}.")
elif delta < 0:
  print("Esta equação não possui raizes reais.")
elif delta == 0:
  print(f"Esta equação possui apenas uma raiz, que é {x_1}.")
elif delta > 0:
  print(f"As raízes desta equação são {x_1} e {x_2}.")
else:
  print("Valores Inválidos")

# 17 - Peça um ano e exiba se é bissexto ou não
ano = int(input("Digite um ano: ")[:4])
bis = [*range(0, 10000, 4)]
if ano in bis:
    print(f"{ano} é um ano bissexto.")
elif ano not in bis:
    print(f"{ano} não é um ano bissexto.")
else:
    print("Valor inválido")

# 18 - Verificador de data válida
print("Digite uma data em formato dd/mm/aaaa: ")
dt = [int(input()[:2]), int(input()[:2]), int(input()[:4])]
dd = [*range(1, 31)]
mm = [*range(1, 12)]
aa = [*range(0, 10000)]
ab = [*range(0, 10000, 4)]
m30 = [4, 6, 9, 10]
if dt[1] in m30 and dt[0] == 31:
    print(f"{dt[0]}/{dt[1]}/{dt[2]} é uma data inválida.")
elif dt[1] == 2 and dt[0] > 28 and dt[2] not in ab or dt[1] == 2 and dt[0] > 29 and dt[2] in ab:
    print(f"{dt[0]}/{dt[1]}/{dt[2]} é uma data inválida.")
elif dt[0] in dd or dt[1] in mm or dt[2] in aa:
    print(f"{dt[0]}/{dt[1]}/{dt[2]} é uma data válida.")
elif dt[0] not in dd or dt[1] not in mm or dt[2] not in aa:
    print(f"{dt[0]}/{dt[1]}/{dt[2]} é uma data inválida.")
else:
    print("Valores inválidos")

# 19 - Leitor de centenas, dezenas e unidades
numero = str(input("Digite um número inteiro de 1 a 999: "))
num = [int(un) for un in numero]
if int(numero) < 0 or int(numero) > 999:
    print("Número inválido.")
elif num[0] > 1 and num[1] > 1 and num[2] > 1:
    print(f"{num[0]} centenas, {num[1]} dezenas e {num[2]} unidades.")
elif num[0] > 1 and num[1] > 1 and num[2] == 1:
    print(f"{num[0]} centenas, {num[1]} dezenas e {num[2]} unidade.")
elif num[0] > 1 and num[1] == 1 and num[2] > 1:
    print(f"{num[0]} centenas, {num[1]} dezena e {num[2]} unidades.")
elif num[0] == 1 and num[1] > 1 and num[2] > 1:
    print(f"{num[0]} centena, {num[1]} dezenas e {num[2]} unidades.")
elif num[0] == 1 and num[1] == 1 and num[2] == 1:
    print(f"{num[0]} centena, {num[1]} dezena e {num[2]} unidade.")
elif num[0] == 1 and num[1] == 1 and num[2] > 1:
    print(f"{num[0]} centena, {num[1]} dezena e {num[2]} unidades.")
elif num[0] == 1 and num[1] > 1 and num[2] == 1:
    print(f"{num[0]} centena, {num[1]} dezenas e {num[2]} unidade.")
elif num[0] > 1 and num[1] == 1 and num[2] == 1:
    print(f"{num[0]} centenas, {num[1]} dezena e {num[2]} unidade.")
else:
    print("Valores inválidos")
    
# 20 - Programa que lê três notas, da a média e diz se aprovado/reprovado
print("Insira suas três notas: ")
nota = [float(input("1º Nota: ")), float(input("2ª Nota: ")), float(input("3ª Nota: "))]
med = (nota[0] + nota[1] + nota[2]) / 3
sit = ["Aprovado com Distinçao!", "Aprovado.", "Reprovado."]
if med == 10:
  print(f"{sit[0]}")
elif med < 10 and med >= 7:
  print(f"{sit[1]}")
elif med < 7 and med >= 0:
  print(f"{sit[2]}")
else:
  print("Valor inválido")

# 21
sqe = int(input("Quanto deseja sacar? "))
per = False
nta = [100, 50, 10, 5, 1]
qnt = [0, 0, 0, 0, 0]
din = 0
if 10 <= sqe <= 600:
    per = True
while per is False:
    sqe = int(input('''Valor inválido.
Digite uma quantia de 10 a 600: '''))
    if 10 <= sqe <= 600:
        per = True
        break
while sqe > din:
    din = din + nta[0]
    qnt[0] = qnt[0] + 1
    if sqe < din:
        din = din - nta[0]
        qnt[0] = qnt[0] - 1
        break
while sqe > din:
    din = din + nta[1]
    qnt[1] = qnt[1] + 1
    if sqe < din:
        din = din - nta[1]
        qnt[1] = qnt[1] - 1
        break
while sqe > din:
    din = din + nta[2]
    qnt[2] = qnt[2] + 1
    if sqe < din:
        din = din - nta[2]
        qnt[2] = qnt[2] - 1
        break
while sqe > din:
    din = din + nta[3]
    qnt[3] = qnt[3] + 1
    if sqe < din:
        din = din - nta[3]
        qnt[3] = qnt[3] - 1
        break
while sqe > din:
    din = din + nta[4]
    qnt[4] = qnt[4] + 1
    if sqe < din:
        din = din - nta[4]
        qnt[4] = qnt[4] - 1
        break
if sqe == din:
    print(f'''
Notas saquadas:
{qnt[0]} de {nta[0]} Reais
{qnt[1]} de {nta[1]}  Reais
{qnt[2]} de {nta[2]}  Reais
{qnt[3]} de {nta[3]}   Reais
{qnt[4]} de {nta[4]}   Real''')

# 22 - 
num = str(input("Digite um número: "))
ip = int(num) % 2
if ip == 1:
    print(f"{num} é um número impar.")
elif ip == 0:
    print(f"{num} é um número par.")
else:
    print("Valor inválido")

# 23 - Informa se é inteiro ou decimal
num = float(input("Digite um número inteiro ou decimal: "))
nua = round(num)
if num == nua:
    print(f"{int(num)} é um número inteiro.")
elif num != nua:
    print(f"{num} é um número decimal.")
else:
    print("Valor inválido")
    
# 24 - Programa que recebe dois números, faz operação desejada e fornece informações dos números
num = [float(input("Digite o 1º Número: ")), float(input("Digite o 2º Número: "))]
op = int(input('''

Qual operação deseja realizar?

0 - Soma
1 - Subtração
2 - Multiplicação
3 - Divisão

Operação: '''))

if op == 0:
    rst = num[0] + num[1]
    op_t = str("+")
elif op == 1:
    rst = num[0] - num[1]
    op_t = str("-")
elif op == 2:
    rst = num[0] * num[1]
    op_t = str("*")
elif op == 3:
    rst = num[0] / num[1]
    op_t = str("/")
else:
    print("Opção inválida")

ip = int(rst) % 2
if ip == 1:
    ip_t = str("impar")
elif ip == 0:
    ip_t = str("par")

nua = round(rst)
if nua == rst:
    nua_t = str("inteiro")
    rst = int(rst)
elif nua != rst:
    nua_t = str("decimal")
    ip_t = str("não par ou impar")

pon = str("positivo")
if rst == 0:
    pon = str("nulo")
elif rst < 0:
    pon = str("negativo")

print(f'''{num[0]} {op_t} {num[1]} = {rst}
{rst} é um número {ip_t}, {pon} e {nua_t}.''')

# 25
import time
print("Responda as perguntas dizendo somente a verdade:")
time.sleep(3)
pnts = 0
txt = "Você foi considerado como: "
jlgt = ["Inocente", "Suspeito", "Cúmplice", "Assassino"]
prgt = str(input('''
Telefonou para vítima?
'''))
if prgt == "sim" or prgt == "Sim":
  pnts = pnts + 1
prgt = str(input('''
Esteve no local do crime?
'''))
if prgt == "sim" or prgt == "Sim":
  pnts = pnts + 1
prgt = str(input('''
Mora perto da vítima?
'''))
if prgt == "sim" or prgt == "Sim":
  pnts = pnts + 1
prgt = str(input('''
Devia para a vítima?
'''))
if prgt == "sim" or prgt == "Sim":
  pnts = pnts + 1
prgt = str(input('''
Já trabalhou com a vítima?
'''))
time.sleep(1)
print('''
Calculando sua participação no crime...
''')
time.sleep(3)
if prgt == "sim" or prgt == "Sim":
  pnts = pnts + 1
if 0 >= pnts <= 1:
  print(f"{txt}{jlgt[0]}")
elif pnts == 2:
  print(f"{txt}{jlgt[1]}")
elif 3 >= pnts <= 4:
  print(f"{txt}{jlgt[2]}")
elif pnts == 5:
  print(f"{txt}{jlgt[3]}")

# 26
import math
abst = int(input('''Qual combustivel deseja abastecer?

0 - Alcool
1 - Gasolina
2 - Alcool e Gasolina

Digite a opção numérica: '''))
prc = [1.9, 2.5]
des = [0.03, 0.04, 0.05, 0.06]
if abst == 0 or abst == 1:
    lts = float(input('''
Quantos litros? '''))
    tot = prc[abst] * lts
    if 1 <= lts < 21:
        tcd = tot - (math.floor(lts) * prc[abst] * des[abst])
        print(f'''
Valor a pagar: R$ {round(tcd, 2)}''')
    elif lts >= 21:
        tcd = tot - (math.floor(lts) * prc[abst] * des[abst + 2])
        print(f'''
Valor a pagar: R$ {round(tcd, 2)}''')
elif abst == 2:
    lt_a = float(input('''
Quantos litros de Alcool? '''))
    lt_g = float(input("E quantos litros de Gasolina? "))
    tot = [prc[0] * lt_a, prc[1] * lt_g]
    if 1 <= lt_a < 21 and 1 <= lt_g <= 21:
        tcd_a = tot[0] - (math.floor(lt_a) * prc[0] * des[0])
        tcd_g = tot[1] - (math.floor(lt_g) * prc[1] * des[1])
        print(f'''
Valor a pagar: 

Alcool   R$ {round(tcd_a, 2)}
Gasolina R$ {round(tcd_g, 2)}
Total    R$ {round(tcd_a + tcd_g, 2)}''')
    elif 1 <= lt_a < 21 <= lt_g:
        tcd_a = tot[0] - (math.floor(lt_a) * prc[0] * des[0])
        tcd_g = tot[1] - (math.floor(lt_g) * prc[1] * des[3])
        print(f'''
Valor a pagar: 

Alcool   R$ {round(tcd_a, 2)}
Gasolina R$ {round(tcd_g, 2)}
Total    R$ {round(tcd_a + tcd_g, 2)}''')
    elif 1 <= lt_g < 21 <= lt_a:
        tcd_a = tot[0] - (math.floor(lt_a) * prc[0] * des[2])
        tcd_g = tot[1] - (math.floor(lt_g) * prc[1] * des[1])
        print(f'''
Valor a pagar: 

Alcool   R$ {round(tcd_a, 2)}
Gasolina R$ {round(tcd_g, 2)}
Total    R$ {round(tcd_a + tcd_g, 2)}''')
    elif lt_g >= 21 <= lt_g:
        tcd_a = tot[0] - (math.floor(lt_a) * prc[0] * des[2])
        tcd_g = tot[1] - (math.floor(lt_g) * prc[1] * des[3])
        print(f'''
Valor a pagar: 

Alcool   R$ {round(tcd_a, 2)}
Gasolina R$ {round(tcd_g, 2)}
Total    R$ {round(tcd_a + tcd_g, 2)}''')
