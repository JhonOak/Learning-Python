# Exercícios de Estrutura Sequencial
# https://wiki.python.org.br/EstruturaSequencial

# 1 - Imprima Alo Mundo
print("Alo Mundo")

# 2 - Exiba um número
numero = float(input("Insira um número: "))
print("O número inserido foi: ", numero)

# 3 - Exiba a soma de dois números
numero1 = float(input("Insira o primeiro número da soma: "))
numero2 = float(input("Insira o segundo número: "))
numero = numero1 + numero2
print("A soma é: ", numero)

# 4 - Exiba a média escolar dos 4 bimestres
bimestre1 = float(input("Insira a nota do 1º Bimestre: "))
bimestre2 = float(input("Insira a nota do 2º Bimestre: "))
bimestre3 = float(input("Insira a nota do 3º Bimestre: "))
bimestre4 = float(input("Insira a nota do 4º Bimestre: "))
media = (bimestre1 + bimestre2 + bimestre3 + bimestre4) / 4
print("Média Escolar: ", media)

# 5 - Conversor de m para cm
metro = int(input("Quantos metros deseja converter? "))
centimetro = metro * 100
print(centimetro, "cm")

# 6 - Calculador de área de circulo  (A=pi*r²)
raio = int(input("Qual o raio do circulo que deseja saber a aŕea? "))
pi = 3.14
area = pi * raio ** 2
print("A área é: ", area)

# 7 - Calculador de dobro da área do quadrado
lado = int(input("Qual o valor do ladro do quadrado que deseja saber o dobro da área? "))
area = 2 * lado ** 2
print("O dobro da área é: ", area)

# 8 - Calculador de salário mensal
valor_hora = float(input("Quanto você ganha por hora?"))
horas = float(input("Quantas horas trabalha no mês? "))
salario = valor_hora * horas
print("Seu salário é: R$", salario)

# 9 - Conversor de Fahrenheit para Celsius (C=5*((F-32)/9))
fahrenheit = float(input("Qual a temperatura em Fahrenheit deseja converter para Celcius? "))
celcius = 5 * ((fahrenheit - 32) / 9)
print(celcius, "°C")

# 10 - Conversor de Celcius para Fahrenheit
celcius = float(input("Qual a temperatura em Celcius deseja converter para Fahrenheit? "))
fahrenheit = 32 + (celcius / 5 * 9)
print(fahrenheit, "°F")

# 11 - Peça dois números intieros e um número real e calcule:
numero_1 = int(input("Insira o primeiro número: "))
numero_2 = int(input("Insira o segundo número: "))
numero_r = float(input("Insira um número real: "))

# a) o produto do dobro do primeiro com metade do segundo
calculo_a = numero_1 * 2 * numero_2 / 2
print("O produto do dobro do primeiro com metade do segundo número é: ", calculo_a)

# b) a soma do triplo do primeiro com o terceiro
calculo_b = (numero_1 * 3) + numero_r
print("A soma do triplo do primeiro com o terceiro número é: ", calculo_b)

# c) o terceiro elevado ao cubo
calculo_c = numero_r ** 3
print("O terceiro número elevado ao cubo é: ", calculo_c)

# 12 - Calculadora de peso ideal ((72.7*altura)-58)
altura = float(input("Qual a altura da pessoa que deseja calcular o peso ideal? "))
peso_ideal = (72.7 * altura) - 58
print("O peso ideal desta pessoa é: ", peso_ideal)

# 13 - Calculadora de peso ideal com as seguintes formulas:
altura = float(input("Qual a altura da pessoa? "))
sexo = input("Esta pessoa é homem ou mulher?: ")

# a) para homens: (72.7*altura)-58
if sexo == "homem":
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para este Homem é:", peso_ideal)

# b) para mulheres: (62.1*altura)-44.7
elif sexo == "mulher":
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para esta Mulher é:", peso_ideal)

# 14 - Calculadora de peso e multa da pesca do João
peso = float(input("Quantos Kg de Peixe João pescou? "))
peso_max = 50
valor_multa = 4.00
excesso = peso - peso_max # quantidade de kg além do limite
multa = excesso * valor_multa # valor da multa que joao deverá pagar
if excesso >= 1:
    print("João excedeu o limite de pesca em:",excesso,"Kg")
    print("Deverá pagar uma multa de R$",multa)
elif excesso < 1:
    print("Não houve multa para João")

# 15 - Calculadora de Salário e descontos
valor_hora = float(input("Quanto você ganha por hora trabalhada? "))
horas_trabalhadas = float(input("Quantas horas você trabalha por mês?"))
imposto_renda = 0.11
inss = 0.08
sindicato = 0.05

# a) salário bruto
bruto = valor_hora * horas_trabalhadas
print("Seu salário bruto é R$",bruto)

# b) quanto pagou ao INSS
pago_inss = bruto * inss
print("Você pagou R$",pago_inss,"ao INSS")

# c) quanto pagou ao sindicato
pago_sindicato = bruto * sindicato
print("Você pagou R$",pago_sindicato,"ao Sindicato")

# d) salário líquido
pago_ir = bruto * imposto_renda
liquido = bruto - pago_sindicato - pago_inss - pago_ir
print("Seu salário líquido é R$",liquido)

# e) calcule os descontos e o salário líquido, conforme tabela exibida
print("+ Salário Bruto  : R$",bruto)
print("- IR       (11%) : R$",pago_ir)
print("- INSS      (8%) : R$",pago_inss)
print("- Sindicato (5%) : R$",pago_sindicato)
print("= Salário Líquido: R$",liquido)

# 16 - Calculador de quantidade de latas de tinta
area = float(input("Quantos metros quadrados deseja pintar? "))
litro_cobre = 3
litros_lata = 18
lata_cobre = litro_cobre * litros_lata
if area <= lata_cobre:
    print("Você precisará de uma lata de tinta.")
elif area > lata_cobre and area <= lata_cobre * 2:
    print("Você precisará de duas latas de tinta.")
elif area > lata_cobre * 2 and area <= lata_cobre * 3:
    print("Você precisará de três latas de tinta.")
elif area > lata_cobre * 3 and area <= lata_cobre * 4:
    print("Você precisará de quatro latas de tinta.")
elif area > lata_cobre * 4 and area <= lata_cobre ** 10:
    print("Você precisará de MUITAS latas de tinta.")

# 17 - Calculador de quantidade de latas de tinta em três situações
import math
area = float(input("Quantos metros quadrados deseja pintar? "))
litro_cobre = 6
lata = 18
galao = 3.6
lata_cobre = litro_cobre * lata
galao_cobre = litro_cobre * galao

# a) comprando apenas latas de 18 litros
latas = area / lata_cobre
print("Você precisará da seguinte quantidade de latas:",math.ceil(latas))
# b) comprando apenas galõesde 3,6 litros
galoes = area / galao_cobre
print("Você precisará da seguinte quantidade de galões:",math.ceil(galoes))
# c) misturar latas e galões. Acrescente 10% de folga e arredonde valores para cima.
# Pulei, preciso aprender um pouco mais kkkk

# 18 - Calculadore de tempo de Download
arquivo = float(input("Qual o tamanho do arquivo em MB? "))
velocidade = float(input("Qual a velocidade da internet em Mbps? "))
tempo = arquivo / velocidade / 60
print("O tempo aproximado do download será de",tempo,"minutos.")
