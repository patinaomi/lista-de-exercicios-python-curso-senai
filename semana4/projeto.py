import json


def menu_principal():
    while True:
        print("""
------ Loja da Pati ------
| [1] Adicionar Produto |
| [2] Editar Produto    |
| [3] Ver Estoque       |
| [4] Buscar Produto    |
| [5] Deletar Produto   |
| [0] Sair do Programa  |
-------------------------
""")

        op = int(input('Digite uma opção: '))

        if op in range(0, 6):
            if op == 1:
                adicionar_prod()
            elif op == 2:
                editar_prod()
            elif op == 3:
                listar_prod()
            elif op == 4:
                buscar_prod()
            elif op == 5:
                deletar_prod()
            elif op == 0:
                print('Encerrando o programa...')
                break
        else:
            print('Opção inválida, digite novamente')


#
def carregar_dados():
    with open('estoque.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados


#
def escrever_dados(dados):
    with open('estoque.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)


#
def imprimir_dados(dados):
    print(f"\n----- ID #{dados['Id']} -----")
    print(f"Produto: {dados['Produto']}")
    print(f"Cor: {dados['Cor']}")
    print(f"Preço: R${dados['Preço']} un")
    variacoes = dados["Variações"]
    for tamanho, quantidade in variacoes.items():
        print(f"Tam: {tamanho} - {quantidade} pçs")


#
def adicionar_prod():
    lista_tam = {}
    while True:
        print('------ Adicionar Produto ------')
        produto = input('Digite o nome do Produto: ')
        cor = input('Digite a cor do Produto: ')
        preco = float(input('Digite o preço unitário: '))
        qtd_var = int(input('Digite a quantidade de variações: '))

        for i in range(qtd_var):
            variacao = input(f'Variação {i + 1}: ')
            qtd = input('Digite a quantidade: ')
            lista_tam.update({variacao.upper(): qtd})

        dados = carregar_dados()
        id = len(dados) + 1

        novo_prod = {'Id': id, 'Produto': produto.capitalize(), 'Cor': cor.capitalize(), 'Preço': preco,
                     'Variações': lista_tam}

        dados.append(novo_prod)
        escrever_dados(dados)

        print(f'Produto {produto} cadastrado com sucesso!')
        break


def editar_prod():
    print('------ Editar Produto ------')
    produtos = carregar_dados()

    if not produtos:
        print('Não há produtos no estoque')
        return

    try:
        index = None
        num_prod = int(input("Digite o número do produto que deseja alterar (ou '0' para cancelar): "))
        if num_prod == 0:
            return

        for i, produto in enumerate(produtos):
            if produto['Id'] == num_prod:
                index = i

                prod_selecionado = produtos[index]
                print('Produto para ser alterado:')
                imprimir_dados(prod_selecionado)

                op = input('\nDigite o número correspondente ao dado que deseja alterar:'
                           '\n [1] Nome do Produto'
                           '\n [2] Cor'
                           '\n [3] Preço'
                           '\n [4] Variações'
                           '\n [0] Cancelar'
                           '\n Opção: ')
                if op == '1':
                    prod_selecionado['Nome'] = input('Digite o novo nome do produto: ')
                elif op == '2':
                    prod_selecionado['Cor'] = input('Digite a nova cor: ')
                elif op == '3':
                    prod_selecionado['Preço'] = float(input('Digite o novo preço: '))
                elif op == '4':
                    lista_tam = {}
                    qtd_var = int(input('Digite a quantidade de variações: '))
                    for i in range(qtd_var):
                        variacao = input(f'Variação {i + 1}: ')
                        qtd = input('Digite a quantidade: ')
                        lista_tam.update({variacao.upper(): qtd})
                        prod_selecionado['Variações'] = lista_tam
                elif op == '0':
                    return
                else:
                    print('Opção inválida')

                escrever_dados(produtos)
                print('Produto alterado com sucesso')
                break

    except ValueError:
        print('Digite somente números')


def listar_prod():
    print('------ Listar Produtos ------')
    produtos = carregar_dados()

    # Caso não tenha produto em estoque
    if not produtos:
        print('Não há produtos no estoque')
        return

    for i, produto in enumerate(produtos):
        imprimir_dados(produto)


def buscar_prod():
    print('------ Buscar Produto ------')
    produtos = carregar_dados()

    if not produtos:
        print('Não há produtos no estoque')
        return

    busca = input('Digite o ID do produto: ')

    try:
        busca = int(busca) - 1
        if busca < len(produtos):
            prod_selecionado = produtos[busca]
            imprimir_dados(prod_selecionado)

        else:
            print("Produto não foi encontrado")

    except ValueError:
        print('Digite somente números')


def deletar_prod():
    print('------ Deletar Produto ------')
    produtos = carregar_dados()

    if not produtos:
        print('Não há produtos no estoque')
        return

    op = input('Digite o ID do produto: ')

    try:
        busca = int(op)
        index = None
        produtos = carregar_dados()
        for i, produto in enumerate(produtos):
            if produto['Id'] == busca:
                index = i
                del produtos[index]

        escrever_dados(produtos)
        print('Produto deletado')

    except ValueError:
        print('Digite somente números')


menu_principal()
