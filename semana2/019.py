idade = int(input('Digite a idade do nadador: '))

if idade < 5:
    print(f'Idade {idade} - Não se enquadra')
elif idade <= 7:
    print(f'Idade {idade} - Categoria Infantil A')
elif idade <= 11:
    print(f'Idade {idade} - Categoria Infantil B')
elif idade <= 13:
    print(f'Idade {idade} - Categoria Juvenil A')
elif idade <= 17:
    print(f'Idade {idade} - Categoria Juvenil B')
else:
    print(f'Idade {idade} - Categoria Adulto')
