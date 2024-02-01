salario = float(input('Digite o valor do salário atual: '))
percentual = float(input('Digite o percentual de aumento: '))

salario_atualizado = salario + (salario * (percentual/100))

print(f'Saldo atualizado: R${salario_atualizado:.2f}')  
