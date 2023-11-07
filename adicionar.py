import os
os.system("cls")
biblioteca = {}
categorias = []
gastosvalores = []
def adicionar ():
    numlivro = input("Digite o número para cadastrar o livro: ")
    biblioteca[numlivro] = []
    nome = input("Insira o nome do livro que você deseja adicionar: ")
    autor = input("Agora insira as informações do livro abaixo, começando pelo autor do livro: ")
    genero = input("Gênero: ")
    dinheiro = input("Preço: ")
    nota = input("Nota pessoal: ")
    biblioteca[numlivro].append(nome)
    biblioteca[numlivro].append(autor)
    biblioteca[numlivro].append(genero)
    biblioteca[numlivro].append(dinheiro)
    biblioteca[numlivro].append(nota)
    categorias.append(genero)
    gastosvalores.append(dinheiro)
    return biblioteca
print(adicionar())