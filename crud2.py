biblioteca = {}

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
         

        

        





        

