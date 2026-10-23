import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()



def pesquisar_produto():
    produtos = carregar_produtos()
    pesquisar_produto = input("Qual o nome do produto você gostaria de encontrar? ")
    for produto in produtos:
        if produto["nome"].lower() == pesquisar_produto.lower():
            print(produto)

def pesquisar_categoria():
    produtos = carregar_produtos()
    pesquisar_categoria = input("Qual categoria você gostaria de encontrar? ")
    for produto in produtos:
        if produto["categoria"].lower() == pesquisar_categoria.lower():
            print(produto)

def pesquisar_preco():
    produtos = carregar_produtos()
    pesquisar_preco = float(input("Você gostaria de ver produtos até quantos R$? "))
    for produto in produtos:
        if produto["preco"] <= pesquisar_preco:
            print(produto)

def pesquisar_estoque():
    produtos = carregar_produtos()
    pesquisar_estoque = int(input("Você gostaria de ver produtos com estoque de até: "))
    for produto in produtos:
        if produto["estoque"] <= pesquisar_estoque:
            print(produto)
    

def adicionar_produto():
    produtos = carregar_produtos()
    id_produto = input("Qual o id do produto novo? ")
    nome_produto = input("Qual o nome do produto novo? ")
    categoria_produto = input("Qual a categoria do produto novo? ")
    preco_produto = input("Qual o preço do produto novo? ")
    estoque_produto = input("Qual a quantidade desse produto no estoque? ")

    novo_produto = {
        "id": id_produto,
        "nome": nome_produto,
        "categoria": categoria_produto,
        "preco": preco_produto,
        "estoque": estoque_produto
    }

    produtos.append(novo_produto)
    print(produtos)

while True:
    print("! ---> Controle de Estoque <--- !")
    print("1 - pesquisar produto")
    print("2 - pesquisar categoria")
    print("3 - pesquisar por preço")
    print("4 - pesquisar por estoque")
    print("5 - adicionar produto")


    opcao = input("Seleione uma das opções a cima! ")

    if opcao == "1":
        pesquisar_produto()

    elif opcao == "2":
        pesquisar_categoria()

    elif opcao == "3":
        pesquisar_preco()

    elif opcao == "4":
        pesquisar_estoque()

    elif opcao == "5":
        adicionar_produto()




    break



