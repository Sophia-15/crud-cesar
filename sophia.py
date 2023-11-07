biblioteca = {
  1: ['Berserk', 'Kentaro Miura', 'Seinen', 24.9],
}

def visualizar_livros():
  print(biblioteca)

def visualizar_livro(livro):
  livro = biblioteca.get(livro, 'Livro não encontrado')
  print(livro)

def excluir_livro(livro):
  print(biblioteca.pop(livro, 'Livro não encontrado'))