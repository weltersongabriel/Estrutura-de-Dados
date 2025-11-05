lista_vendas = [100, 50, 90, 250, 300] # Toda lista fica dentro de []

print(lista_vendas [0]) # Pegar um elemento da lista

# len -> tamanho
tamanho_lista = len(lista_vendas)
print(tamanho_lista) # Pegar o tamanho da Lista

# sum -> somar
total_vendas = sum(lista_vendas) # Somar todos os itens
print(total_vendas)

# maximo, minimo, media
print(max(lista_vendas))
print(min(lista_vendas))
print(total_vendas / tamanho_lista)



# Encontrar um Elemento na Lista ( A POSIÇÃO DO ELEMENTO)
lista_carros = ["BMW", "Ferrari", "Audi", "Mercedes", "Fiat"]
print(lista_carros)
print("Tem o carro Audi", "Audi" in lista_carros) # in -> e para saber se tem na lista // A resposta sera True ou False

posicao = lista_carros.index("BMW")
print(posicao)



# Editar um Item
precos_carros = [300, 1500, 200, 250, 100]
novo_preco = precos_carros[0] * 1.1
precos_carros[0] = novo_preco
print(precos_carros)

# Remover um item da lista
lista_carros.remove("Fiat") # Remover com remove
lista_carros.pop(2) # Remover com pop
print(lista_carros)

# Adicionar um Item na Lista
lista_carros.append("Porsche") # Adicionar com append
print(lista_carros)

lista_carros_2 = ["Mustang", "Camaro", "Civic"]
lista_carros.extend(lista_carros_2) # extend -> adiciona itens de uma lista a outra
print(lista_carros)


# Inserir um item em posição especifica
lista_carros.insert(1, "BMW")
print(lista_carros)

# Contar quantas vezes o item aparece na Lista
print(lista_carros.count("BMW"))


# Oredena uma Lista
lista_carros.sort() # Se colocar sort(reverse) a lista ordena de forma oposta
print(lista_carros)