lista = []
soma = 0
cont = 0
cont2 = 0

qtd = int(input('Informe a quantidade de clientes: '))

for i in range(qtd):
    lista.append(float(input(f'Informe a temperatura do {i+1}° cliente: ')))
    soma += lista[i]
    cont += 1

print('\n--- RESULTADO ---') 
for item in lista:
    cont2 += 1
    if item <= 37.2:
        print(f'Paciente {cont2} : {item}°C - Temperatura Normal')
    elif item <= 38:
        print(f'Paciente {cont2} : {item}°C - Estado Febril')
    elif item <= 39:
        print(f'Paciente {cont2} : {item}°C - Febre')
    else:
        print(f'Paciente {cont2} : {item}°C - Febre Alta')


print('\n---- RELATÓRIO ----')
print(f'Quantidade de pessoas analisadas: {cont}')
print(f'Média da temperatura: {soma/cont:.2f}°C')


