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
  print(num,"é positivo")
elif num < 0:
  print(num," é negativo")
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
vog = ["a","e","i","o","u","A","E","I","O","U"]
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

# 7 - Exiba o maior e o menor entre três numeros
num_1 = float(input("Digite o 1º número a ser comparado: "))
num_2 = float(input("Digite o 2º número a ser comparado: "))
num_3 = float(input("Digite o 3º número a ser comparado: "))
if num_1 >= num_2 and num_1 >= num_3 and num_2 <= num_1 and num_2 <= num_3:
  print(num_1,"foi o maior e",num_2,"foi o menor.")
elif num_1 >= num_2 and num_1 >= num_3 and num_3 <= num_1 and num_3 <= num_2:
  print(num_1,"foi o maior e",num_3,"foi o menor.")
elif num_2 >= num_1 and num_2 >= num_3 and num_1 <= num_2 and num_1 <= num_3:
  print(num_2,"foi o maior e",num_1,"foi o menor.")
elif num_2 >= num_1 and num_2 >= num_3 and num_3 <= num_1 and num_3 <= num_2:
  print(num_2,"foi o maior e",num_3,"foi o menor.")
elif num_3 >= num_1 and num_3 >= num_2 and num_1 <= num_2 and num_1 <= num_3:
  print(num_3,"foi o maior e",num_1,"foi o menor.")
elif num_3 >= num_1 and num_3 >= num_2 and num_2 <= num_1 and num_2 <= num_3:
  print(num_3,"foi o maior e",num_2,"foi o menor.")
elif num_1 == num_2 and num_2 == num_3:
  print(num_1,"foi o maior e o menor número, pois os três são iguais.")

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
  print("Em ordem decrecente:",num_1,",",num_2,"e",num_3)
elif num_1 >= num_2 and num_1 >= num_3 and num_3 >= num_2:
  print("Em ordem decrecente:",num_1,",",num_3,"e",num_2)
elif num_2 >= num_1 and num_2 >= num_3 and num_1 >= num_3:
  print("Em ordem decrecente:",num_2,",",num_1,"e",num_3)
elif num_2 >= num_1 and num_2 >= num_3 and num_3 >= num_1:
  print("Em ordem decrecente:",num_2,",",num_3,"e",num_1)
elif num_3 >= num_1 and num_3 >= num_2 and num_1 >= num_2:
  print("Em ordem decrecente:",num_3,",",num_1,"e",num_2)
elif num_3 >= num_1 and num_3 >= num_2 and num_2 >= num_1:
  print("Em ordem decrecente:",num_3,",",num_2,"e",num_1)

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
sal = float(input("Quanto é o seu salário?"))
aum_1 = 0.2
aum_2 = 0.15
aum_3 = 0.1
aum_4 = 0.05
if sal > 0 and sal <= 280:
  sal_a = sal + (sal * aum_1)
  print("Seu salário era de R$",sal)
  print("Você recebeu um aumento de",aum_1*100,"%")
  print("O valor do seu aumento foi de R$",sal*aum_1)
  print("Seu salário agora é de R$",sal_a)
elif sal > 280 and sal <= 700:
  sal_a = sal + (sal * aum_2)
  print("Seu salário era de R$",sal)
  print("Você recebeu um aumento de",aum_2*100,"%")
  print("O valor do seu aumento foi de R$",sal*aum_2)
  print("Seu salário agora é de R$",sal_a)
elif sal > 700 and sal <= 1500:
  sal_a = sal + (sal * aum_3)
  print("Seu salário era de R$",sal)
  print("Você recebeu um aumento de",aum_3*100,"%")
  print("O valor do seu aumento foi de R$",sal*aum_3)
  print("Seu salário agora é de R$",sal_a)
elif sal > 1500:
  sal_a = sal + (sal * aum_4)
  print("Seu salário era de R$",sal)
  print("Você recebeu um aumento de",aum_4*100,"%")
  print("O valor do seu aumento foi de R$",sal*aum_4)
  print("Seu salário agora é de R$",sal_a)
