lista_estoque = []

def adicionar_produto():
    resposta = ()
    produto = input("Digite o nome do produto a ser adicionado: ")
    lista_estoque.append(produto)
    print(f"'{produto}' adicionado ao estoque.")
    resposta = input("\nDeseja adicionar mais um produto? [S/N] ")
    while resposta == "S":
      if resposta == "S":
        produto = input("Digite o nome do produto a ser adicionado: ")
        lista_estoque.append(produto)
        print(f"'{produto}' adicionado ao estoque. \n")
        resposta = input("Deseja adicionar mais um produto? [S/N] ")
      elif resposta == "N":
        print("Retornando ao menu... \n")
        break
      else:
        print("Opção inválida. Tente novamente. \n")


def trocar_produto(lista_estoque):
    print("Estoque atual:", lista_estoque, "\n")
    produto_a_substituir = input("Digite o nome do produto que gostaria de trocar: ")
    if produto_a_substituir in lista_estoque:
        novo_produto = input(f"Informe o produto que irá substituir '{produto_a_substituir}': ")
        indice = lista_estoque.index(produto_a_substituir)
        lista_estoque[indice] = novo_produto
        print(f"'{produto_a_substituir}' foi substituído por '{novo_produto}'.\n")
        print("Estoque atual:", lista_estoque, "\n")
    else:
        print(f"'{produto_a_substituir}' não encontrado no estoque. \n")
    

def remover_produto():
    produto = input("Digite o nome do produto a ser removido: ")
    if produto in lista_estoque:
      lista_estoque.remove(produto)
      print(f"'{produto}' removido do estoque.")
    else:
      print(f"'{produto}' não encontrado no estoque. \n")

    resposta = input("\nDeseja remover mais um produto? [S/N] ")
    while resposta == "S":
      if resposta == "S":
        produto = input("Digite o nome do produto a ser removido: ")
        lista_estoque.remove(produto)
        print(f"'{produto}' removido do estoque. \n")
        resposta = input("Deseja remover mais um produto? [S/N] ")
      elif resposta == "N":
        print("Retornando ao menu... \n")
        break  
      

def exibir_estoque():
    print("Estoque atual:", lista_estoque, "\n")


while True:
    print("1. Adicionar Produto")
    print("2. Trocar Produto")
    print("3. Remover Produto")
    print("4. Exibir Estoque")
    print("5. Sair")

    escolha = input("\nEscolha uma opção (1/2/3/4/5): ")
    print("\n")

    if escolha == '1':
        adicionar_produto()
    elif escolha == '2':
        trocar_produto(lista_estoque)
    elif escolha == '3':
        remover_produto()
    elif escolha == '4':
        exibir_estoque()
    elif escolha == '5':
        print("Saindo do programa... ")
        break
    else:
        print("[ERRO] Tente novamente.")