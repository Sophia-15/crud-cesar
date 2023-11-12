import os
import time

biblioteca = {}
categorias = ['Ação', 'Fantasia', 'Mistério', 'Suspense', 'Ficção Científica', 'Romance', 'Comédia', 'Mangá', 'HQ', 'Terror']
gastosvalores = []


def selecionar_livro(livro_selecionado):
    livros = []
    livro_selecionado -= 1

    for livro in biblioteca.keys():
        livros.append(livro)
    
    return livros[livro_selecionado]

def selecionar_categoria(categoria_selecionada):
    categoria_selecionada -= 1

    return categorias[categoria_selecionada]

    
def listar_livros():
    livros = []
    for i in biblioteca.keys():
        livros.append(i)

    for i in range(len(livros)):
        print(f"{i + 1}. {livros[i]}")

def listar_categorias():
    for i in range(len(categorias)):
        print(f"{i + 1}. {categorias[i]}")

def adicionar():
    os.system('cls')
    opcao = int(input(f"📖 Você está cadastrando um novo livro\n[1] Continuar\n[2] Voltar\nDigite o número correspondente: "))
    if opcao == 1:
        os.system('cls')
        print('📖 Você está cadastrando um novo livro')

        nome = input("Digite o nome do livro que você deseja adicionar: ")
        autor = input("Digite o nome do autor: ")
        print(f"Todas as categorias:")
        listar_categorias()
        genero = input(f"Digite a(s) categoria(s) do seu livro separados por espaços: ").title()
        generoLista = genero.split()
        dinheiro = float(input("Digite o preço: "))
        nota = float(input("Digite a sua nota pessoal de 0 a 5 (Digite 6 se ainda não leu): "))

        biblioteca[nome] = []
        biblioteca[nome].append(autor)
        biblioteca[nome].append(generoLista)
        biblioteca[nome].append(dinheiro)

        if nota >= 0 and nota <= 5:
            biblioteca[nome].append(emojiNota(nota))
        elif nota == 6:
            biblioteca[nome].append("Não avaliado")
        
        for j in range(len(generoLista)):         
            if not generoLista[j] in categorias:
                if generoLista[j] != 'Hq':
                    categorias.append(generoLista[j])

        gastosvalores.append(dinheiro)

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
        os.system('cls')
        print('✏️  Você está na Área de Edição')
        listar_livros()
        livro_indice = int(input("Digite o número do livro que deseja editar: "))
        livro = selecionar_livro(livro_indice)
        novo_nome = input('Digite o novo nome do livro: ')
        biblioteca[novo_nome] = biblioteca.pop(livro, "Valor não encontrado")
        print('✅ Alterado com sucesso!')
        time.sleep(1)
        editar()

    elif opcao == 2:
        os.system('cls')
        print('✏️  Você está na Área de Edição')
        listar_livros()
        livro_indice = int(input("Digite o número do livro que deseja editar: "))
        livro = selecionar_livro(livro_indice)
        autor = input("Digite o novo autor do livro: ")
        biblioteca[livro][0] = autor
        print('✅ Alterado com sucesso!')
        time.sleep(1)
        editar()

    elif opcao == 3:
        os.system('cls')
        print('✏️  Você está na Área de Edição')
        listar_livros()
        livro_indice = int(input("Digite o número do livro que deseja editar: "))
        livro = selecionar_livro(livro_indice)
        os.system('cls')
        print('✏️  Você está na Área de Edição')
        print("Todas as categorias: ")
        listar_categorias()
        livro_encontrado = biblioteca.get(livro, 'Livro não encontrado')
        strCategorias = ''
        contVirgula = 1
        if type(livro_encontrado[1]) == list:
            for i in livro_encontrado[1]:
                if contVirgula == len(livro_encontrado[1]):
                    strCategorias += (f'{i}')
                else:
                    strCategorias += (f'{i}, ')
                    contVirgula+=1
        else:
            strCategorias = livro_encontrado[1] 
        print(f'Categorias atuais: {strCategorias}')
        categoria = input("Digite as categorias atualizadas do livro:  ").title()
        categoriaLista = categoria.split()
        for j in range(len(categoriaLista)):
            if not categoriaLista[j] in categorias:
                categorias.append(categoriaLista[j])
                
        biblioteca[livro][1] = categoria
        print('✅ Alterado com sucesso!')
        time.sleep(1)
        editar()

    elif opcao == 4: 
        os.system('cls')
        print('✏️  Você está na Área de Edição')
        listar_livros()
        livro_indice = int(input("Digite o número do livro que deseja editar: "))
        livro = selecionar_livro(livro_indice)
        print(f'Valor atual do livro: R${biblioteca[livro][2]}')
        valor = float(input("Digite o novo valor do livro: "))
        biblioteca[livro][2] = valor
        print('✅ Alterado com sucesso!')
        time.sleep(1)
        editar()

    elif opcao == 5: 
        os.system('cls')
        print('✏️  Você está na Área de Edição')
        listar_livros()
        livro_indice = int(input("Digite o número do livro que deseja editar: "))
        livro = selecionar_livro(livro_indice)
        print(f'Nota atual do livro: {biblioteca[livro][3]}')
        nota = float(input("Digite a nova nota do livro: "))
        if nota >= 0 and nota <= 5:
            biblioteca[livro][3] = (emojiNota(nota)) 
        elif nota == 6:
            biblioteca[livro][3] = ("Não avaliado")
        print('✅ Alterado com sucesso!')
        time.sleep(1)
        editar()
    
    elif opcao == 6:
        menu()


