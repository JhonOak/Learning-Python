# Coleções(Listas)
price_1 = 20
price_2 = 50
price_3 = 200
# Lista
prices = [20,50,200]
#         0,  1, 2
print(prices[1])
print(prices.index(200))
# Lista
diversities = [15,"Jhon",True]
print(diversities[0])
print(diversities[1])
print(diversities[2])
# Laços em interaveis
for price in prices:
  print(price)

# Exemplo 5 - Some os valores
# Dados uma coleção de idades [15,46,75,34,23], imprima na tela a soma desses valores.

ages = [15,46,75,34,23]
total = 0
for age in ages:
  total = total + age
  print(total)

test = diversities[2]
if test == True:
  print("It Works!")
else:
  print("Error")