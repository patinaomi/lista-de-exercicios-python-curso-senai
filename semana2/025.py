lista = []
lista_mulheres = []
lista_homens = []


for i in range(11):
    genero = ''

    while True:
        idade = int(input(f'Digite a {i+1}ª idade: '))
        if idade >= 18 and idade <=70:
            lista.append(idade)
            break
        else:
            print('Idade inválida, deve ser maior que 18 e menor que 70!')
        

    while True:
        genero = input('\t[F] - Feminino\n\t[M]- Masculino\n\tDigite: ')

        if genero.upper() == 'F':
            lista_mulheres.append(idade)
            break
        elif genero.upper() == 'M':
            lista_homens.append(idade)
            break
        else:
          print('Opção Inválida')

print('----- RESULTADO -----')
if len(lista_mulheres) != 0:
    media_m = sum(lista_mulheres) / len(lista_mulheres)
    print(f'Idade média das mulheres: {media_m:.2f}')
else:
    print('Não há mulheres na lista!')

if len(lista_homens) != 0:
    media_h = sum(lista_homens) / len(lista_homens)
    print(f'Idade médias dos homens: {media_h:.2f}')
else:
    print('Não há homens na lista!')

media_grupo = sum(lista) / len(lista)
print(f'Idade média do grupo: {media_grupo:.2f}')
