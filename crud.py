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
        return f'{nota} | 🌚🌚🌚🌚🌚'
    elif 1 > nota > 0:
        return f'{nota} | 🌗🌚🌚🌚🌚'
    elif nota == 1:
        return f'{nota} | 🌕🌚🌚🌚🌚'
    elif 2 > nota >= 1.5:
        return f'{nota} | 🌕🌗🌚🌚🌚'
    elif nota == 2:
        return f'{nota} | 🌕🌕🌚🌚🌚'
    elif 3 > nota >= 2.5:
        return f'{nota} | 🌕🌕🌗🌚🌚'
    elif nota == 3:
        return f'{nota} | 🌕🌕🌕🌚🌚'
    elif 4 > nota >= 3.5:
        return f'{nota} | 🌕🌕🌕🌗🌚'
    elif nota == 4:
        return f'{nota} | 🌕🌕🌕🌕🌚'
    elif 5 > nota >= 4.5:
        return f'{nota} | 🌕🌕🌕🌕🌗'
    elif nota == 5:
        return f'{nota} | 🌕🌕🌕🌕🌕'

while True:
    menu()
    saida = menu()
    if saida == 5:
        break