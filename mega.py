import random


from math import factorial

def combinacao(n, k):
  return factorial(n) // (factorial(k) * factorial(n - k))

# Calcula C(48, 6)// #C(48, 6) = 48! / (6! * 42!)

resultado = combinacao(60, 6) # 12 eh o numero total conta o 6 que eh o numero jogado.

# Imprime o resultado
print(f"A chance de acertar eh de 1 a = {resultado}")


def gerar_numeros(excluir):
  numeros = []
  for _ in range(6):
      num = random.randint(1, 60)
      while num in excluir or num in numeros:
          num = random.randint(1, 60)
      numeros.append(num)
  return numeros

print(sorted (gerar_numeros([1,2, 4, 5, 6, 7, 13, 14,23, 39, 55, 59, 60]))) #numeros dentro do parentese sao os que quero que nao rode 

