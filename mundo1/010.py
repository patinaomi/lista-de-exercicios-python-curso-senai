# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar, considere u$1,00 = r$3,27

import sys

def dolar_para_real():
    real = float(input('Quanto dinheiro você tem? R$'))
    dolar = 3.27
    conversao = real / dolar
    print(f'Com R${real:.2f}, você pode comprar US${conversao:.2f}.')
 
def real_para_dolar():
    dolar = float(input('Quanto dinheiro você tem? US$'))
    real = 3.27
    conversao = dolar * real
    print(f'Com US${dolar:.2f}, você pode comprar R${conversao:.2f}.')
       

def exibir_menu():
    print('==== CONVERSOR DE DINHEIRO ====')
    print('[1] - Dólar para Real')
    print('[2] Real para Dólar')
    print('[0] Sair do programa')
    
while True:
    exibir_menu()
    
    op = int(input('Digite uma opção: '))
    
    if op == 1:
        dolar_para_real()
    elif op == 2:
        real_para_dolar()
    elif op == 0:
        print('SAINDO DO PROGRAMA....')
        sys.exit()
    else:
        print('Opção inválida, tente novamente')    
    