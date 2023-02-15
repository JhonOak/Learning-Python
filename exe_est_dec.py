# Exercícios de Estrutura de Decisão
# https://wiki.python.org.br/EstruturaDeDecisao

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
  print(num_1,"foi o maior número dos três.")
elif num_2 >= num_1 and num_2 >= num_3:
  print(num_2,"foi o maior número dos três.")
elif num_3 >= num_1 and num_3 >= num_2:
  print(num_3,"foi o maior número dos três.")
  
# 7 - Exiba o produto com menor preço
pro_1 = float(input("Qual o preço do 1º produto? )
pro_2 = float(input("Qual o preço do 2º produto? )
pro_3 = float(input("Qual o preço do 3º produto? )
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
                    
# 8 - 
