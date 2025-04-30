# Nesse módulo são criadas as fórmulas de manipulação de string

import os

def iniciais_maiusculas(string):
    # Aqui vai o endereço do arquivo
    folder = str(input('Digite o caminho da pasta (recomenado copiar endereço da barra do Explorador de arquivos): '))
    for file_name in os.listdir(folder):
        old_name = folder + file_name
        new_name = folder + 'AAAA - ' + file_name
        os.rename(old_name, new_name)
def adicao_de_caractere(string, posicao):
def remocao_de_caractere(string):
def substituicao_de_caractere(atual, novo):
def criar_lista_de_nomes_dos_arquivos():
