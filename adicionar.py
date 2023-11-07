import os
os.system("cls")
biblioteca = {}
def adicionar ():
    numlivro = input("Digite o número para cadastrar o livro: ")
    biblioteca[numlivro] = []
    nome = input("Insira o nome do livro que você deseja adicionar: ")
    autor = input("Agora insira as informações do livro abaixo, começando pelo autor do livro: ")
    genero = input("Gênero: ")
    dinheiro = input("Preço: ")
    biblioteca[numlivro].append(nome)
    biblioteca[numlivro].append(autor)
    biblioteca[numlivro].append(genero)
    biblioteca[numlivro].append(dinheiro)
    return biblioteca
print(adicionar())