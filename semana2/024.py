lista = []
soma = 0
cont = 0

qtd = int(input('Informe a quantidade de clientes: '))

for i in range(qtd):
    lista.append(float(input(f'Informe a temperatura do {i+1}° cliente: ')))
    soma += lista[i]

print('\n--- RESULTADO ---') 
for item in lista:
    cont += 1
    if item <= 37.2:
        print(f'Paciente {cont} : {item}°C - Temperatura Normal')
    elif item <= 38:
        print(f'Paciente {cont} : {item}°C - Estado Febril')
    elif item <= 39:
        print(f'Paciente {cont} : {item}°C - Febre')
    else:
        print(f'Paciente {cont} : {item}°C - Febre Alta')


print('\n---- RELATÓRIO ----')
print(f'Quantidade de pessoas analisadas: {qtd}')
print(f'Média da temperatura: {soma/cont:.2f}°C')
