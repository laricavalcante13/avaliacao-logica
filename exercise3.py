print('Bem-vindos a Madeireira da lenhadora Larissa Cavalcante')

#Escolhe o tipo de madeira
def escolha_tipo(): 
    # Valor da madeira
    valorMadeira = {
        'PIN': 150.4,
        'PER': 170.2,
        'MOG': 190.9,
        'IPE': 210.1,
        'IMB': 220.7
    }
    
    # Pergunta o tipo de madeira e verifica se a opção é válida
    while True:
        try:
            tipoMadeira = input('Entre com o tipo de madeira desejado:\nPIN - Tora de Pinho\nPER - Tora de Peroba\nMOG - Tora de Mogno\nIPE - Tora de Ipê\nIMB - Tora de Imbuia\n')
            
            if tipoMadeira in valorMadeira:
                return valorMadeira[tipoMadeira] 
            else:
                raise ValueError('Escolha inválida, entre com o modelo novamente.')   
        
        except ValueError as escolhaInvalida:
            print(escolhaInvalida)

valorMadeira = escolha_tipo()#Retorna valor da madeira fora da função

#Solicita a quantidade de toras e verifica se valor é válido
def qtd_toras():
    while True:
        try:
           qtdToras = float(input('Entre com a quantidade de toras (m³):'))

           if qtdToras < 100:
               desconto = 0
           elif qtdToras >= 100 and qtdToras < 500:
               desconto = 0.04
           elif qtdToras >= 500 and qtdToras < 1000:
               desconto = 0.09
           elif qtdToras >= 1000 and qtdToras < 2000:
               desconto = 0.16
           else:
               raise ValueError('Não aceitamos pedidos com essa quantidade de toras.\nPor favor, entre com a quantidade novamente.')
           return qtdToras,desconto

        except ValueError as qtdInvalida:
            print(qtdInvalida)
        
qtdToras,desconto = qtd_toras()#Retorna qtd de toras e desconto fora da função

#Pergunta qual tipo de transporte será usado
def transporte():
    while True:
        try:
            tipoTransp = int(input('Escolha o tipo de transporte:\n1-Transporte Rodoviário - R$ 1000,00\n2-Transporte Ferroviário - R$ 2000,00\n3-Transporte Hidroviário - R$ 2500,00\n'))
            
            if tipoTransp == 1:
                valorTransporte = 1000
            elif tipoTransp == 2:
                valorTransporte = 2000
            elif tipoTransp == 3:
                valorTransporte = 2500
            else:
                 raise ValueError('Tente novamente.')
            return valorTransporte

        except ValueError as transpInvalido:
            print(transpInvalido)

valorTransporte = transporte()#Retorna valor do transporte fora da função

#Cálculo do valor total            
total = float(valorMadeira * qtdToras * (1-desconto))
totalfinal = total + valorTransporte
print(f'Total: R$ {totalfinal}')
