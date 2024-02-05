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
    vencedor = timeA
elif qtd_golA == qtd_golB:
    vencedor = ''
else:
    vencedor = timeB
  
if vencedor == '':
    print('Jogo empatado')
else:  
    print(f'O {vencedor} venceu o jogo.')

# Exemplo com Listas

timeA = []
timeB = []

timeA.append(input('Digite o nome do time A: '))
timeA.append(int(input('Digite a quantidade de gols: ')))

timeB.append(input('Digite o nome do time B: '))
timeB.append(int(input('Digite a quantidade de gols: ')))


print(f'PLACAR: {timeA[0]} {timeA[1]} X {timeB[1]} {timeB[0]}')

if timeA[1] > timeB[1]:
    vencedor = timeA[0]

elif timeA[1] == timeB[1]:
    vencedor = ''
else:
    vencedor = timeB[0]

if vencedor == '':
    print('Jogo empatado')
else:  
    print(f'O {vencedor} venceu o jogo.')
