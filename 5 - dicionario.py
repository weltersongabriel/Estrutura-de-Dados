lista_produtos = ["violão", "teclado", "bateria"]
lista_precos = [2000, 3000, 5000]

# DICIONARIO
dicionario_produtos = {"violão":2000, "teclado": 3000, "bateria": 5000}

print(dicionario_produtos["violão"])

# ADICIONAR UM ITEM
dicionario_produtos["guitarra"] = 1500
print(dicionario_produtos)

# EDITAR UM ITEM
dicionario_produtos["violão"] = 2500 # dicionario_produtos["violão"] = dicionario_produtos["violão"] = 2500 * 1.1
print(dicionario_produtos)

# REMOVER UM ITEM 
dicionario_produtos.pop("teclado")
print(dicionario_produtos)


# VERIFICAR SE EXISTE UM ITEM NO DICIONARIO
print("bateria" in dicionario_produtos)
print("bateria" in dicionario_produtos.keys()) # As chaves do dicionario -> violão, teclado, baeria
print(5000 in dicionario_produtos.values()) # Os valores -> 2000, 3000, 5000


# CONTAGEM DE ITENS DO DICIONARIO
quantidade = len(dicionario_produtos)
print(quantidade)


# EXERCICIO
dicionario_produtos = {
    "violão": 2000,
    "teclado": 3000,
    "bateria": 5000,
    "guitarra": 2500,
    "baixo": 3500,
    "amplificador": 1500,
    "piano digital": 4000,
    "microfone": 800,
    "caixa de som": 1200,
    "pedal de efeito": 1000,
    "cajón": 600
}

buscar_produto = input("Digite o produto que deseja encontrar: ")

if buscar_produto in dicionario_produtos:
    preco = dicionario_produtos[buscar_produto]
    print("Produto encontrado")
    print(f"Produto: {buscar_produto}, preço: R${preco}")
else:
    print("Produto não Encontrado")
