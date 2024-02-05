timeA = int(input('Digite a quantidade de gols do primeiro time: '))
timeB = int(input('Digite a quantidade de gols do segundo time: '))

print(f'PLACAR: {timeA} X {timeB}')

if timeA > timeB:
    print('Vitória do primeiro time.')
elif timeA == timeB:
    print('Empate')
else: 
    print('Vitória do segundo time.')


# Exemplo mais dinâmico

timeA = input('Digite o nome do time A: ')
qtd_golA = int(input('Digite a quantidade de gols: '))
timeB = input('Digite o nome do time B: ')
qtd_golB = int(input('Digite a quantidade de gols: '))

print(f'PLACAR: {timeA} {qtd_golA} X {qtd_golB} {timeB}')

if qtd_golA > qtd_golB:
  print(f'O {timeA} venceu o jogo.')
elif qtd_golA == qtd_golB:
  print('Jogo empatado')
else:
  print(f'O {timeB} venceu o jogo.')


# Exemplo com Listas

timeA = []
timeB = []


timeA.append(input('Digite o nome do time A: '))
timeA.append(int(input('Digite a quantidade de gols: ')))

timeB.append(input('Digite o nome do time B: '))
timeB.append(int(input('Digite a quantidade de gols: ')))


print(f'PLACAR: {timeA[0]} {timeA[1]} X {timeB[1]} {timeB[0]}')

if timeA[1] > timeB[1]:
  print(f'O {timeA[0]} venceu o jogo.')

elif timeA[1] == timeB[1]:
  print('Jogo empatado')
else:
  print(f'O {timeB[0]} venceu o jogo.')
