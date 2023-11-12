import os
import time

biblioteca = {}
categorias = ['Ação', 'Fantasia', 'Mistério', 'Suspense', 'Ficção Científica', 'Romance', 'Comédia', 'Mangá', 'HQ', 'Terror']
gastosvalores = []

def listar_categorias():
    for i in range(len(categorias)):
        print(f"{i + 1} - {categorias[i]}")

def adicionar():
    os.system('clear')
    opcao = int(input(f"📖 Você está cadastrando um novo livro\n[1] Continuar\n[2] Voltar\nDigite o número correspondente: "))
    if opcao == 1:
        os.system('clear')
        print('📖 Você está cadastrando um novo livro')

        nome = input("Digite o nome do livro que você deseja adicionar: ")
        autor = input("Digite o nome do autor: ")
        print(f"Todas as categorias:")
        listar_categorias()
        genero = input(f"Digite o(s) gênero(s) do seu livro separados por espaços: ")
        generoLista = genero.split()
        dinheiro = float(input("Digite o preço: "))
        nota = float(input("Digite a sua nota pessoal de 0 a 5 (Digite 6 se ainda não leu): "))

        biblioteca[nome] = []
        biblioteca[nome].append(autor)

        for i in range(len(generoLista)):
            biblioteca[nome].append(generoLista[i])
        biblioteca[nome].append(dinheiro)

        if nota >= 0 and nota <= 5:
            biblioteca[nome].append(emojiNota(nota))
        elif nota == 6:
            biblioteca[nome].append("Não avaliado")
        
        if not genero in categorias:
            for j in range(len(generoLista)):            
                categorias.append(generoLista[j])
        gastosvalores.append(dinheiro)

        print(biblioteca)
        
        print('✅ Livro cadastrado com sucesso!')
        time.sleep(1)
        adicionar()
    else:
        menu()

def editar():
    os.system('cls')
    opcao = int(input(f"✏️  Você está na Área de Edição\n[1] Alterar nome\n[2] Alterar autor\n[3] Alterar categoria\n[4] Alterar valor\n[5] Alterar nota\n[6] Voltar\nDigite o número correspondente: "))

    cont = 0
    if opcao == 1:
        os.system('clear')
        print('✏️  Você está na Área de Edição')
        print(biblioteca)
        visualizar_livros()
        livro = input('Digite o nome do livro: ')
        novo_nome = input('Digite o novo nome do livro: ')
        biblioteca[novo_nome] = biblioteca.pop(livro, "Valor não encontrado")
        print('✅ Alterado com sucesso!')
        time.sleep(1)
        editar()

    elif opcao == 2:
        os.system('clear')
        print('✏️  Você está na Área de Edição')
        visualizar_livros()
        livro = input('Digite o nome do livro: ')
        autor = input("Digite o novo autor do livro: ")
        biblioteca[livro][0] = autor
        print('✅ Alterado com sucesso!')
        time.sleep(1)
        editar()

    elif opcao == 3:
        os.system('clear')
        print('✏️  Você está na Área de Edição')
        visualizar_livros()
        livro = input('Digite o nome do livro: ')
        os.system('cls')
        print('✏️  Você está na Área de Edição')
        print("Todas as categorias: ", end = ' ')
        for cate in categorias:
            cont+=1
            if cont == len(categorias):
                print(cate)
            else:
                 print(cate, end = ', ')  
        print("Categorias atuais do livro : ",biblioteca[livro][1])
        categoria = input("Digite as categorias atualizadas do livro:  ")
        biblioteca[livro][1] = categoria
        print('✅ Alterado com sucesso!')
        time.sleep(1)
        editar()

    elif opcao == 4: 
        os.system('clear')
        print('✏️  Você está na Área de Edição')
        visualizar_livros()
        livro = input('Digite o nome do livro: ')
        valor = float(input("Digite o novo valor do livro: "))
        biblioteca[livro][2] = valor
        print('✅ Alterado com sucesso!')
        time.sleep(1)
        editar()

    elif opcao == 5: 
        os.system('cls')
        print('✏️  Você está na Área de Edição')
        visualizar_livros()
        livro = input('Digite o nome do livro: ')
        nota = int(input("Digite a nova nota do livro: "))
        if nota >= 0 and nota <= 5:
           biblioteca[livro][3] = (emojiNota(nota)) 
        elif nota == 6:
            biblioteca[livro][3] = ("Não avaliado")
        print('✅ Alterado com sucesso!')
        time.sleep(1)
        editar()
    
    elif opcao == 6:
        menu()

