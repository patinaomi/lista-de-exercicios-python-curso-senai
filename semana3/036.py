def input_num():
    try:
        x = int(input('Digite o primeiro número: '))
        y = int(input('Digite o segundo número: '))
    except ValueError:
        print('Digite somente números')

    lista = [x, y]
    return lista

def somar(x, y):
    print(f'\nResultado: {x} + {y} = {x+y}')


def subtrair(x, y):
    print(f'\nResultado: {x} - {y} = {x-y}')

def multiplicar(x, y):
    print(f'\nResultado: {x} X {y} = {x*y}')

def dividir(x, y):
    try:
        print(f'\nResultado: {x} / {y} = {x/y}')
    except ZeroDivisionError:
        print('Não é possível dividir por 0')


def menu():
    while True:
        print(
"""----- CALCULADORA ----
[1] SOMAR
[2] SUBTRAIR
[3] MULTIPLICAR
[4] DIVIDIR
[0] Sair do programa
--------------------""")

        try:
            op = int(input('Digite uma opção: '))
            if(op in range(0, 6)):
                if op == 1:
                    lista = num()
                    x = lista[0]
                    y = lista[1]
                    somar(x, y)

                elif op == 2:
                    lista = num()
                    x = lista[0]
                    y = lista[1]
                    subtrair(x, y)

                elif op == 3:
                    lista = num()
                    x = lista[0]
                    y = lista[1]
                    multiplicar(x, y)
                elif op == 4:
                    lista = num()
                    x = lista[0]
                    y = lista[1]
                    dividir(x, y)

                elif op == 0:
                    print('Saindo do programa....')
                    break

            else:
                print('Opção Inválida')
        except ValueError:
            print('Digite somente números')


menu()
