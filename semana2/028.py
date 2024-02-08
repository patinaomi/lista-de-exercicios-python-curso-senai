numero = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1

print(f'Fatorial de {numero}! - ', end='')
for i in range(numero, 0, -1):

    # aqui foi utilizado um if ternário ou seja, um if que é feito em uma só linha de código
    print(i, end=' = ') if i == 1 else print(i, end=' X ')

    # mesma coisa que fatorial = fatorial * i
    fatorial *= i
    
print(fatorial)
