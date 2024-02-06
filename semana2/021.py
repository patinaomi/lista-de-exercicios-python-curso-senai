lista = ['João', 'Maria', 'Pedro', 'José', 'Lulu', 'Jajá', 'Tati', 'Mario', 'Selma']

nome = input('Digite o nome para pesquisa: ')

for i in lista: 
    if i == nome.capitalize():
      print(f'{i} - encontrado')
      break
else:
    print(f'{nome} - não foi encontrado')
