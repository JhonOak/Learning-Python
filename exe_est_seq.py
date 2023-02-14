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
# 14 -


