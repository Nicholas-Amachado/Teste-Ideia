import time
def pagina ():
    nome = input('Opa usuario novo!! Qual é seu nome?')
    lin('PÁGINA INICIAL')
    print(f'Seja bem vindo a nossa Pagina {nome}')


def menu (*valor):
    linhas =len(valor)
    topico = list(valor)
    print('----------------MENU----------------')
    print('~ESCOLHA UM DOS TÓPICOS PELO NÚMERO~')
    if linhas > 4:
        print(f'|[1] {topico[0]}')
        print(f'|[2] {topico[1]}')
        print(f'|[3] {topico[2]}')
        print(f'|[4] {topico[3]}')
        print(f'|[5] {topico[4]}')
        print('_' * 36)
    elif linhas > 3:
        print(f'|[1] {topico[0]}')
        print(f'|[2] {topico[1]}')
        print(f'|[3] {topico[2]}')
        print(f'|[4] {topico[3]}')
        print('_' * 36)
    elif linhas > 2:
        print(f'|[1] {topico[0]}')
        print(f'|[2] {topico[1]}')
        print(f'|[3] {topico[2]}')
        print('_' * 36)
    elif linhas > 1:
        print(f'|[1] {topico[0]}')
        print(f'|[2] {topico[1]}')
        print('_' * 36)



def lin (frase):
    print('-' * 36)
    print(frase.title())
    print('-' * 36)


def area():
    while True:
        print('~~~~~~~~~~Calculo De Area~~~~~~~~~~~')
        largura = float(input('insira a área do terreno:'))

        comprimento= float(input('agora o comprimento:'))

        print(f'O terreno de {largura} x {comprimento} da no total de área de area de {largura * comprimento}metros quadrados')

        continua = input('deseja calcular novamente?')
        if continua == 'sim' or continua == 's':
            continue
        else:
            return cadastro()


def cadastro ():
    while True:
        lin('ÁREA DE CADASTRO')
        nomecompleto = input('informe o seu nome:')
        if not nomecompleto.isalpha():
            print('nome invalido!!!')
            continue
        else:
            idade = input('insira a sua idade:')
            if not idade.isnumeric():
                print('coloque apenas NÚMEROS')
                continue
        print('-' * 20)
        print(f'seja bem vindo {nomecompleto}!!')
        time.sleep(1)
        menu('calculo de area','bolsa','moeda')

        escolha = input('OQUE VOCÊ DESEJA SABER? ')
        time.sleep(1)
        if not escolha.isnumeric():
            print('INVALIDO!! É aceito apenas numeros!!')

        if escolha == '1' or escolha == 'um':
            return area()


def contagem (valor):
     return len(valor)



cadastro()


























