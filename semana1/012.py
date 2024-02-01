# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto 

preco_produto = float(input('Digite o preço do produto: R$'))
desconto = int(input('Digite o valor do desconto: '))

preco_final = preco_produto - (preco_produto * desconto / 100)

print(f'Preço do produto R${preco_produto} com desconto de {desconto}%')
print(f'Valor atualizado: R${preco_final}')