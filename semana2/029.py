usuario = 'patinaomi'
senha = 'goiaba'

while True:
    usuario_login = input('Usuário: ')
    senha_login = input('Senha: ')

    if usuario_login.lower() == senha_login:
        print('A senha não pode ser igual ao nome do usuário')
        continue
    if usuario_login.lower() == usuario and senha_login == senha:
        print('Login realizado com sucesso!')
        break
    else:
        print('Não foi possível realizar o login')
