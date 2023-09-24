# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

variavel = input('Digite algo: ')

print(f'O tipo primitivo desse valor é: {type(variavel)}')
print(f'Só tem espaços? {variavel.isspace()}')
print(f'É um número?  {variavel.isnumeric()}')
print(f'É alfabético?  {variavel.isalpha()}')
print(f'É alfanumérico? {variavel.isalnum()}')
print(f'Está em maiúsculas? {variavel.isupper()}')
print(f'Está em minúsculas? {variavel.islower()}')
print(f'Está em capitalizada? {variavel.istitle()}')
