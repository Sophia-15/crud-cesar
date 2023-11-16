import os
import time

biblioteca = {'Teste':['Teste', 'Ação', 15.90, 3], 'Teste2':['Teste2', 'Fantasia Ação', 32.90, 4]}
categorias = ['Ação', 'Fantasia', 'Mistério', 'Suspense', 'Ficção Científica', 'Romance', 'Comédia', 'Mangá', 'HQ', 'Terror']
gastosvalores = []

def selecionar_livro(livro_selecionado, livros_categoria = []):
    livros = []

    livro_selecionado -= 1

    if len(livros_categoria) > 0 and livro_selecionado + 1 != 0 and livro_selecionado > 0:
        return livros_categoria[livro_selecionado]

    for livro in biblioteca.keys():
        livros.append(livro)
    
    if (livro_selecionado) < len(livros) and livro_selecionado >= 0 and livro_selecionado + 1 != 0:
        return livros[livro_selecionado]
    else:
        return 'vazio'

def selecionar_categoria(categoria_selecionada):
    categoria_selecionada -= 1

    return categorias[categoria_selecionada]

def listar_livros():
    livros = []
    for i in biblioteca.keys():
        livros.append(i)
    if livros == []:
        print('Você ainda não possui livros')
        return 'vazio'
    else:
        for i in range(len(livros)):
            print(f"{i + 1}. {livros[i]}")

def listar_categorias():
    for i in range(len(categorias)):
        print(f"{i + 1}. {categorias[i]}")

def adicionar():
    while True:
        try:        
            os.system('clear')
            opcao = int(input(f"📖 Você está cadastrando um novo livro\n\n[1] Continuar\n[2] Voltar\n\nDigite o número correspondente: "))
            if opcao == 1:
                os.system('clear')
                print('📖 Você está cadastrando um novo livro')
                print()
                nome = input("Digite o nome do livro que você deseja adicionar: ")
                os.system('clear')
                print('📖 Você está cadastrando um novo livro')
                print()
                autor = input("Digite o nome do autor: ")
                os.system('clear')
                print('📖 Você está cadastrando um novo livro')
                print()
                print(f"Todas as categorias:")
                listar_categorias()
                print()
                genero = input(f"(Se a categoria que você digitar não existir, uma nova será criada)\n\nDigite a(s) categoria(s) do seu livro separadas por vírgulas e espaços: ").title()
                generoLista = genero.split(', ')
                while True:
                    try:
                        os.system('clear')
                        print('📖 Você está cadastrando um novo livro')
                        print()
                        dinheiro = float(input("Digite o preço: "))
                        break
                    except:
                        print('❌ Código inválido!')
                        time.sleep(1)
                while True:
                    try:
                        os.system('clear')
                        print('📖 Você está cadastrando um novo livro')
                        print()
                        nota = float(input("Digite a sua nota pessoal de 0 a 5 (Digite 6 se ainda não leu): "))
                        break
                    except:
                        print('❌ Código inválido!')
                        time.sleep(1)
                
                biblioteca[nome] = []
                biblioteca[nome].append(autor)
                biblioteca[nome].append(generoLista)
                biblioteca[nome].append(dinheiro)

                arquivo = open(f"usuarios/{name}.csv", "a+")
                arquivo.write(f"{nome}, {autor}, {generoLista}, {dinheiro}")

                if nota >= 0 and nota <= 5:
                    biblioteca[nome].append(emojiNota(nota))
                    arquivo.write(f", {emojiNota(nota)}\n")
                elif nota == 6:
                    biblioteca[nome].append("Não avaliado")
                    arquivo.write(f", Não avaliado\n")

                arquivo.close()
                
                for j in range(len(generoLista)):         
                    if not generoLista[j] in categorias:
                        if generoLista[j] != 'Hq':
                            categorias.append(generoLista[j])

                gastosvalores.append(dinheiro)

                os.system('clear')
                print('📖 Você está cadastrando um novo livro')
                print()
                print('✅ Livro cadastrado com sucesso!')
                time.sleep(1)
                adicionar()
            elif opcao == 2:
                menu()
                break
            else:
                print('❌ Código inválido!')
                time.sleep(1)
        except:
            print('❌ Código inválido!')
            time.sleep(1)

