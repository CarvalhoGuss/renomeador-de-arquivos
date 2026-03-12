# Nome: Projeto Sísifo
# Descrição: este "script" tem a função de automatizar a tarefa repetitiva de renomear arquivos.
# Autor: Gustavo Carvalho Brito
# Data de criação: 04/04/2024 - 00:16
# Data de lançamento: 15/04/2024 - 23:36
# Última modificação: 11/03/2026 - 19:00
# Versão: 1.2.0

# Libs utilizadas:
import os
import time


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


# Funções gerais
def contar_itens_da_pasta(pasta):
    quantidade = 0
    for entrada in os.scandir(pasta):
        if entrada.is_file():
            quantidade += 1
    return quantidade


def relatorio(pasta, tempo_inicial, tempo_final, arquivos_renomeados, arquivos_ignorados):
    print('\n\033[35mRenomeando...')
    print('\nResultados: \033[m\n')
    for entrada in os.scandir(pasta):
        print(entrada.name)
    print('\n\033[35mProcesso finalizado!\033[m')
    tempo_total = tempo_final - tempo_inicial
    print(f'\n\033[33mTarefa realizada em {tempo_total:.4f} segundos.\033[m\n')
    print(f'\n\033[33mQuantidade de arquivos analizados: {arquivos_ignorados + arquivos_renomeados}\033[m\n')
    print(f'\033[33mQuantidade de arquivos renomeados: {arquivos_renomeados}\033[m\n')
    print(f'\033[33mQuantidade de arquivos ignorados: {arquivos_ignorados}\033[m\n')
    print('\n\033[33mRetornando ao menu principal...\033[m\n')
    time.sleep(1)


def processar_renomeacao(pasta, opc, caracteres, buscar=''):
    arquivos_renomeados = 0
    arquivos_ignorados = 0
    tempo_inicial = time.time()

    # "Congela" a pasta em uma lista para evitar loops infinitos
    arquivos = list(os.scandir(pasta))

    for entrada in arquivos:
        if not entrada.is_file():
            continue

        nome_arquivo = entrada.name
        nome_antigo = entrada.path
        nome_base, extensao = os.path.splitext(nome_arquivo)

        # --- Lógica de Construção do Nome ---
        if opc == 1:  # Início
            nome_novo_base = caracteres + nome_base
        elif opc == 2:  # Final
            nome_novo_base = nome_base + caracteres
        elif opc == 3:  # Após ocorrência
            posicao = nome_base.find(buscar)
            if posicao == -1:
                arquivos_ignorados += 1
                continue
            nome_novo_base = nome_base[:posicao + 1] + caracteres + nome_base[posicao + 1:]

        nome_novo = os.path.join(pasta, nome_novo_base + extensao)

        # --- Execução com Segurança ---
        if nome_novo != nome_antigo and not os.path.exists(nome_novo):
            os.rename(nome_antigo, nome_novo)
            arquivos_renomeados += 1
        else:
            arquivos_ignorados += 1

    tempo_final = time.time()
    relatorio(pasta, tempo_inicial, tempo_final, arquivos_renomeados, arquivos_ignorados)



