# Escreva um programa que converta um a temperatura digitada em ºC e converta para ºF 

while True:
    print('==== CONVERSOR DE TEMPERATURA ====')
    print('[1] Celsius para Fahrenheit')
    print('[2] Fahrenheit para Celsius')
    print('[0] Sair do programa')
    
    op = int(input('Digite uma opção: '))
    
    if op == 1:
        c = float(input('Digite a temperatura em graus Celsius: '))
        f = c * 1.8 + 32
        print(f'A temperatura de {c}ºC corresponde a {f:.2f}F')

    elif op == 2:
        f = float(input('Digite a temperatura em Fahrenheit: '))
        c = (f - 32) / 1.8
        print(f'A temperatura de {f}F corresponde a {c:.2f}ºC')
        
    elif op == 0:
        print('SAINDO DO PROGRAMA')
        break
    else:
        print('Opção inválida')
        
    
    
    

