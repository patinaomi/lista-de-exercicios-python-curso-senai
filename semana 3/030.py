# Teste usando UPDATE

pacientes = {}

print('----- CADASTRO -----')
nome = input('Digite o nome: ')
sobrenome = input('Digite o sobrenome: ')
idade = int(input('Digite a idade: '))

pacientes.update({'Nome': nome, 'Sobrenome': sobrenome, 'Idade': idade})

print('\n--- IMPRESSÃO ---')
for k, v  in pacientes.items():
   print(f'{k} - {v}')


# Armazenando direto no dicionário
pacientes = {}

print('----- CADASTRO -----')
pacientes['Nome'] = input('Digite o nome: ')
pacientes['Sobrenome'] = input('Digite o sobrenome: ')
pacientes['Idade'] = int(input('Digite a idade: '))


print('\n --- IMPRESSÃO ---')
for k, v  in pacientes.items():
   print(f'{k} - {v}')


# Aqui posso adicionar uma quantidade indeterminada de pacientes dentro de uma lista
lista_pacientes = []
id = 0

while True:
    print('----- CADASTRAR NOVO PACIENTE -----')
    nome = input('Digite o nome: ')
    sobrenome = input('Digite o sobrenome: ')
    idade = int(input('Digite a idade: '))
    id += 1
    novo_paciente = {'Id': id, 'Nome': nome, 'Sobrenome': sobrenome, 'Idade': idade}
    lista_pacientes.append(novo_paciente)

    opcao = input('Deseja adicionar novo paciente? (S/N): ')
    if opcao.upper() == 'N':
        break

print('--- IMPRESSÃO ---')
print(lista_pacientes)
