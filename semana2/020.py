n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

print('--- Calculadora ---')
print('[1] SOMA')
print('[2] SUBTRAÇÃO')
print('[3] MULTIPLICAR')
print('[4] DIVIDIR')
print('------------------')
op = int(input('Qual operação gostaria de realizar? '))


if op == 1:
    print(f'{n1} + {n2} = {n1+n2}')
elif op == 2:
    print(f'{n1} - {n2} = {n1-n2}')
elif op == 3:
    print(f'{n1} X {n2} = {n1*n2}')
elif op == 4:
    print(f'{n1} / {n2} = {n1/n2}')
else:
    print('Opção inválida')
