for i in range(3):
    print("Olá Mundo!")



lista_preco = [1500, 1000, 800, 2000]
taxa_imposto = 0.1

for preco in lista_preco:
    imposto = preco * taxa_imposto

    print(f"Preço do Produto {preco}, imposto é de {imposto}")


print("------------EXEMPLO 1-----------------")


# EXEMPLOS
# produtos de até 1000 pagam 10%
# produtos acima de 1000 pagam 15% de imposto

for preco in lista_preco:
    if preco > 1000:
        taxa = 0.15
else:
    taxa = 0.1
imposto = taxa * preco
print(f"Preço do produto: {preco}, Imposto: {imposto}")

print("-------------EXEMPLO 2----------------")

# EXEMPLO 2
# mesma regra de imposto mas eu quero conseguir calcular o total de imposto somado a todos os preço


lista_preco = [1500, 1000, 800, 2000]
taxa_imposto = 0.1

total_imposto = 0

for preco in lista_preco:
    if preco > 1000:
        taxa = 0.15
else:
    taxa = 0.1
imposto = taxa * preco

total_imposto = total_imposto + imposto #  total_imposto += imposto

print("Total de Imposto", total_imposto)


print("-------------EXEMPLO 3----------------")

vendas_23 = {"jan": 15000, "fev": 10000, "mar": 50000}
vendas_24 = {"jan": 16000, "fev": 11000, "mar": 51000}

# calculo pecentual de crecimento // 16000/15000 -1 ---> quantos % eu cresci de um ano para o outro
 
for mes in vendas_24:
    valor_23 = vendas_23[mes]
    valor_24 = vendas_24[mes]

    crecimento = valor_24 / valor_23 - 1

    print(f"No mes de {mes}, o crecimento foi de {crecimento:.1%}")