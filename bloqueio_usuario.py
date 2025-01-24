count = 0

while True:
    usuario = input('Informe seu usuário: ')
    senha = input('Informe sua senha: ')

    if usuario != 'aluno':
        print('Usuário incorreto ou inexistente')
    elif (usuario == 'aluno') and (senha == 'segredo'):
        print('Bem Vindo')
    else:
        if count == 2:
            print('Usuário bloqueado')
            break
        count = count + 1
        print('Senha incorreta, mais '+str(3-count)+' tentivas o usuário será bloqueado')
