# 🪨 Projeto Sísifo — Renomeador de Arquivos

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Versão](https://img.shields.io/badge/vers%C3%A3o-1.1.3-green)
![Interface](https://img.shields.io/badge/interface-terminal-lightgrey)

Script em Python, executado no terminal, que **automatiza a tarefa repetitiva de renomear arquivos em lote**. Em vez de renomear um por um, você escolhe a operação em um menu interativo e ela é aplicada a todos os arquivos da pasta informada.

> O nome é uma referência a Sísifo, da mitologia grega, condenado a repetir a mesma tarefa para sempre. Este projeto existe para que essa tarefa não seja sua. 😄

---

## 📋 Funcionalidades

| # | Opção | O que faz |
|---|-------|-----------|
| 1 | **Adição de caractere** | Insere um texto no início, no final (antes da extensão) ou após a ocorrência de um caractere |
| 2 | **Remoção de caractere** | Remove um texto/caractere específico do nome dos arquivos |
| 3 | **Substituição de texto/caractere** | Troca todas as ocorrências de um texto por outro |
| 4 | **Iniciais maiúsculas** | Transforma a inicial de cada palavra do nome em maiúscula |
| 5 | **Inverter "Título - Nome"** | Inverte a ordem das partes separadas por ` - ` |
| 6 | **Recortar nome** | Corta uma quantidade de caracteres do início ou do final, ou corta até encontrar um caractere (lendo do início ou do final) |
| 7 | **Enumerar cada arquivo** | Adiciona um índice no início, no final ou após um caractere, nos formatos `1, 2, 3…` ou `001, 002, 003…`, com texto opcional antes e depois do índice |
| 8 | **Listar arquivos da pasta** | Exibe todos os arquivos da pasta informada |
| 9 | **Sair** | Encerra o programa |

### Recursos adicionais

- ✅ **Confirmação antes de executar:** você revisa os dados informados e confirma com `S` ou `N`.
- 🛡️ **Proteção contra sobrescrita:** se o novo nome já existir, o arquivo é ignorado em vez de ser sobrescrito.
- 📊 **Relatório ao final:** mostra o tempo de execução e as quantidades de arquivos analisados, renomeados e ignorados.
- 🎨 **Interface colorida** no terminal, com tratamento de entradas inválidas e de `Ctrl+C`.

---

## ⚙️ Requisitos

- [Python 3](https://www.python.org/downloads/)
- Nenhuma biblioteca externa: usa apenas `os` e `time`, da biblioteca padrão.

---

## 🚀 Como usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/CarvalhoGuss/renomeador-de-arquivos.git
   cd renomeador-de-arquivos
   ```

2. Execute o script (ajuste o nome do arquivo, se for diferente):

   ```bash
   python renomeador.py
   ```

3. Informe o **caminho da pasta** quando solicitado. Dica: copie o endereço da barra do Explorador de Arquivos e cole **sem aspas**.

4. Escolha a opção desejada no menu, siga as instruções na tela e confirme a operação.

### Exemplo de fluxo

```text
------------------------------------------
          RENOMEADOR DE ARQUIVOS
------------------------------------------
O que deseja fazer?
1 - Adição de caractere
2 - Remoção de caractere
3 - Substituição de texto/caractere
4 - Transformar caracteres iniciais em maiúsculas
5 - Inverter "Título - Nome"
6 - Recortar nome
7 - Enumerar cada arquivo
8 - Listar todos os arquivos da pasta
9 - Sair.
------------------------------------------
Sua Opção:
```

---

## ⚠️ Avisos importantes

- A renomeação **não pode ser desfeita** pelo programa. **Faça um backup** ou teste primeiro em uma cópia da pasta.
- A operação é aplicada a **todos os itens da pasta informada**. Use o recurso de listar arquivos (opção 8) para conferir o conteúdo antes de começar.
- Os códigos de cor ANSI funcionam melhor em terminais modernos (Windows Terminal, PowerShell recente, terminais Linux/macOS).

---

## 🗂️ Estrutura do código

- **Funções de interface:** `leia_int`, `linha_menu`, `cabecalho_menu`, `menu` e `confirmacao`.
- **Funções gerais:** `contar_itens_da_pasta` e `relatorio`.
- **Funções do menu:** `adicao_de_caractere`, `remocao_de_caractere`, `substituicao_de_caractere`, `iniciais_maiusculas`, `inverter`, `recortar_nome`, `enumerar` e `listar_todos_os_arquivos`.

---

## 📝 Informações do projeto

- **Versão:** 1.1.3
- **Criação:** 04/04/2024
- **Lançamento:** 15/04/2024
- **Última modificação:** 18/08/2026

---

## 👤 Autor

**Gustavo Carvalho Brito**

- GitHub: [@CarvalhoGuss](https://github.com/CarvalhoGuss)
- LinkedIn: [gustavo-carvalho-brito](https://linkedin.com/in/gustavo-carvalho-brito)

---

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Abra uma *issue* ou envie um *pull request* no [repositório](https://github.com/CarvalhoGuss/renomeador-de-arquivos).