def editar():
    while True:   
        try:
            os.system('clear')
            opcao = int(input(f"✏️  Você está na Área de Edição\n\n[1] Alterar nome\n[2] Alterar autor\n[3] Alterar categoria\n[4] Alterar valor\n[5] Alterar nota\n[6] Voltar\n\nDigite o número correspondente: "))

            if opcao == 1:
                while True:        
                    try:    
                        os.system('clear')
                        print('✏️  Você está na Área de Edição de nomes\n')
                        if listar_livros() != 'vazio':
                            livro_indice = int(input("\nDigite o número do livro que deseja editar: "))
                            if selecionar_livro(livro_indice) != 'vazio':
                                os.system('clear')
                                print('✏️  Você está na Área de Edição de nomes\n')
                                print(f'Nome atual: {selecionar_livro(livro_indice)}')
                                novo_nome = input('\nDigite o novo nome do livro: ')
                                biblioteca[novo_nome] = biblioteca.pop(selecionar_livro(livro_indice), "Valor não encontrado")
                                print('✅ Alterado com sucesso!')
                                time.sleep(1)
                                editar()
                            else:
                                print('❌ Código inválido!')
                                time.sleep(1)
                        else:
                            acao2 = int(input('Digite [1] para voltar: '))
                            if acao2 == 1:
                                menu()
                            else:
                                print('❌ Código inválido!')
                                time.sleep(1)
                    except:
                        print('❌ Código inválido!')
                        time.sleep(1)

            elif opcao == 2:
                while True:        
                    try:    
                        os.system('clear')
                        print('✏️  Você está na Área de Edição de autores\n')
                        if listar_livros() != 'vazio':
                            livro_indice = int(input("\nDigite o número do livro que deseja editar: "))
                            if selecionar_livro(livro_indice) != 'vazio':
                                os.system('clear')
                                print('✏️  Você está na Área de Edição de autores\n')
                                print(f'Autor atual: {biblioteca[selecionar_livro(livro_indice)][0]}')
                                autor = input("\nDigite o novo autor do livro: ")
                                biblioteca[selecionar_livro(livro_indice)][0] = autor
                                print('✅ Alterado com sucesso!')
                                time.sleep(1)
                                editar()
                            else:
                                print('❌ Código inválido!')
                                time.sleep(1)
                        else:
                            acao2 = int(input('Digite [1] para voltar: '))
                            if acao2 == 1:
                                menu()
                            else:
                                print('❌ Código inválido!')
                                time.sleep(1)
                    except:
                        print('❌ Código inválido!')
                        time.sleep(1)

            elif opcao == 3:
                while True:
                    try:    
                        os.system('clear')
                        print('✏️  Você está na Área de Edição de categorias\n')
                        if listar_livros() != 'vazio':
                            livro_indice = int(input("\nDigite o número do livro que deseja editar: "))
                            if selecionar_livro(livro_indice) != 'vazio':
                                os.system('clear')
                                print('✏️  Você está na Área de Edição de categorias\n')
                                print("Todas as categorias: ")
                                listar_categorias()
                                livro_encontrado = biblioteca.get(selecionar_livro(livro_indice), 'Livro não encontrado')
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
                                print(f'\nCategorias atuais: {strCategorias}')
                                categoria = input("\nDigite as categorias atualizadas do livro separadas por vírgulas e espaços: ").title()
                                categoriaLista = categoria.split(', ')
                                for j in range(len(categoriaLista)):
                                    if not categoriaLista[j] in categorias:
                                        categorias.append(categoriaLista[j])
                                        
                                biblioteca[selecionar_livro(livro_indice)][1] = categoria
                                print('✅ Alterado com sucesso!')
                                time.sleep(1)
                                editar()
                            else:
                                print('❌ Código inválido!')
                                time.sleep(1)
                        else:
                            acao2 = int(input('Digite [1] para voltar: '))
                            if acao2 == 1:
                                menu()
                            else:
                                print('❌ Código inválido!')
                                time.sleep(1)
                    except:
                        print('❌ Código inválido!')
                        time.sleep(1)

            elif opcao == 4: 
                while True:
                    try:
                        os.system('clear')
                        print('✏️  Você está na Área de Edição de valores\n')
                        if listar_livros() != 'vazio':
                            livro_indice = int(input("\nDigite o número do livro que deseja editar: "))
                            if selecionar_livro(livro_indice) != 'vazio':
                                while True:
                                    try:   
                                        os.system('clear')
                                        print('✏️  Você está na Área de Edição de valores')
                                        print(f'\nValor atual do livro: R${biblioteca[selecionar_livro(livro_indice)][2]:.2f}')
                                        valor = float(input("\nDigite o novo valor do livro: "))
                                        biblioteca[selecionar_livro(livro_indice)][2] = valor
                                        print('✅ Alterado com sucesso!')
                                        time.sleep(1)
                                        editar()
                                        break
                                    except:
                                        print('❌ Código inválido!')
                                        time.sleep(1)
                            else:
                                print('❌ Código inválido!')
                                time.sleep(1)
                        else:
                            acao2 = int(input('Digite [1] para voltar: '))
                            if acao2 == 1:
                                menu()
                            else:
                                print('❌ Código inválido!')
                                time.sleep(1)
                    except:
                        print('❌ Código inválido!')
                        time.sleep(1)

            elif opcao == 5: 
                while True:
                    try:
                        os.system('clear')
                        print('✏️  Você está na Área de Edição de notas\n')
                        if listar_livros() != 'vazio':
                            livro_indice = int(input("\nDigite o número do livro que deseja editar: "))
                            if selecionar_livro(livro_indice) != 'vazio':
                                while True:
                                    try:
                                        os.system('clear')
                                        print('✏️  Você está na Área de Edição de notas\n')
                                        print(f'Nota atual do livro: {biblioteca[selecionar_livro(livro_indice)][3]}')
                                        nota = float(input("\nDigite a nova nota do livro: "))
                                        if nota >= 0 and nota <= 5:
                                            biblioteca[selecionar_livro(livro_indice)][3] = (emojiNota(nota)) 
                                            print('✅ Alterado com sucesso!')
                                            time.sleep(1)
                                            editar()
                                            break
                                        elif nota == 6:
                                            biblioteca[selecionar_livro(livro_indice)][3] = ("Não avaliado")
                                            print('✅ Alterado com sucesso!')
                                            time.sleep(1)
                                            editar()
                                            break
                                        else:
                                            print('❌ Código inválido!')
                                            time.sleep(1)
                                    except:
                                        print('❌ Código inválido!')
                                        time.sleep(1)
                        else:
                            acao2 = int(input('Digite [1] para voltar: '))
                            if acao2 == 1:
                                menu()
                            else:
                                print('❌ Código inválido!')
                                time.sleep(1)
                    except:
                        print('❌ Código inválido!')
                        time.sleep(1)
            
            elif opcao == 6:
                menu()
            
            else:
                print('❌ Código inválido!')
                time.sleep(1)
        
        except:
            print('❌ Código inválido!')
            time.sleep(1)

