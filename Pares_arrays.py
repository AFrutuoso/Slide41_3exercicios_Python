array = [3,8,12,7,20,5,6]
contador = 0
for n in array:
  if n%2 == 0: # compara o resto da divisão por 2 se zero
      contador += 1 # equivalente contador = contador  + 1

print("Quantidade de números pares:", contador)
