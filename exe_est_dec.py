# Exercícios de Estrutura de Decisão
# https://wiki.python.org.br/EstruturaDeDecisa

# 1 - Exiba o maior de dois números
num_1 = float(input("Digite um número: "))
num_2 = float(input("Agora o segundo número: "))
if num_1 > num_2:
  print("O maior número é:",num_1)
elif num_1 < num_2:
  print("O maior número é:",num_2)
else:
  print("Os números são iguais")

# 2 - Exiba se o número é positivo ou negativo
num = float(input("Digite um número positivo ou negativo: "))
if num > 0:
  print("Este número é positivo")
elif num < 0:
  print("Este número é negativo")
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
vog = ['a','e','i','o','u',"A","E","I","O","U"]
con = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
letra = input("Digite uma letra: ")
if letra in vog:
 print("A letra",letra,"é uma vogal")
elif letra in con:
 print("A letra",letra,"é uma consoante")
else:
 print("Caractere inválido")

# 5 - 
  