# Funções de Manipulação no Menu:
def adicao_de_caractere(pasta):
    # Adiciona uma "string" no Início ou no Final da "String".
    while True:
        print('\033[33mEm qual parte do nome você gostaria de adicionar essas caracteres?\033[m')
        print('\033[33m1\033[m - \033[34mInício\033[m')
        print('\033[33m2\033[m - \033[34mFinal\033[m')
        print('\033[33m3\033[m - \033[34mApós a ocorrencia de uma caractere\033[m')
        opc = leia_int('\033[33mSua Opção: \033[m')
        caracteres = str(input('\033[33mDigite EXATAMENTE o texto que deseja adicionar: \033[m'))
        buscar = ''
        if opc == 3:
            buscar = str(input('\033[33m"' + caracteres + '"' + ' deverá ser inserido a partir de qual caractere: \033'
                                                                '[m'))
        conf = confirmacao()
        if conf == 'S':
            break
    tempo_inicial = time.time()
    arquivos_renomeados = 0
    arquivos_ignorados = 0
    if opc == 1:  # Início
        arquivos = list(os.scandir(pasta))
        for entrada in arquivos:
            if not entrada.is_file():  # ignora pastas
                continue
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            nome_base, extensao = os.path.splitext(nome_arquivo)

            nome_novo = os.path.join(pasta, caracteres + nome_base + extensao)
            os.rename(nome_antigo, nome_novo)
            arquivos_renomeados += 1

    elif opc == 2:  # Final
        arquivos = list(os.scandir(pasta))
        for entrada in arquivos:  # para cada arquivo no diretório
            if not entrada.is_file():
                continue
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            nome_base, extensao = os.path.splitext(nome_arquivo)
            nome_novo = os.path.join(pasta, nome_base + caracteres + extensao)
            os.rename(nome_antigo, nome_novo)
            arquivos_renomeados += 1

    elif opc == 3:  # Ocorrencia de uma caractere
        arquivos = list(os.scandir(pasta))
        for entrada in arquivos:
            if not entrada.is_file():
                continue
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            nome_base, extensao = os.path.splitext(nome_arquivo)  # Extensão
            posicao = nome_base.find(buscar)  # Encontra a localização da ocorrencia da String fornecida
            if posicao != -1:  # Verifica se a string está no arquivo
                nome_novo = os.path.join(pasta, nome_base[:posicao + 1] + caracteres + nome_base[posicao + 1:] +
                                         extensao)  # Gera o nome renomeado
                if nome_novo != nome_antigo:
                    if not os.path.exists(nome_novo):
                        os.rename(nome_antigo, nome_novo)  # Atribui o nome ao arquivo
                        arquivos_renomeados += 1
                    else:
                        arquivos_ignorados += 1
                else:
                    arquivos_ignorados += 1
            else:
                arquivos_ignorados += 1
    tempo_final = time.time()
    relatorio(pasta, tempo_inicial, tempo_final, arquivos_renomeados, arquivos_ignorados)


def remocao_de_caractere(pasta):
    # Remove uma "string" em específico.
    while True:
        remover = str(input('\033[33mDigite EXATAMENTE o texto/caractere que você quer que seja removido: \033[m'))
        conf = confirmacao()
        if conf == 'S':
            break
    tempo_inicial = time.time()
    arquivos_renomeados = 0
    arquivos_ignorados = 0
    arquivos_existentes = set(os.listdir(pasta))  # carrega tudo na memória
    arquivos = list(os.scandir(pasta))
    for entrada in arquivos:
        if not entrada.is_file():
            arquivos_ignorados += 1
            continue
        nome_arquivo = entrada.name
        nome_antigo = entrada.path
        nome_base, extensao = os.path.splitext(nome_arquivo)
        if remover in nome_base:
            novo_base = nome_base.replace(remover, '', 1).strip()
            nome_novo = novo_base + extensao
            if nome_novo == nome_arquivo:
                arquivos_ignorados += 1
                continue
            if os.path.exists(nome_novo):
                arquivos_ignorados += 1
                continue
            caminho_novo = os.path.join(pasta, nome_novo)
            os.rename(nome_antigo, caminho_novo)

            # atualiza o set
            arquivos_existentes.remove(nome_arquivo)
            arquivos_existentes.add(nome_novo)
            arquivos_renomeados += 1
        else:
            arquivos_ignorados += 1
    tempo_final = time.time()
    relatorio(pasta, tempo_inicial, tempo_final, arquivos_renomeados, arquivos_ignorados)


def substituicao_de_caractere(pasta):
    # Substitui uma "string" por outra (inclui cada ocorrencia dentro da frase)
    while True:
        remover = str(input('\033[33mDigite EXATAMENTE o texto/caractere que você quer que seja removido: \033[m'))
        substituicao = str(input('\033[33mDigite EXATAMENTE o texto/caractere que deve ser inserido: \033[m'))
        conf = confirmacao()
        if conf == 'S':
            break
    tempo_inicial = time.time()
    arquivos_renomeados = 0
    arquivos_ignorados = 0
    arquivos = list(os.scandir(pasta))
    for entrada in arquivos:
        if not entrada.is_file():
            continue
        nome_arquivo = entrada.name
        nome_antigo = entrada.path
        nome_base, extensao = os.path.splitext(nome_arquivo)
        if remover in nome_arquivo:
            nome_base = nome_base.replace(remover, substituicao, 1)
            nome_novo = os.path.join(pasta, nome_base + extensao)
            if nome_novo != nome_antigo and not os.path.exists(nome_novo):
                os.rename(nome_antigo, nome_novo)
                arquivos_renomeados += 1
            else:
                arquivos_ignorados += 1
        else:
            arquivos_ignorados += 1
    tempo_final = time.time()
    relatorio(pasta, tempo_inicial, tempo_final, arquivos_renomeados, arquivos_ignorados)