def visualizar_livros():
    os.system('clear')
    try:
        opcao = int(input('👓 Você está na área de visualização\n\n[1] Visualizar livros\n[2] Visualizar por categoria\n[3] Visualizar gastos\n[4] Voltar\n\nDigite o número correspondente: '))
        
        if opcao == 1:
            while True:
                os.system('clear')
                print('👓 Você está na área de visualização de livros')
                Vazio = listar_livros()
                try:    
                    if Vazio != 'vazio':
                        livro_indice = int(input("\nDigite o número do livro que deseja visualizar: "))
                        if livro_indice != 0:
                            livro = selecionar_livro(livro_indice)
                            os.system('clear')
                            print('👓 Você está na área de visualização de livro')
                            print()
                            visualizar_livro(livro)
                            print("")
                            opcao2 = int(input('Digite [1] para voltar: '))
                            if opcao2 == 1:
                                visualizar_livros()
                                break
                        else:
                            print('❌ Código inválido!')
                            time.sleep(1)
                    else:
                        sair = int(input('Digite [1] para voltar: '))
                        if sair == 1:
                            visualizar_livros()
                            break
                        else:
                            sair += 'erro'
                except:
                    print('❌ Código inválido!')
                    time.sleep(1)
        
        elif opcao == 2:
            while True:
                os.system('clear')
                print('👓 Você está na área de visualização por categoria')
                print()
                listar_categorias()
                print()
                try:
                    categoria_indice = int(input("Digite o número da categoria que você deseja filtrar por: "))
                    categoria = selecionar_categoria(categoria_indice)
                    while True:
                        try:    
                            os.system('clear')
                            print(f'👓 Você está visualizando a categoria: {categoria}')
                            Vazio = filtrar_categoria(categoria)
                            if Vazio != 'vazio': 
                                opcao2 = int(input('\n[1] Visualizar livro \n[2] Voltar\n\nDigite o número correspondente: '))
                            else:
                                sair = int(input('Digite [1] para voltar: '))
                                if sair == 1:
                                    visualizar_livros()
                                    break
                                else:
                                    sair += 'erro'
                            if opcao2 == 1:
                                while True:
                                    try:    
                                        os.system('clear')
                                        print(f'👓 Você está visualizando a categoria: {categoria}')
                                        print()
                                        livros_categoria = filtrar_categoria(categoria)
                                        print()
                                        livro_indice = int(input("Digite o número do livro que deseja visualizar: "))
                                        livro = selecionar_livro(livro_indice, livros_categoria)
                                        os.system('clear')
                                        print('👓 Você está na área de visualização de livro')
                                        print()
                                        visualizar_livro(livro[0] if type(livro) == list else livro)
                                        print()
                                        opcao2 = int(input('Digite [1] para voltar: '))

                                        if opcao2 == 1:
                                            visualizar_livros()
                                            break
                                    except:
                                        print('❌ Código inválido!')
                                        time.sleep(1)
                            elif opcao2 == 2:
                                visualizar_livros()
                                break
                            else:
                                print('❌ Código inválido!')
                                time.sleep(1)
                        except:
                            print('❌ Código inválido!')
                            time.sleep(1)
                except:
                    print('❌ Código inválido!')
                    time.sleep(1)
        
        elif opcao == 3:
            while True:
                try:    
                    os.system('clear')
                    print('👓 Você está na área de visualização de gastos')
                    print()
                    print(f'💸 Gasto total: R${sum(gastosvalores):.2f}\n')
                    livros = []
                    for i in biblioteca.keys():
                        livros.append(i)
                    for i in range(len(livros)):
                        print(f"{i + 1}. {livros[i]} - R${biblioteca[livros[i]][2]:.2f}")
                    print()
                    opcao2 = int(input('Digite [1] para voltar: '))
                    if opcao2 == 1:
                        visualizar_livros()
                        break
                    else:
                        print('❌ Código inválido!')
                        time.sleep(1)
                except:
                    print('❌ Código inválido!')
                    time.sleep(1)
        elif opcao == 4:
            menu()
        else:
            opcao += 'erro'
    except:
        print('❌ Código inválido!')
        time.sleep(1)
        visualizar_livros()

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
    while True:
        try:
            os.system('clear')   
            opcao = int(input('🗑️  Você está excluindo um livro\n\n[1] Continuar\n[2] Voltar\n\nDigite o número correspondente: '))
            if opcao == 1:
                while True:
                    try:
                        os.system('clear')
                        print('🗑️  Você está excluindo um livro\n')
                        if listar_livros() != 'vazio':
                            livro_indice = int(input("\nDigite o número do livro que deseja excluir: "))
                            if selecionar_livro(livro_indice) != 'vazio':
                                livro = selecionar_livro(livro_indice)
                                biblioteca.pop(livro, 'Livro não encontrado')
                                print('✅ Livro excluído com sucesso!')
                                time.sleep(1)
                                excluir()
                                break
                            else:
                                print('❌ Código inválido!')
                                time.sleep(1)
                        else:
                            while True:
                                    os.system('clear')
                                    print('🗑️  Você está excluindo um livro')
                                    listar_livros()
                                    opcao2 = int(input('Digite [1] para voltar: '))
                                    if opcao2 == 1:
                                        menu()
                                        break
                                    else:
                                        print('❌ Código inválido!')
                                        time.sleep(1)
                    except:
                        print('❌ Código inválido!')
                        time.sleep(1)
            elif opcao == 2:
                menu()
            else:
                opcao += 'erro'
        except:
            print('❌ Código inválido!')
            time.sleep(1)

def filtrar_categoria(categoria):    
    livros = []
    for livro in biblioteca.items():
        if categoria in livro[1][1]:
            livros.append(livro[0])
    if livros == []:
        print()
        print('Você ainda não possui livros nessa categoria')
        print()
        return 'vazio'
    for i in range(len(livros)):
        print(f"{i + 1}. {livros[i]}")

    return livros

def menu():
    pasta_usuarios = './usuarios'
    if not os.path.isdir(pasta_usuarios):
        os.mkdir(pasta_usuarios)
    arquivo = open(f'usuarios/{name}.csv', 'a')
    arquivo.close()
    os.system('clear')
    print(f"📚 Olá {name}! Bem-vindo(a) ao Sistema de Gerenciamento de Leitura (SGL)")
    print()
    acao = int(input("[1] Visualizar a sua lista de livros\n[2] Adicionar um novo livro\n[3] Editar as informações de um livro\n[4] Excluir um livro\n[5] Sair\n\nDigite o número correspondente: "))
    
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
        print('❌ Código inválido!')
        time.sleep(1)

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

os.system('clear')
name = input('Digite o seu nome: ')
acao = 0
while acao != 5:
    try:
        acao = menu()
    except:
        print('❌ Código inválido!')
        time.sleep(1)