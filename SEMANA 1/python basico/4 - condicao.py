faturamento = 300
custo = 300

lucro = faturamento - custo


if lucro >= 0:
    print("Lucro de ", lucro)
else:
    print("Prejuizo de ", lucro)

print("Concluido")


# EXEMPLO
produtos = ["Celular", "Notebook", "Computador"]
novo_produto = input("Digite o nome do prduto: ")

if novo_produto in produtos:
    print("Produto já existente")
else:
    print(f"{novo_produto} cadastrado com sucesso")
    produtos.append(novo_produto)

print(produtos)


# EXEMPLO 2
# maior que 15000 ganha 500 de bonus
# entre 5000 a 15000 ganha 100 de bonus
# menos de 15000 sem bonus

vendas_empresa = 200_000
meta_empresa = 100_000

vendas_funcionario = 15000

if vendas_funcionario >= 15000 and vendas_empresa >= meta_empresa:
    bonus = 500
elif vendas_funcionario >= 5000 and vendas_empresa >= meta_empresa:
    bonus = 100
else:
    bonus = 0

print(f"O bonus do funcionario e: {bonus}")