lista_preco = [1500, 1000, 800, 2000]

# produtos de até 1000 pagam 10%
# produtos acima de 1000 pagam 15% de imposto

def calcular_imposto(lista_valores): # def -> definir uma função
    imposto_total = 0
    for preco in lista_valores:
        if preco > 1000:
            taxa = 0.15
        else:
            taxa = 0.1
        imposto = preco * taxa
        imposto_total = imposto_total + imposto
    return imposto_total
    

imposto_lista_1 = calcular_imposto(lista_preco)
print(imposto_lista_1)


lista_preco_2 = [7500, 3000, 1000, 4400]
imposto_lista_2 = calcular_imposto(lista_preco_2)

print(imposto_lista_2)

# PARA MELHOR ENTENDIMENTO
def aprendendo_funcao():
    print("Aprendendo Função")
    print("Que desistir nunca seja uma opção")

aprendendo_funcao()