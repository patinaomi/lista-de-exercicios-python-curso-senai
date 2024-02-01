valor = float(input('Digite o valor: '))
taxa = float(input('Digite a taxa de juros: '))
tempo = int(input('Digite a quantidade de meses: '))

prestacao = valor + (valor * (taxa/100) * tempo)

print('\n--- PRESTAÇÃO CONTAS ---')
print(f'Valor em atraso R${valor:.2f}')
print(f'Taxa de juros: {taxa:.1f}%')
print(f'Quantidade de meses em atraso: {tempo}')
print(f'Valor atualizado: R${prestacao:.2f}')
