# Nome: Projeto Sísifo
# Descrição: este "script" tem a função de automatizar a tarefa repetitiva de renomear arquivos.
# Autor: Gustavo Carvalho Brito
# Data de criação: 04/04/2024 - 00:16
# Data de lançamento: 15/04/2024 - 23:36
# Última modificação: 15/04/2024
# Versão: 1.0.0

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


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    print('\033[33mO que deseja fazer?\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leia_int('\033[33mSua Opção: \033[m')
    print(linha())
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


# Funções de Manipulação de “String”:
def adicao_de_caractere(pasta):
    # Adiciona uma "string" no Início ou no Final da "String".
    while True:
        print('\033[33mEm qual parte do nome você gostaria de adicionar essas caracteres?\033[m')
        print('\033[33m1\033[m - \033[34mInício\033[m')
        print('\033[33m2\033[m - \033[34mFinal\033[m')
        opc = leia_int('\033[33mSua Opção: \033[m')
        caracteres = str(input('\033[33mDigite EXATAMENTE o texto que deseja adicionar: \033[m'))
        conf = confirmacao()
        if conf == 'S':
            break
    if opc == 1:
        for nome_arquivo in os.listdir(pasta):
            nome_antigo = pasta + '/' + nome_arquivo
            nome_novo = pasta + '/' + caracteres + nome_arquivo
            os.rename(nome_antigo, nome_novo)
        listando_nomes_novos(pasta)
    elif opc == 2:
        for nome_arquivo in os.listdir(pasta):
            nome_antigo = pasta + '/' + nome_arquivo
            extensao = nome_arquivo.rfind('.')
            parte1 = pasta + '/' + nome_arquivo[:extensao] + caracteres
            parte2 = nome_arquivo[extensao:]
            nome_novo = parte1 + parte2
            os.rename(nome_antigo, nome_novo)
        listando_nomes_novos(pasta)


def remocao_de_caractere(pasta):
    # Remove uma "string" em específico.
    remover = str(input('\033[33mDigite EXATAMENTE o texto/caractere que você quer que seja removido: \033[m'))
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
    remover = str(input('\033[33mDigite EXATAMENTE o texto/caractere que você quer que seja removido: \033[m'))
    substituicao = str(input('\033[33mDigite EXATAMENTE o texto/caractere que deve ser inserido: \033[m'))
    for nome_arquivo in os.listdir(pasta):
        try:
            if remover in nome_arquivo:
                nome_antigo = pasta + '/' + nome_arquivo
                nome_novo = nome_antigo.replace(remover, substituicao)
                os.rename(nome_antigo, nome_novo)
        except Exception:
            pass
    listando_nomes_novos(pasta)


def maiusculas(pasta):
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
        print('\033[33m1\033[m - \033[34mInício\033[m')
        print('\033[33m2\033[m - \033[34mFinal\033[m')
        opc = leia_int('\033[33mSua Opção: \033[m')
        numero = int(input('\033[33mQuantidade de caracteres que gostaria de recortar: \033[m'))
        if opc == 1:
            # Fatiamento do Início
            for nome_arquivo in os.listdir(pasta):
                try:
                    nome_antigo = pasta + '/' + nome_arquivo
                    nome_novo = pasta + '/' + nome_arquivo[numero:]
                    os.rename(nome_antigo, nome_novo)
                except Exception:
                    pass
            listando_nomes_novos(pasta)
        elif opc == 2:
            # Fatiamento do Final
            for nome_arquivo in os.listdir(pasta):
                try:
                    nome_antigo = pasta + '/' + nome_arquivo
                    extensao = nome_arquivo.rfind('.')
                    parte1 = nome_arquivo[:extensao]
                    parte2 = nome_arquivo[extensao:]
                    nome_recortado = parte1[:-numero]
                    nome_novo = pasta + '/' + nome_recortado + parte2
                    os.rename(nome_antigo, nome_novo)
                except Exception:
                    pass
            listando_nomes_novos(pasta)
        break


def listar_todos_os_arquivos(pasta):
    for arquivo in os.listdir(pasta):
        print(arquivo)
    print()
    print('\033[33mRetornando ao menu principal...\033[m')
    sleep(1)


# Programa Principal
lista_de_opcoes = ['Adição de caractere', 'Remoção de caractere', 'Substituição de texto/caractere',
                   'Transformar caracteres iniciais em maiúsculas', 'Inverter "Título - Nome"',
                   'Recortar nome', 'Listar todos os arquivos da pasta', 'Sair.']
cabecalho("\033[1:33mRENOMEADOR DE ARQUIVOS\033[m")
caminho = str(input('\033[33mDigite o caminho da pasta (recomendado copiar endereço da barra do Explorador de '
                    'Arquivos): \033[m'))
print(linha())
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
        maiusculas(caminho)
    elif resposta == 5:
        # Inverter "Título - Nome"
        inverter(caminho)
    elif resposta == 6:
        # Recortar o nome
        recortar_nome(caminho)
    elif resposta == 7:
        # Listar todos os arquivos da pasta
        listar_todos_os_arquivos(caminho)
    elif resposta == 8:
        # Sair
        break
