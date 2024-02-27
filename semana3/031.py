# Sistema para buscar determinado paciente da lista

lista_pacientes = []
id = 0

while True:
    print('--- MENU ---')
    print('[1] Cadastrar Paciente')
    print('[2] Buscar Paciente')
    print('[0] Sair do Programa')
    opcao = input('Digite uma opção: ')

    if opcao == '1':
        while True:
            print('----- CADASTRAR NOVO PACIENTE -----')
            nome = input('Digite o nome: ')
            sobrenome = input('Digite o sobrenome: ')
            idade = int(input('Digite a idade: '))
            id += 1
            paciente = {'Id': id, 'Nome': nome, 'Sobrenome': sobrenome, 'Idade': idade}

            print('Paciente cadastrado com sucesso')
            lista_pacientes.append(paciente)

            break

    elif opcao == '2':
            print('----- BUSCAR PACIENTE -----')
            id_busca = int(input('Digite o Id do paciente: '))
            for k in paciente:
                if paciente[k] == id_busca:
                    print('Usuário encontrado: ')
                    print(paciente)
                    break
            else:
                print('Paciente não encontrado na lista')

    elif opcao == '0':
        print('Saindo do Programa...')
        break

    else:
        print('Opção Inválida')
