# Nome: Projeto Sísifo
# Descrição: este "script" tem a função de automatizar a tarefa repetitiva de renomear arquivos.
# Autor: Gustavo Carvalho Brito
# Data de criação: 04/04/2024 - 00:16
# Data de lançamento: 15/04/2024 - 23:36
# Última modificação: 27/06/2025 - 23:30
# Versão: 1.1.0

# Libs utilizadas:
import os
from time import sleep


# Funções de “Interface”:
def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\n\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha_menu(tam=42):
    return '-' * tam


def cabecalho_menu(txt):
    print(linha_menu())
    print(txt.center(42))
    print(linha_menu())


def menu(lista):
    print('\033[33mO que deseja fazer?\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha_menu())
    opc = leia_int('\033[33mSua Opção: \033[m')
    print(linha_menu())
    return opc


def confirmacao():
    print('\033[35mAntes de continuar, verifique se os dados informados estão corretos.\033[m')
    while True:
        conf = str(input('\033[35mDeseja continuar? [S/N] \033[m')).upper()
        if conf == 'S' or conf == 'N':
            return conf
        else:
            print('\033[31mERRO! Por favor, responda apenas com "S" para Sim ou "N" para Não.\033[m')


def listando_nomes_novos(pasta):
    print('\n\033[35mRenomeando...')
    print('\nResultados: \033[m\n')
    for arquivo in os.listdir(pasta):
        print(arquivo)
    print('\n\033[35mProcesso finalizado!\033[m')
    print('\n\033[33mRetornando ao menu principal...\033[m\n')
    sleep(1)


# Funções gerais
def contar_itens_da_pasta(pasta):
    itens_na_pasta = os.listdir(pasta)
    arquivos = []
    for item in itens_na_pasta:
        caminho_completo = os.path.join(pasta, item)
        if os.path.isfile(caminho_completo):
            arquivos.append(item)
    quantidade = len(arquivos)
    return quantidade


# Funções de Manipulação de “String”:
def adicao_de_caractere(pasta):
    # Adiciona uma "string" no Início ou no Final da "String".
    while True:
        print('\033[33mEm qual parte do nome você gostaria de adicionar essas caracteres?\033[m')
        print('\033[33m1\033[m - \033[34mInício\033[m')
        print('\033[33m2\033[m - \033[34mFinal\033[m')
        print('\033[33m3\033[m - \033[34mA partir da primeira ocorrência de uma caractere\033[m')
        opc = leia_int('\033[33mSua Opção: \033[m')
        caracteres = str(input('\033[33mDigite EXATAMENTE o texto que deseja adicionar: \033[m'))
        buscar = ''
        if opc == 3:
            buscar = str(input('\033[33m"' + caracteres + '"' + ' deverá ser inserido a partir de qual caractere: \033'
                                                                '[m'))
        conf = confirmacao()
        if conf == 'S':
            break

    if opc == 1:  # Início
        for nome_arquivo in os.listdir(pasta):
            nome_antigo = pasta + '/' + nome_arquivo
            nome_novo = pasta + '/' + caracteres + nome_arquivo
            os.rename(nome_antigo, nome_novo)
        listando_nomes_novos(pasta)

    elif opc == 2:  # Final
        for nome_arquivo in os.listdir(pasta):  # para cada arquivo no diretório
            nome_antigo = pasta + '/' + nome_arquivo
            extensao = nome_arquivo.rfind('.')
            parte1 = pasta + '/' + nome_arquivo[:extensao] + caracteres
            parte2 = nome_arquivo[extensao:]
            nome_novo = parte1 + parte2
            os.rename(nome_antigo, nome_novo)
        listando_nomes_novos(pasta)

    elif opc == 3:  # Ocorrencia de uma caractere
        for nome_arquivo in os.listdir(pasta):
            nome_antigo = pasta + '/' + nome_arquivo
            extensao = nome_arquivo.rfind('.')  # Encontra a extensão
            parte1 = pasta + '/' + nome_arquivo[:extensao] + caracteres  # pega o nome do arquivo antes da extensão
            posicao = parte1.find(buscar)
            if posicao != -1:
                parte2 = nome_arquivo[extensao:]
                nome_novo = parte1[:posicao + 1] + caracteres + parte1[posicao + 1:] + parte2
                os.rename(nome_antigo, nome_novo)
        listando_nomes_novos(pasta)


def remocao_de_caractere(pasta):
    # Remove uma "string" em específico.
    while True:
        remover = str(input('\033[33mDigite EXATAMENTE o texto/caractere que você quer que seja removido: \033[m'))
        conf = confirmacao()
        if conf == 'S':
            break
    for nome_arquivo in os.listdir(pasta):
        try:
            if remover in nome_arquivo:
                nome_antigo = pasta + '/' + nome_arquivo
                nome_novo = nome_antigo.replace(remover, '').strip()
                os.rename(nome_antigo, nome_novo)
        except Exception:
            pass
    listando_nomes_novos(pasta)


def substituicao_de_caractere(pasta):
    # Substitui uma "string" por outra (inclui cada ocorrencia dentro da frase)
    while True:
        remover = str(input('\033[33mDigite EXATAMENTE o texto/caractere que você quer que seja removido: \033[m'))
        substituicao = str(input('\033[33mDigite EXATAMENTE o texto/caractere que deve ser inserido: \033[m'))
        conf = confirmacao()
        if conf == 'S':
            break
    for nome_arquivo in os.listdir(pasta):
        try:
            if remover in nome_arquivo:
                nome_antigo = pasta + '/' + nome_arquivo
                nome_novo = nome_antigo.replace(remover, substituicao)
                os.rename(nome_antigo, nome_novo)
        except Exception:
            pass
    listando_nomes_novos(pasta)


def iniciais_maiusculas(pasta):
    while True:
        conf = confirmacao()
        if conf == 'S':
            break
    for nome_arquivo in os.listdir(pasta):
        nome_antigo = pasta + '/' + nome_arquivo
        extensao = nome_arquivo.rfind('.')
        parte1 = nome_arquivo[:extensao]
        parte2 = nome_arquivo[extensao:]
        alteradas = parte1.title()
        nome_novo = pasta + '/' + alteradas + parte2
        os.rename(nome_antigo, nome_novo)
    listando_nomes_novos(pasta)


def inverter(pasta):
    for nome_arquivo in os.listdir(pasta):
        try:
            nome_antigo = pasta + '/' + nome_arquivo
            extensao = nome_arquivo.rfind('.')
            parte1 = nome_arquivo[:extensao]
            parte2 = nome_arquivo[extensao:]
            palavras = parte1.split(' - ')
            palavras_invertidas = ' - '.join(palavras[::-1])
            nome_novo = pasta + '/' + palavras_invertidas + parte2
            os.rename(nome_antigo, nome_novo)
        except Exception:
            pass
    listando_nomes_novos(pasta)


def recortar_nome(pasta):
    while True:
        print('\033[33mGostaria de recortar em que parte?\033[m')
        print('\033[33m1\033[m - \033[34mQuantidade de caracteres do início\033[m')
        print('\033[33m2\033[m - \033[34mQuantidade de caracteres do final\033[m')
        print('\033[33m3\033[m - \033[34mCortar até encontrar uma determinada caractere lendo do início para o '
              'final\033[m')
        print('\033[33m4\033[m - \033[34mCortar até encontrar uma determinada caractere lendo do final para o '
              'início\033[m')
        opc = leia_int('\033[33mSua Opção: \033[m')
        buscar = ''
        numero = ''
        if opc == 1 or opc == 2:
            numero = int(input('\033[33mQuantidade de caracteres que gostaria de recortar: \033[m'))
        elif opc == 3 or opc == 4:
            buscar = str(input('\033[33mApagar até encontrar qual caractere: \033''[m'))
        conf = confirmacao()
        if conf == 'S':
            break

    if opc == 1:
        # Fatiamento do Início
        for nome_arquivo in os.listdir(pasta):
            nome_antigo = os.path.join(pasta, nome_arquivo)
            if len(nome_arquivo) > numero:
                nome_novo = os.path.join(pasta, nome_arquivo[numero:])
                if nome_novo != nome_antigo:
                    if not os.path.exists(nome_novo):
                        os.rename(nome_antigo, nome_novo)

    elif opc == 2:
        # Fatiamento do Final
        for nome_arquivo in os.listdir(pasta):
            nome_antigo = pasta + '/' + nome_arquivo
            extensao = nome_arquivo.rfind('.')
            parte1 = nome_arquivo[:extensao]
            parte2 = nome_arquivo[extensao:]
            if len(nome_arquivo) > numero:
                nome_novo = pasta + '/' + parte1[:-numero] + parte2
                if nome_novo != nome_antigo:
                    if not os.path.exists(nome_novo):
                        os.rename(nome_antigo, nome_novo)

    elif opc == 3:
        # Busca início até o final
        for nome_arquivo in os.listdir(pasta):
            nome_antigo = pasta + '/' + nome_arquivo
            extensao = nome_arquivo.rfind('.')  # Encontra a localização que a extensão começa
            parte1 = nome_arquivo[:extensao]  # Nome do arquivo antes da extensão
            parte2 = nome_arquivo[extensao:]  # Extensão
            posicao = parte1.find(buscar)  # Encontra a localização da ocorrencia da String fornecida
            if posicao != -1:  # Verifica se a string está no arquivo
                nome_novo = pasta + '/' + parte1[posicao:] + parte2  # Gera o nome renomeado
                if nome_novo != nome_antigo:
                    if not os.path.exists(nome_novo):
                        os.rename(nome_antigo, nome_novo)  # Atribui o nome ao arquivo

    elif opc == 4:
        # Busca final até o início
        for nome_arquivo in os.listdir(pasta):
            nome_antigo = pasta + '/' + nome_arquivo
            extensao = nome_arquivo.rfind('.')  # Encontra a localização que a extensão começa
            parte1 = nome_arquivo[:extensao]  # Nome do arquivo antes da extensão
            parte2 = nome_arquivo[extensao:]  # Extensão
            posicao = parte1.rfind(buscar)  # Encontra a localização da ocorrencia da String fornecida
            if posicao != -1:  # Verifica se a string está no arquivo
                nome_novo = pasta + '/' + parte1[:posicao] + parte2  # Gera o nome renomeado
                if nome_novo != nome_antigo:
                    if not os.path.exists(nome_novo):
                        os.rename(nome_antigo, nome_novo)  # Atribui o nome ao arquivo
    listando_nomes_novos(pasta)


def enumerar(pasta):
    # Enumera cada arquivo no Início ou no Final da "String" de acordo com o que o usuário especificar.
    while True:
        print('\033[33mEm qual parte do nome você gostaria de adicionar os indices? \033[m')
        print('\033[33m1\033[m - \033[34mInício\033[m')
        print('\033[33m2\033[m - \033[34mFinal\033[m')
        print('\033[33m3\033[m - \033[34mA partir da primeira ocorrência de uma caractere\033[m')
        opc = leia_int('\033[33mSua Opção: \033[m')
        print('\033[33mQual formato você gostaria de adicionar? \033[m')
        print('\033[33m1\033[m - \033[34m1, 2, 3... 10... 100.\033[m')
        print('\033[33m2\033[m - \033[34m001, 002, 003... 010.\033[m')
        tipo_contagem = leia_int('\033[33mSua Opção: \033[m')
        antes = str(input('\033[33mDigite EXATAMENTE o texto que deseja adicionar antes do indice (Enter para não '
                          'adicionar nada): \033[m'))
        depois = str(input('\033[33mDigite EXATAMENTE o texto que deseja adicionar depois do indice(Enter para não '
                           'adicionar nada): \033[m'))
        buscar = ''
        if opc == 3:
            buscar = str(input('\033[33m"' + antes + '"' + ' deverá ser inserido a partir de qual caractere: \033'
                                                           '[m'))
        tamanho_quantidade = 0
        if tipo_contagem == 1:
            tamanho_quantidade = 0

        elif tipo_contagem == 2:
            # Cria uma lista apenas com os arquivos (exclui subpastas)
            quantidade = contar_itens_da_pasta(pasta)
            print(f'Quantidade de arquivos na pasta: {quantidade}')
            tamanho_quantidade = len(str(quantidade))

        conf = confirmacao()
        if conf == 'S':
            break

    indice = 0
    if opc == 1:  # Início
        for nome_arquivo in os.listdir(pasta):
            indice += 1
            indice_formatado = f"{indice:0{int(tamanho_quantidade)}d}"
            nome_antigo = pasta + '/' + nome_arquivo
            nome_novo = pasta + '/' + antes + indice_formatado + depois + nome_arquivo
            os.rename(nome_antigo, nome_novo)
        listando_nomes_novos(pasta)

    elif opc == 2:  # Final
        for nome_arquivo in os.listdir(pasta):  # para cada arquivo no diretório
            indice += 1
            indice_formatado = f"{indice:0{int(tamanho_quantidade)}d}"
            nome_antigo = pasta + '/' + nome_arquivo
            extensao = nome_arquivo.rfind('.')
            parte1 = pasta + '/' + nome_arquivo[:extensao] + antes + indice_formatado + depois
            parte2 = nome_arquivo[extensao:]
            nome_novo = parte1 + parte2
            os.rename(nome_antigo, nome_novo)
        listando_nomes_novos(pasta)

    elif opc == 3:  # Ocorrencia de uma caractere
        for nome_arquivo in os.listdir(pasta):
            indice += 1
            indice_formatado = f"{indice:0{int(tamanho_quantidade)}d}"
            nome_antigo = pasta + '/' + nome_arquivo
            extensao = nome_arquivo.rfind('.')  # Encontra a extensão
            parte1 = pasta + '/' + nome_arquivo[:extensao]  # pega o nome do arquivo antes da extensão
            posicao = parte1.find(buscar)
            if posicao != -1:
                parte2 = nome_arquivo[extensao:]
                nome_novo = parte1[:posicao + 1] + antes + indice_formatado + depois + parte1[posicao + 1:] + parte2
                os.rename(nome_antigo, nome_novo)
        listando_nomes_novos(pasta)


def listar_todos_os_arquivos(pasta):
    for arquivo in os.listdir(pasta):
        print(arquivo)
    print()
    print('\033[33mRetornando ao menu principal...\033[m')
    sleep(1)


# Programa Principal
lista_de_opcoes = ['Adição de caractere', 'Remoção de caractere', 'Substituição de texto/caractere',
                   'Transformar caracteres iniciais em maiúsculas', 'Inverter "Título - Nome"',
                   'Recortar nome', 'Enumerar cada arquivo', 'Listar todos os arquivos da pasta', 'Sair.']
cabecalho_menu("\033[1:33mRENOMEADOR DE ARQUIVOS\033[m")
caminho = str(input('\033[33mDigite o caminho da pasta (recomendado copiar endereço da barra do Explorador de '
                    'Arquivos, inserir sem aspas): \033[m'))
print(linha_menu())
while True:
    resposta = menu(lista_de_opcoes)
    if resposta == 1:
        # Adição de caractere
        adicao_de_caractere(caminho)
    elif resposta == 2:
        # Remoção de caractere
        remocao_de_caractere(caminho)
    elif resposta == 3:
        # Substituição de caractere
        substituicao_de_caractere(caminho)
    elif resposta == 4:
        # Transformar caracteres Iniciais em Maiúsculas
        iniciais_maiusculas(caminho)
    elif resposta == 5:
        # Inverter "Título - Nome"
        inverter(caminho)
    elif resposta == 6:
        # Recortar o nome
        recortar_nome(caminho)
    elif resposta == 7:
        # Enumerar os arquivos
        enumerar(caminho)
    elif resposta == 8:
        # Listar todos os arquivos da pasta
        listar_todos_os_arquivos(caminho)
    elif resposta == 9:
        # Sair
        break

# adicionar função de "apagar tudo até x ponto, de trás para frente e de frente para trás. adicionar contador de
# tempo em segundos, minutos e horas, de quantos arquivos foram renomeados, quantos foram ignorados contar também o
# tempo que a operação toda levou
