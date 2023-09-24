# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado. 

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

preco_total = (60 * dias) + (0.15 * km)

print(f'O total a pagar é de R${preco_total:.2f}')