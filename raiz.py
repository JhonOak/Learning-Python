# Raiz Quadrada
i_raiz = int(input("Digite uma Raiz: "))
for raiz in range(1,10**10):
  x_raiz = raiz ** 2 # Para Raiz Cubica ** 3, Quarta ** 4...
  y_raiz = x_raiz * 1 / raiz # Raiz Cubica ** 2, Quarta ** 3...
  if i_raiz == x_raiz:
    print(int(y_raiz))