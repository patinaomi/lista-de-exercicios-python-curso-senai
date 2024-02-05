valor = float(input('Digite o valor da compra: '))
qtd_prestacao = int(input('Digite o número de prestações: '))

resultado = valor / qtd_prestacao

print(f'Valor do Produto: R${valor} em {qtd_prestacao}X sem juros')
print(f'Valor da Prestação: R${resultado:.2f}')
