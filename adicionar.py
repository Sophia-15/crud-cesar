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

print(adicionar())