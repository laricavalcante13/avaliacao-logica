print('Bem vindo ao sistema de Larissa Cavalcante')

#Solicita as informações de valor base e idade do cliente
valorBase = float(input(f'Informe o valor base do plano: '))
idade = int(input(f'Informe a idade do cliente: '))

#Calcula o valor mensal de acordo com a idade
if idade >= 0 and idade < 19: 
    valorMensal = valorBase * 100/100

elif idade >= 19 and idade < 29:
    valorMensal = valorBase * 150/100

elif idade >= 29 and idade < 39:
    valorMensal = valorBase * 225/100

elif idade >= 39 and idade < 49:
    valorMensal = valorBase * 240/100

elif idade >= 49 and idade < 59:
    valorMensal = valorBase * 350/100

elif idade >= 59:
    valorMensal = valorBase * 600/100

#Caso a idade informada seja inválida
else:
    print('Idade inválida')

#Calcula o valor mensal caso a idade seja válida
if idade >= 0:
    print(f'O valor mensal do plano é {valorMensal}')

#Informa se a idade é maior ou igual a 29 anos
if idade >=29:
    print('Idade maior ou igual a 29 anos')
