biblioteca = {
  'berserk': ['Berserk', 'Kentaro Miura', 'Seinen', 24.9],
  'cu': ['Berserk', 'Kentaro Miura', 'Seinen', 24.9],
  'eu': ['Berserk', 'Kentaro Miura', 'klasjdfk', 24.9],
}

def visualizar_livros():
  print(biblioteca)

def visualizar_livro(livro):
  livro = biblioteca.get(livro, 'Livro não encontrado')
  print(livro)

def excluir_livro():
  visualizar_livros()
  livro = int(input("Digite o número do livro que deseja excluir: "))
  print(biblioteca.pop(livro, 'Livro não encontrado'))

def filtrar_categoria(categoria):
  for livro in biblioteca.items():
    if categoria in livro[1]:
      print(livro[1])
