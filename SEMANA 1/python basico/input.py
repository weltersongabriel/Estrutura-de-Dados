faturamento = input("Prencha com o faturamento: ")

# reaplace -> ela transforma uma string em outra
faturamento = faturamento.replace("R$", "").replace(",", ".")
faturamento = float(faturamento)
custo = 300

lucro = faturamento - custo
print("O lucro foi: ", lucro)


vendas_dia_1 = float(input("Vendas do dia 1: "))
vendas_dia_2 = float(input("Vendas do dia 2: "))

soma = vendas_dia_1 + vendas_dia_2
print("Resultado: ", soma)