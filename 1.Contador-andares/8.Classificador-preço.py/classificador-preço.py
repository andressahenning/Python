try:

    produto = input("Insira o nome do produto: ")

    preco_produto = float(input("Insira o preço do produto: "))

    if preco_produto < 50:
        print(f"{produto} é classificado como preço baixo")
    elif  50 <= preco_produto <= 100: 
        print(f"{produto} é classificado como preço médio")
    else:
        print(f"{produto} é classificado como preço alto")

except(ValueError, TypeError):
    print('[ERRO] Caractere inválido! Tente novamente.')
