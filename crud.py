import os
os.system('cls')

biblioteca = {}
categorias = []
gastosvalores = []

def adicionar():
    nome = input("Insira o nome do livro que você deseja adicionar: ")
    biblioteca[nome] = []
    autor = input("Agora insira as informações do livro abaixo, começando pelo autor do livro: ")
    genero = input("Gênero: ")
    dinheiro = input("Preço: ")
    nota = int(input("Nota pessoal (0 a 5, digite 6 se for um livro que você não leu ainda): "))

    biblioteca[nome].append(autor)
    biblioteca[nome].append(genero)
    biblioteca[nome].append(dinheiro)
    if nota >= 0 and nota <= 5:
        biblioteca[nome].append(nota)
    elif nota == 6:
        biblioteca[nome].append("Não avaliado")
    categorias.append(genero)
    gastosvalores.append(dinheiro)
    
    return biblioteca

def editar(livro):
    opcao = int(input(f"✏️  Você está na Área de Edição\n{biblioteca}\n[1] Alterar nome\n[2] Alterar autor\n[3] Alterar categoria\n[4] Alterar valor\n[5] Voltar\nDigite o número correspondente: "))

    if opcao == 1:
       novo_nome = input()
       biblioteca[novo_nome] = biblioteca.pop(livro, "Valor não encontrado")

    elif opcao == 2:
        autor = input("Qual é o nome do autor livro? ")
        biblioteca[livro][0] = autor

    elif opcao == 3:
         
        categoria = input("Qual é a categoria do livro? ")
        
        biblioteca[livro][1] = categoria

    elif opcao == 4: 
        gasto = float(input("Qual é o gasto do livro? "))
        biblioteca[livro][2] = gasto

    elif opcao == 5:
        menu()

def visualizar_livros():
  print(biblioteca)

def visualizar_livro(livro):
  livro = biblioteca.get(livro, 'Livro não encontrado')
  print(livro)

def excluir():
  visualizar_livros()
  livro = int(input("Digite o nome do livro que deseja excluir: "))
  print(biblioteca.pop(livro, 'Livro não encontrado'))

def filtrar_categoria(categoria):
  for livro in biblioteca.items():
    if categoria in livro[1]:
      print(livro[1])

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
    saida = menu()
    if saida == 5:
        break