num = int(input('Digite um número: '))

if num == 0:
  print(f'{num} é NULO')
elif num % 2 == 0:
  print(f'O número {num} é PAR')
else:
  print(f'O número {num} é ÍMPAR')