def visualizar_livros():
    os.system('cls')
    opcao = int(input('👓 Você está na área de visualização\n[1] Visualizar livros\n[2] Visualizar por categoria\n[3] Visualizar gastos\n[4] Voltar\nDigite o número correspondente: '))

    if opcao == 1:
        os.system('cls')
        print('👓 Você está na área de visualização')
        listar_livros()
        livro_indice = int(input("Digite o número do livro que deseja visualizar: "))
        livro = selecionar_livro(livro_indice)
        os.system('cls')
        print('👓 Você está na área de visualização')
        print()
        visualizar_livro(livro)
        print("")
        opcao2 = int(input('Digite [1] para voltar: '))

        if opcao2 == 1:
            visualizar_livros()
    elif opcao == 2:
        os.system('cls')
        print('👓 Você está na área de visualização por categoria')
        print()
        listar_categorias()
        print()
        categoria_indice = int(input("Digite o número da categoria que você deseja filtrar por: "))
        categoria = selecionar_categoria(categoria_indice)
        os.system('cls')
        print(f'👓 Você está visualizando a categoria: {categoria}')
        print()
        filtrar_categoria(categoria)
        print()
        opcao2 = int(input('[1] Visualizar livro \n[2] Voltar\nDigite o número correspondente: '))

        if opcao2 == 1:
            os.system('cls')
            print(f'👓 Você está visualizando a categoria: {categoria}')
            print()
            filtrar_categoria(categoria)
            print()
            livro_indice = int(input("Digite o número do livro que deseja visualizar: "))
            livro = selecionar_livro(livro_indice)
            os.system('cls')
            print('👓 Você está na área de visualização')
            print()
            visualizar_livro(livro)
            print()
            opcao2 = int(input('Digite [1] para voltar: '))

            if opcao2 == 1:
                visualizar_livros()

        if opcao2 == 2:
            visualizar_livros()
    elif opcao == 3:
        os.system('cls')
        print('👓 Você está na área de visualização')
        print()
        print(f'Gasto total: R${sum(gastosvalores):.2f}')
        livros = []
        for i in biblioteca.keys():
            livros.append(i)

        for i in range(len(livros)):
            print(f"{i + 1}. {livros[i]} - R${biblioteca[livros[i]][2]:.2f}")
        print()
        opcao2 = int(input('Digite [1] para voltar: '))
        if opcao2 == 1:
            visualizar_livros() 
    elif opcao == 4:
        menu()

def visualizar_livro(livro):
    livro_encontrado = biblioteca.get(livro, 'Livro não encontrado')
    strCategorias = ''
    contVirgula = 1
    if type(livro_encontrado[1]) == list:
        for i in livro_encontrado[1]:
            if contVirgula == len(livro_encontrado[1]):
                strCategorias += (f'{i}')
            else:
                strCategorias += (f'{i}, ')
                contVirgula+=1
    else:
        strCategorias = livro_encontrado[1]

    print(f"Nome: {livro} \nAutor: {livro_encontrado[0]} \nCategorias: {strCategorias} \nPreço: R${float(livro_encontrado[2]):.2f} \nNota: {(livro_encontrado[3])}")


def excluir():
    os.system('cls')
    opcao = int(input('🗑️  Você está excluindo um livro\n[1] Continuar\n[2] Voltar\nDigite o número correspondente: '))
    if opcao == 1:
        os.system('cls')
        print('🗑️  Você está excluindo um livro')
        listar_livros()
        
        livro_indice = int(input("Digite o número do livro que deseja excluir: "))
        livro = selecionar_livro(livro_indice)
        biblioteca.pop(livro, 'Livro não encontrado')
        
        print('✅ Livro excluído com sucesso!')
        time.sleep(1)
        excluir()
    elif opcao == 2:
        menu()

def filtrar_categoria(categoria):    
    livros = []
    for livro in biblioteca.items():
        if categoria in livro[1][1]:
            livros.append(livro[0])

    for i in range(len(livros)):
        print(f"{i + 1}. {livros[i]}")

    return livros

def menu():
    os.system('cls')
    print(f"📚 Olá {name}! Bem-vindo(a) ao Sistema de Gerenciamento de Leitura (SGL)")
    acao = int(input("[1] Visualizar a sua lista de livros\n[2] Adicionar um novo livro\n[3] Editar as informações de um livro\n[4] Excluir um livro\n[5] Sair\nDigite o número correspondente: "))
    
    if acao == 1:
        os.system('cls')
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
    elif nota == 1 or nota < 1.5:
        return f'🌕🌚🌚🌚🌚'
    elif 2 > nota >= 1.5:
        return f'🌕🌗🌚🌚🌚'
    elif nota == 2 or nota < 2.5:
        return f'🌕🌕🌚🌚🌚'
    elif 3 > nota >= 2.5:
        return f'🌕🌕🌗🌚🌚'
    elif nota == 3 or nota < 3.5:
        return f'🌕🌕🌕🌚🌚'
    elif 4 > nota >= 3.5:
        return f'🌕🌕🌕🌗🌚'
    elif nota == 4 or nota < 4.5:
        return f'🌕🌕🌕🌕🌚'
    elif 5 > nota >= 4.5:
        return f'🌕🌕🌕🌕🌗'
    elif nota == 5:
        return f'🌕🌕🌕🌕🌕'

os.system('cls')
name = input('Digite o seu nome: ')
acao = 0
while acao != 5:
    acao = menu()
