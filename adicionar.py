import os
os.system("cls")

biblioteca = {}
categorias = []
gastosvalores = []

def adicionar ():
    nome = input("Insira o nome do livro que você deseja adicionar: ")
    biblioteca[nome] = []
    autor = input("Agora insira as informações do livro abaixo, começando pelo autor do livro: ")
    genero = input("Gênero: ")
    dinheiro = input("Preço: ")
    nota = input("Nota pessoal (0 a 5): ")

    biblioteca[nome].append(autor)
    biblioteca[nome].append(genero)
    biblioteca[nome].append(dinheiro)
    if nota >= 0 and nota <= 5:
        biblioteca[nome].append(nota)
    categorias.append(genero)
    gastosvalores.append(dinheiro)
    
    return biblioteca

print(adicionar())