def listar_livros():
    livros = []
    for i in biblioteca.keys():
        livros.append(i)

    for i in range(len(livros)):
        print(f" {i + 1} - {livros[i]}")

def visualizar_livros():
    os.system('clear')
    opcao = int(input('👓 Você está na área de visualização\n[1] Continuar\n[2] Voltar\nDigite o número correspondente: '))

    if opcao == 1:
        os.system('clear')
        print('👓 Você está na área de visualização')
        listar_livros()
        livro = input("Digite o nome do livro que deseja visualizar: ")
        os.system('clear')
        print('👓 Você está na área de visualização')
        visualizar_livro(livro)
        print("")
        opcao = int(input('Digite [1] para voltar: '))

        if opcao == 1:
            visualizar_livros()
    elif opcao == 2:
        menu()

def visualizar_livro(livro):
    livro_encontrado = biblioteca.get(livro, 'Livro não encontrado')
    print(f"Nome: {livro} \nAutor: {livro_encontrado[0]} \nCategorias: {livro_encontrado[1]} \nPreço: R${float(livro_encontrado[2]):.2f} \nNota: {livro_encontrado[3]}")

def excluir():
    os.system('clear')
    opcao = int(input('🗑️  Você está excluindo um livro\n[1] Continuar\n[2] Voltar\nDigite o número correspondente: '))
    if opcao == 1:
        os.system('clear')
        print('🗑️ Você está excluindo um livro')
        listar_livros()
        
        livro = (input("Digite o nome do livro que deseja excluir: "))
        biblioteca.pop(livro, 'Livro não encontrado')
        
        print('✅ Livro excluído com sucesso!')
        time.sleep(1)
        excluir()
    elif opcao == 2:
        menu()

def filtrar_categoria(categoria):
    for livro in biblioteca.items():
        if categoria in livro[1]:
            print(livro[1])

def menu():
    os.system('clear')
    print(f"📚 Olá {name}! Bem-vinda ao Sistema de Gerenciamento de Leitura (SGL)")
    acao = int(input("[1] Visualizar a sua lista de livros\n[2] Adicionar um novo livro\n[3] Editar as informações de um livro\n[4] Excluir um livro\n[5] Sair\nDigite o número correspondente: "))
    
    if acao == 1:
        os.system('clear')
        visualizar_livros()
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
        return f'🌚🌚🌚🌚🌚'
    elif 1 > nota > 0:
        return f'🌗🌚🌚🌚🌚'
    elif nota == 1:
        return f'🌕🌚🌚🌚🌚'
    elif 2 > nota >= 1.5:
        return f'🌕🌗🌚🌚🌚'
    elif nota == 2:
        return f'🌕🌕🌚🌚🌚'
    elif 3 > nota >= 2.5:
        return f'🌕🌕🌗🌚🌚'
    elif nota == 3:
        return f'🌕🌕🌕🌚🌚'
    elif 4 > nota >= 3.5:
        return f'🌕🌕🌕🌗🌚'
    elif nota == 4:
        return f'🌕🌕🌕🌕🌚'
    elif 5 > nota >= 4.5:
        return f'🌕🌕🌕🌕🌗'
    elif nota == 5:
        return f'🌕🌕🌕🌕🌕'

os.system('clear')
name = input('Digite o seu nome: ')

while True:
    programa = menu()
    if programa == 5:
        break