def iniciais_maiusculas(pasta):
    while True:
        conf = confirmacao()
        if conf == 'S':
            break
    tempo_inicial = time.time()
    arquivos_renomeados = 0
    arquivos_ignorados = 0
    arquivos = list(os.scandir(pasta))
    for entrada in arquivos:
        if not entrada.is_file():
            continue
        nome_arquivo = entrada.name
        nome_antigo = entrada.path
        nome_base, extensao = os.path.splitext(nome_arquivo)
        alteradas = nome_base.title()
        nome_novo = os.path.join(pasta, alteradas + extensao)
        if nome_antigo != nome_novo:
            os.rename(nome_antigo, nome_novo)
            arquivos_renomeados += 1
        else:
            arquivos_ignorados += 1
    tempo_final = time.time()
    relatorio(pasta, tempo_inicial, tempo_final, arquivos_renomeados, arquivos_ignorados)


def inverter(pasta):
    #Falta adicionar verificação S/N aqui
    while True:
        conf = confirmacao()
        if conf == 'S':
            break
    tempo_inicial = time.time()
    arquivos_renomeados = 0
    arquivos_ignorados = 0
    arquivos = list(os.scandir(pasta))
    for entrada in arquivos:
        if not entrada.is_file():
            continue
        nome_arquivo = entrada.name
        nome_antigo = entrada.path
        if ' - ' in nome_arquivo:
            nome_base, extensao = os.path.splitext(nome_arquivo)
            palavras = nome_base.split(' - ')
            palavras_invertidas = ' - '.join(palavras[::-1])
            nome_novo = os.path.join(pasta, palavras_invertidas + extensao)
            if nome_novo != nome_antigo and not os.path.exists(nome_novo):
                os.rename(nome_antigo, nome_novo)
                arquivos_renomeados += 1
            else:
                arquivos_ignorados += 1
        else:
            arquivos_ignorados += 1
    tempo_final = time.time()
    relatorio(pasta, tempo_inicial, tempo_final, arquivos_renomeados, arquivos_ignorados)


