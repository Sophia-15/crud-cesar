import os
os.system('cls')

biblioteca = {}

def menu():
    print(f"📚 Olá Nathália! Bem-vinda ao Sistema de Gerenciamento de Leitura (SGL)")
    acao = int(input("[1] Visualizar a sua lista de livros\n[2] Adicionar um novo livro\n[3] Editar as informações de um livro\n[4] Excluir um livro\n[5] Sair\nDigite o número correspondente: "))
    if acao == 1:
        visualizar()
    elif acao == 2:
        adicionar()
    elif acao == 3:
        editar()
    elif acao == 4:
        excluir()
    elif acao == 5:
        return 5
    else:
        print('CÓDIGO INVÁLIDO')


def emojiNota(nota):
    if nota == 0:
        return '🌚🌚🌚🌚🌚'
    elif 1 > nota > 0:
        return '🌗🌚🌚🌚🌚'
    elif nota == 1:
        return '🌕🌚🌚🌚🌚'
    elif 2 > nota > 1:
        return '🌕🌗🌚🌚🌚'
    elif nota == 2:
        return '🌕🌕🌚🌚🌚'
    elif 3 > nota > 2:
        return '🌕🌕🌗🌚🌚'
    elif nota == 3:
        return '🌕🌕🌕🌚🌚'
    elif 4 > nota > 3:
        return '🌕🌕🌕🌗🌚'
    elif nota == 4:
        return '🌕🌕🌕🌕🌚'
    elif 5 > nota > 4:
        return '🌕🌕🌕🌕🌗'
    elif nota == 5:
        return '🌕🌕🌕🌕🌕'

while True:
    menu()
    saida = menu()
    if saida == 5:
        break