lista = []
cont = 0
soma = 0

for i in range(10):
    lista.append(int(input(f'Digite o {i+1}° número: ')))
    cont +=1 
    soma += lista[i]

maior = lista[0]
menor = lista[0]

for item in lista:
  if item > maior:
    maior = item
    else:
    if item < menor:
      menor = item

res = soma / cont

print('\n--- RESULTADO ---')
print('Maior Valor: ', maior)
print('Menor Valor: ', menor)
print(f'Média dos Números: {res:.2f}')
