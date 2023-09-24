# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

import math

numero = int(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz_quadrada =  math.sqrt(numero)

print(f'O dobro de {numero} vale {dobro}.')
print(f'O triplo de {numero} vale {triplo}.')
print(f'A raíz quadrada de {numero} é igual a {raiz_quadrada:.2f}.')
