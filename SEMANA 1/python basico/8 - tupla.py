# Principal função da TUPLA e não poder ser editada --> Exemplo: tela_pc = (1920, 1080)

# bonus 1: R$ 2,00 por venda feita
# bonus 2: 1% do valor de vendas

def calcular_bonus(lista_vendas):

    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)

    return bonus1, bonus2

vendas = [100, 250, 400, 1000]

bonus1, bonus2 = calcular_bonus(vendas)

print(bonus1)
print(bonus2)


print("------------ EXERCICIO -----------------")

def calcular_bonus(lista_vendas):

    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)

    return bonus1, bonus2

vendas = {
    "João": [1200, 1500, 1800, 1300, 1400, 1550, 1600, 1350, 1450, 1700, 1850],
    "Maria": [2200, 2500, 2700, 2300, 2400, 2600, 2650],
    "Carlos": [800, 100],
    "Ana": [1400, 1600, 1800, 1750, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700]
}

# Quero calcular o bonus de cada funcionario
# total de bonus 1 pago aos funcionarios
# total de bonus 2 pago aos funcionarios

total_bonus_1 = 0
total_bonus_2 = 0
for vendedor in vendas:
    bonus1, bonus2 = calcular_bonus(vendas[vendedor])
    print(f"Vendedor --> {vendedor}. Bonus 1: {bonus1}. Bonus 2: {bonus2}")

    total_bonus_1 = total_bonus_1 + bonus1
    total_bonus_2 = total_bonus_2 + bonus2

print("Total Bonus 1 ---> ", total_bonus_1)
print("Total Bonus 2 ---> ", total_bonus_2)
