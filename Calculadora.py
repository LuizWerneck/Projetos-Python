# Primeiro chamo a função bemvindo():
def bemvindo():
    print('''
Seja bem vindo a calculadora Werneck
''')
bemvindo()
# depois a função calculadora() para iniciar os calculos:
def calculadora():
    operador = input('''
Por gentileza, insira o simbolo matemático para o cálculo, sendo:
+ para adição
- para subtração
* para multiplicação
/ para divisão
** para exponenciação
% para resto de divisão (módulo)
''')

    num_1 = int(input('Por gentileza, insira o primeiro número: '))
    num_2 = int(input('Por gentileza, insira o segundo número: '))

    if operador == '+':
        print(f'{num_1} + {num_2} = ')
        print(num_1 + num_2)

    elif operador == '-':
        print(f'{num_1} - {num_2} = ')
        print(num_1 - num_2)

    elif operador == '*':
        print(f'{num_1} * {num_2} = ')
        print(num_1 * num_2)

    elif operador == '/':
        print(f'{num_1} / {num_2} = ')
        print(num_1 / num_2)
    
    elif operador == '**':
        print(f'{num_1} ** {num_2} = ')
        print(num_1 ** num_2)

    elif operador == '%':
        print(f'{num_1} % {num_2} = ')
        print(num_1 % num_2)

    else:
        print('Você não digitou um simbolo matemático válido, inicie o programa novamente.')

    # Adicionando a função denovo() para função calculadora()
    denovo()

def denovo():
    calc_denovo = input('''
Você quer usar a calculadora de novo?
Por favor digita S para SIM e N para NÃO
''')

    if calc_denovo.upper() == 'S':
        calculadora()
    elif calc_denovo.upper() == 'N':
        print('Grato por utilizar a calculadora Werneck.')
    else:
        denovo()

calculadora()