import datetime as dt

ano_atual = dt.datetime.now().year

ano_nascimento = int(input('Digite seu ANO de nascimento: '))

if ano_atual - ano_nascimento >= 18:
    print('Você é MAIOR de idade')
else:
    print('Você é MENOR de idade')
