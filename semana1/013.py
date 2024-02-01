# Faça um algoritmo que leia o salário de uma funcionário e mostre seu novo salário, com 15% de aumento 

salario = float(input('Digite o salário do funcionário: R$'))

novo_salario =  salario + (salario * 15/100)

print(f'Salário antigo {salario:.2f}, com reajuste de 15%')
print(f'Salário atualizado: R${novo_salario:.2f}')