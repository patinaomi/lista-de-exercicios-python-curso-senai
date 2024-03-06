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
                print('del prod')
            elif op == 0:
                print('Encerrando o programa...')
                break
        else:
            print('Opção inválida, digite novamente.')


def adicionar_prod():
    lista_tam = {}
    while True:
        print('------ Adicionar Produto ------')
        produto = input('Digite o nome do Produto: ')
        cor = input('Digite a cor do Produto: ')
        preco = float(input('Digite o preço unitário: '))
        qtd_var = int(input('Digite a quantidade de variações: '))

        for i in range(qtd_var):
            variacao = input(f'Variação {i+1}: ')
            qtd = input('Digite a quantidade: ')
            lista_tam.update({variacao.upper(): qtd})

        with open('estoque.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            id = len(dados) + 1
            novo_prod = {'Id': id, 'Produto': produto.capitalize(), 'Cor': cor.capitalize(), 'Preço': preco,
                         'Variações': lista_tam}

            dados.append(novo_prod)

            with open('estoque.json', 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        print(f'Produto {produto} cadastrado com sucesso!')
        break

def editar_prod():
    print('------ Alterar Produto ------')
    with open('estoque.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)



def listar_prod():
    print('------ Listar Produtos ------')
    with open('estoque.json', 'r', encoding='utf-8') as arquivo:
        produtos = json.load(arquivo)

    #Caso não tenha produto em estoque
    if not produtos:
        print('Não há produtos no estoque')
        return

    for i, produto in enumerate(produtos):
        print(f"Id #{produto['Id']}  -  {produto['Produto']}")
        print(f"Cor: {produto['Cor']}")
        print(f"Preço: R${produto['Preço']} un.")
        print(f"Variações: {produto['Variações']}")

        for k, v in enumerate(produtos[3]):
            print(k, v)


def buscar_prod():
    print('------ Buscar Produto ------')
    with open('estoque.json', 'r', encoding='utf-8') as arquivo:
        produtos = json.load(arquivo)

        if not produtos:
            print('Não há produtos no estoque')
            return

        busca = input('Digite o ID do produto: ')

        try:
            busca = int(busca) - 1
            if 0 <= busca < len(produtos):
                produto_encontrado = produtos[busca]
                print(f"\n----- ID #{produto_encontrado['Id']} -----")
                print(f"Produto: {produto_encontrado['Produto']}")
                print(f"Cor: {produto_encontrado['Cor']}")
                print(f"Preço: R${produto_encontrado['Preço']}un")
                variacoes = produto_encontrado["Variações"]
                for tamanho, quantidade in variacoes.items():
                    print(f"Tam: {tamanho} - {quantidade} pçs")
            else:
                print("Produto não foi encontrado")

        except ValueError:
            print('Digite somente números')


menu_principal()
