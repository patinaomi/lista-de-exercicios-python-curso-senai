lista = []
lista_mulheres = []
lista_homens = []


for i in range(10):
    genero = ''
    idade = int(input(f'Digite a {i+1}ª idade: '))
    lista.append(idade)

    while True:
        genero = input('Feminino ou Masculino (F/M): ')

        if genero.upper() == 'F':
            lista_mulheres.append(idade)
            break
        elif genero.upper() == 'M':
            lista_homens.append(idade)
            break
        else:
          print('Opção Inválida')


media_m = sum(lista_mulheres) / len(lista_mulheres)
media_h = sum(lista_homens) / len(lista_homens)
media_grupo = sum(lista) / len(lista)

print(f'Idade média das mulheres: {media_m:.2f}')
print(f'Idade médias dos homens: {media_h:.2f}')
print(f'Idade média do grupo: {media_grupo:.2f}')
