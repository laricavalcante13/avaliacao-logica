#Menu
print('----------Bem-vindos a pizzaria da Larissa Cavalcante----------')
print('------------------------Cardápio-------------------------------')
print('---------------------------------------------------------------')
print('------|  Tamanho  |  Pizza Salgada (PS)  |  Pizza Doce  |------')
print('------|     P     |       R$ 30,00       |   R$ 34,00   |------')
print('------|     M     |       R$ 45,00       |   R$ 48,00   |------')
print('------|     G     |       R$ 60,00       |   R$ 66,00   |------')
print('---------------------------------------------------------------')

# Solicita o sabor e tamanho correto
def pizza():
    valorTotal = 0
    while True:
        sabor = input('Entre com o sabor desejado (PS/PD): ')
        if sabor == 'PS' or sabor == 'PD':
            break
        else:
            print('Sabor inválido. Tente novamente:')
            continue

    while True:
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')
        if tamanho == 'P' or tamanho == 'M' or tamanho == 'G':
            break
        else:
            print('Tamanho inválido. Tente novamente:')
            continue

    # Valores das pizzas
    valorPsP = 30.00
    valorPsM = 45.00
    valorPsG = 60.00
    valorPdP = 34.00
    valorPdM = 48.00
    valorPdG = 66.00

    # Mostra o sabor e tamanho escolhido e o valor da pizza
    if sabor == 'PS' and tamanho == 'P':
        valorTotal = valorPsP
        print(f'Você pediu uma Pizza Salgada no tamanho P: R$ {valorPsP}')
    elif sabor == 'PS' and tamanho == 'M':
        valorTotal = valorPsM
        print(f'Você pediu uma Pizza Salgada no tamanho M: R$ {valorPsM}')
    elif sabor == 'PS' and tamanho == 'G':
        valorTotal = valorPsG
        print(f'Você pediu uma Pizza Salgada no tamanho G: R$ {valorPsG}')
    else:
        if sabor == 'PD' and tamanho == 'P':
            valorTotal = valorPdP
            print(f'Você pediu uma Pizza Doce no tamanho P: R$ {valorPdP}')
        elif sabor == 'PD' and tamanho == 'M':
            valorTotal = valorPdM
            print(f'Você pediu uma Pizza Doce no tamanho M: R$ {valorPdM}')
        else:
            valorTotal = valorPdG
            print(f'Você pediu uma Pizza Doce no tamanho G: R$ {valorPdG}')

    return valorTotal

# Total inicial
valor_total = 0

# Primeiro pedido
valor_total += pizza()

# Verifica se mais algum item será adicionado
while True:
    resposta = input('Deseja mais alguma coisa? (S/N): ')
    if resposta == 'S':
        valor_total += pizza()
    else:
        break

# Calcula o valor total a ser pago
print(f'O valor total a ser pago é: R$ {valor_total}')
