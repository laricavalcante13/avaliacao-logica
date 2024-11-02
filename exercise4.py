print('Bem-vindo à lista de contatos de Larissa Cavalcante')
print('---------------------------------------------------')
print('---------------- MENU PRINCIPAL -------------------')

# Lista de contatos e id global
lista_contatos = []
id_global = 5032270

# Função para cadastrar contato
def cadastrar_contato(id_global):
    print('---------------------------------------------------')
    print('------------- MENU CADASTRAR CONTATO --------------')
    print(f'Id do contato: {id_global}')

    nome = input('Por favor, entre com o nome do contato: ')
    atividade = input('Por favor, entre com a atividade do contato: ')
    telefone = int(input('Por favor, entre com o telefone do contato: '))

    # Dicionário de contato
    contato = {
        'id': id_global,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
    }

    # Copiando o dicionário
    lista_contatos.append(contato.copy())
    print('---------------------------------------------------')

# Função para consultar contatos
def consultar_contato():
    print('---------------------------------------------------')
    print('------------- MENU CONSULTAR CONTATO --------------')

    while True:
        consulta = int(input('Escolha a opção desejada:\n1 - Consultar todos os cadastros\n2 - Consultar contato por ID\n3 - Consultar contato por atividade\n4 - Retornar ao menu principal\n'))
        if consulta == 1:
            if lista_contatos:
                for contato in lista_contatos:
                    print(contato)
            else:
                print('Nenhum contato cadastrado.')
        elif consulta == 2:
            id_consulta = int(input('Digite o ID do contato: '))
            encontrado = False
            for contato in lista_contatos:
                if contato['id'] == id_consulta:
                    print(contato)
                    encontrado = True
                    break
            if not encontrado:
                print(f'Contato com ID {id_consulta} não encontrado.')

        elif consulta == 3:
            atividade_consulta = input('Digite a atividade do contato: ')
            encontrado = False
            for contato in lista_contatos:
                if contato['atividade'] == atividade_consulta:
                    print(contato)
                    encontrado = True
            if not encontrado:
                print(f'Nenhum contato com a atividade "{atividade_consulta}" foi encontrado.')

        elif consulta == 4:
            break
        else:
            print('Opção inválida. Tente novamente.')

    print('---------------------------------------------------')

# Função para remover contato
def remover_contato():
    print('---------------------------------------------------')
    print('------------- MENU REMOVER CONTATO --------------')

    remover = int(input('Digite o ID do contato a ser removido: '))

    encontrado = False
    for contato in lista_contatos:
        if contato['id'] == remover:
            lista_contatos.remove(contato)
            print(f'Contato com ID {remover} foi removido.')
            encontrado = True
            break
    if not encontrado:
        print(f'Contato com ID {remover} não encontrado.')

    print('---------------------------------------------------')

# Menu
while True:
    escolha = int(input('Escolha a opção desejada:\n1 - Cadastrar Contato\n2 - Consultar Contato\n3 - Remover Contato\n4 - Sair\n'))
    if escolha == 1:
        cadastrar_contato(id_global)
        id_global += 1  # Incrementa o ID global após o cadastro
    elif escolha == 2:
        consultar_contato()
    elif escolha == 3:
        remover_contato()
    elif escolha == 4:
        break
    else:
        print('Opção inválida. Tente novamente.')

