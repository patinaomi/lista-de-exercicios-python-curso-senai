# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada

numero = int(input('Digite um número: '))

print(f'Tabuada do {numero}:')
for i in range(1, 11):
    tabuada = numero * i
    print(f'{numero} X {i} = {tabuada}')