def recortar_nome(pasta):
    while True:
        print('\033[33mGostaria de recortar em que parte?\033[m')
        print('\033[33m1\033[m - \033[34mQuantidade de caracteres do início\033[m')
        print('\033[33m2\033[m - \033[34mQuantidade de caracteres do final\033[m')
        print('\033[33m3\033[m - \033[34mCortar até encontrar uma determinada caractere lendo do início para o '
              'final\033[m')
        print('\033[33m4\033[m - \033[34mCortar até encontrar uma determinada caractere lendo do final para o '
              'início\033[m')
        print('\033[33m5\033[m - \033[34mManter um número X de caracteres e cortar o resto (Do começo para o final)'
              '\033[m')
        print('\033[33m6\033[m - \033[34mManter um número X de caracteres e cortar o resto (Do final para o começo)'
              '\033[m')
        print('\033[33m7\033[m - \033[34mRecortar o que estiver entre 2 caracteres\033[m')
        opc = leia_int('\033[33mSua Opção: \033[m')
        numero = ''
        buscar = ''
        manter = ''
        divisor_1 = ''
        divisor_2 = ''
        if opc == 1 or opc == 2:
            numero = int(input('\033[33mQuantidade de caracteres que gostaria de recortar: \033[m'))
        elif opc == 3 or opc == 4:
            buscar = str(input('\033[33mApagar até encontrar qual caractere: \033''[m'))
        elif opc == 5 or opc == 6:
            manter = int(input('\033[33mQuantidade de caracteres que gostaria de manter: \033[m'))
        elif opc == 7:
            divisor_1 = str(input('\033[33mDigite a parte que ele deve iniciar o corte: \033[m'))
            divisor_2 = str(input('\033[33mDigite a parte que ele deve parar o corte: \033[m'))
        conf = confirmacao()
        if conf == 'S':
            break
    tempo_inicial = time.time()
    arquivos_renomeados = 0
    arquivos_ignorados = 0

    if opc == 1:
        # Fatiamento do Início
        arquivos = list(os.scandir(pasta))
        for entrada in arquivos:
            if not entrada.is_file():
                continue
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            nome_base, extensao = os.path.splitext(nome_arquivo)
            if len(nome_base) > numero:
                nome_novo = os.path.join(pasta, nome_base[numero:]) + extensao
                if nome_novo != nome_antigo:
                    if not os.path.exists(nome_novo):
                        os.rename(nome_antigo, nome_novo)
                        arquivos_renomeados += 1
                    else:
                        arquivos_ignorados += 1
                else:
                    arquivos_ignorados += 1
            else:
                arquivos_ignorados += 1

    elif opc == 2:
        # Fatiamento do Final
        arquivos = list(os.scandir(pasta))
        for entrada in arquivos:
            if not entrada.is_file():
                continue
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            nome_base, extensao = os.path.splitext(nome_arquivo)
            if len(nome_base) > numero:
                nome_novo = pasta + '/' + nome_base[:-numero] + extensao
                if nome_novo != nome_antigo:
                    if not os.path.exists(nome_novo):
                        os.rename(nome_antigo, nome_novo)
                        arquivos_renomeados += 1
                    else:
                        arquivos_ignorados += 1
                else:
                    arquivos_ignorados += 1
            else:
                arquivos_ignorados += 1

    elif opc == 3:
        # Busca início até o final
        arquivos = list(os.scandir(pasta))
        for entrada in arquivos:
            if not entrada.is_file():
                continue
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            nome_base, extensao = os.path.splitext(nome_arquivo) # Encontra a extenção do arquivo
            posicao = nome_base.find(buscar)  # Encontra a localização da ocorrencia da String fornecida
            if posicao != -1:  # Verifica se a string está no arquivo
                nome_novo = os.path.join(pasta, nome_base[posicao:] + extensao)  # Gera o nome renomeado
                if nome_novo != nome_antigo:
                    if not os.path.exists(nome_novo):
                        os.rename(nome_antigo, nome_novo)  # Atribui o nome ao arquivo
                        arquivos_renomeados += 1
                    else:
                        arquivos_ignorados += 1
                else:
                    arquivos_ignorados += 1
            else:
                arquivos_ignorados += 1

    elif opc == 4:
        # Busca final até o início
        arquivos = list(os.scandir(pasta))
        for entrada in arquivos:
            if not entrada.is_file():
                continue
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            nome_base, extensao = os.path.splitext(nome_arquivo)
            posicao = nome_base.rfind(buscar)  # Encontra a localização da ocorrencia da String fornecida
            if posicao != -1:  # Verifica se a string está no arquivo
                nome_novo = os.path.join(pasta, nome_base[:posicao] + extensao)  # Gera o nome renomeado
                if nome_novo != nome_antigo:
                    if not os.path.exists(nome_novo):
                        os.rename(nome_antigo, nome_novo)  # Atribui o nome ao arquivo
                        arquivos_renomeados += 1
                    else:
                        arquivos_ignorados += 0
                else:
                    arquivos_ignorados += 0
            else:
                arquivos_ignorados += 0

    elif opc == 5:
        arquivos = list(os.scandir(pasta))
        for entrada in arquivos:
            if not entrada.is_file():
                continue
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            nome_base, extensao = os.path.splitext(nome_arquivo)
            if len(nome_base) > manter:
                nome_novo = os.path.join(pasta, nome_base[:manter] + extensao)
                if nome_novo != nome_antigo:
                    if not os.path.exists(nome_novo):
                        os.rename(nome_antigo, nome_novo)
                        arquivos_renomeados += 1
                    else:
                        arquivos_ignorados += 1
                else:
                    arquivos_ignorados += 1
            else:
                arquivos_ignorados += 1

    elif opc == 6:
        arquivos = list(os.scandir(pasta))
        for entrada in arquivos:
            if not entrada.is_file():
                continue
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            nome_base, extensao = os.path.splitext(nome_arquivo)
            if len(nome_base) > manter:
                novo_base = nome_base[-manter:]
                nome_novo = os.path.join(pasta, nome_base[-manter:] + extensao)
                if nome_arquivo != novo_base + extensao:
                    if not os.path.exists(nome_novo):
                        os.rename(nome_antigo, nome_novo)
                        arquivos_renomeados += 1
                    else:
                        arquivos_ignorados += 1
                else:
                    arquivos_ignorados += 1
            else:
                arquivos_ignorados += 1

    elif opc == 7:
        arquivos = list(os.scandir(pasta))
        for entrada in arquivos:
            if not entrada.is_file():
                continue
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            nome_base, extensao = os.path.splitext(nome_arquivo)  # Separa a extensão
            posicao_inicio = nome_base.find(divisor_1)
            posicao_final = nome_base.find(divisor_2)
            if posicao_inicio != -1 and posicao_final != -1 and posicao_final > posicao_inicio:
                nome_base = nome_base[:posicao_inicio + len(divisor_1)] + nome_base[posicao_final:]
                nome_novo = os.path.join(pasta, nome_base + extensao)
                if nome_novo != nome_antigo:
                    if not os.path.exists(nome_novo):
                        os.rename(nome_antigo, nome_novo)
                        arquivos_renomeados += 1
                    else:
                        arquivos_ignorados += 1
                else:
                    arquivos_ignorados += 1
            else:
                arquivos_ignorados += 1

    tempo_final = time.time()
    relatorio(pasta, tempo_inicial, tempo_final, arquivos_renomeados, arquivos_ignorados)


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
            quantidade = contar_itens_da_pasta(pasta)
            print(f'Quantidade de arquivos na pasta: {quantidade}')
            tamanho_quantidade = 0

        elif tipo_contagem == 1:
            quantidade = contar_itens_da_pasta(pasta)
            print(f'Quantidade de arquivos na pasta: {quantidade}')
            tamanho_quantidade = 0

        elif tipo_contagem == 2:
            # Cria uma lista apenas com os arquivos (exclui subpastas)
            quantidade = contar_itens_da_pasta(pasta)
            print(f'Quantidade de arquivos na pasta: {quantidade}')
            tamanho_quantidade = len(str(quantidade))

        conf = confirmacao()
        if conf == 'S':
            break
    tempo_inicial = time.time()
    arquivos_renomeados = 0
    arquivos_ignorados = 0
    indice = 0
    if opc == 1:  # Início
        arquivos = list(os.scandir(pasta))
        for entrada in arquivos:
            if not entrada.is_file():
                continue
            indice += 1
            indice_formatado = f"{indice:0{int(tamanho_quantidade)}d}"
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            novo_nome = antes + indice_formatado + depois + nome_arquivo
            nome_novo = os.path.join(pasta, novo_nome)
            os.rename(nome_antigo, nome_novo)
            arquivos_renomeados += 1

    elif opc == 2:  # Final
        for entrada in os.scandir(pasta):
            if not entrada.is_file():
                continue
            indice += 1
            indice_formatado = f"{indice:0{int(tamanho_quantidade)}d}"
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            nome_base, extensao = os.path.splitext(nome_arquivo)
            novo_nome = nome_base + antes + indice_formatado + depois + extensao
            nome_novo = os.path.join(pasta, novo_nome)
            os.rename(nome_antigo, nome_novo)
            arquivos_renomeados += 1

    elif opc == 3:  # Ocorrencia de uma caractere
        for entrada in os.scandir(pasta):
            if not entrada.is_file():
                continue
            nome_arquivo = entrada.name
            nome_antigo = entrada.path
            indice += 1
            indice_formatado = f"{indice:0{int(tamanho_quantidade)}d}"
            nome_base, extensao = os.path.splitext(nome_arquivo)
            posicao = nome_base.find(buscar)
            if posicao != -1:
                novo_base = (nome_base[:posicao + 1] + antes + indice_formatado + depois + nome_base[posicao + 1:])
                nome_novo = os.path.join(pasta, novo_base + extensao)
                os.rename(nome_antigo, nome_novo)
                arquivos_renomeados += 1
            else:
                arquivos_ignorados += 1
    tempo_final = time.time()
    relatorio(pasta, tempo_inicial, tempo_final, arquivos_renomeados, arquivos_ignorados)


def listar_todos_os_arquivos(pasta):
    arquivos = list(os.scandir(pasta))
    for entrada in arquivos:
        print(entrada.name)
    print()
    print('\033[33mRetornando ao menu principal...\033[m')
    time.sleep(1)


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

# Adicionar:
# feito apagar entre
# feito reestruturação do código para evitar outros problemas
# feito corrigir função 2 e 3, apagando ponto da extensão
# feito buscar de uma lista e não ficar fazendo consultas diretas no Disco
# fazer def para todas as funções para reduzir a quantidade de linhas de codigo
# Arrumar o enumerar
# feito adicionar verificação no inverter,
# feito listar arquivos para aparecer o nome direito
# criar função de desfazer
#retornar ao menu
#relatorio de tempo total
#remover mais de 1 espec de 1 vez
#tentar reduzir o codigo
#retestar todas as funções