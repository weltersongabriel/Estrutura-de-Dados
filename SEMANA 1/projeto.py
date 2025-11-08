"""
Explicação:
A ideia é ter um pequeno programa que permita cadastrar, listar, buscar e remover
itens (como alunos e suas notas, ou produtos e preços).

Esse tipo de projeto te obriga a:

Usar listas ou dicionários para armazenar dados;
Criar funções para organizar o código;
Praticar entrada e saída de dados;
E desenvolver o raciocínio de como estruturar informações de forma lógica.


💡 É um projeto simples, mas poderoso: ele consolida sua base e já te prepara para entender estruturas de dados mais complexas nas próximas semanas.
"""

alunos_notas = {
    "Ana": 9.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8,
    "Eduardo": 5.9,
    "Fernanda": 8.0,
    "Gabriel": 8.5,
    "Helena": 9.0,
    "Igor": 6.3,
    "Juliana": 8.7,
    "Kaun": 4.0
}

print(alunos_notas)


def adicionar_aluno():
    nome_aluno = input("Digite o nome do Aluno: ")
    #nota_aluno = float(input("Digite a nota do Aluno: "))
    if nome_aluno in alunos_notas:
        print("Aluno já existente")
        print(alunos_notas)
        
    else:
        nota_aluno = float(input("Digite a nota do Aluno: "))
        alunos_notas[nome_aluno] = nota_aluno
        print(alunos_notas)
    
    
    return

def editar_aluno():
    nome_aluno = input("Digite o nome do Aluno: ")
    nota_aluno = float(input("Digite a nota do Aluno: "))

    alunos_notas[nome_aluno] = nota_aluno
    print(alunos_notas)
    return

def remover_aluno():
    nome_aluno = input("Digite o nome do Aluno: ")

    alunos_notas.pop(nome_aluno)
    print(alunos_notas)
    return



print("Goastaria de Editar ?")

dicionario = int(input("DIGITE\n 1 para adicionar\n 2 para ediar\n 3 para remover\n 0 para visualizar\n -->: "))


if dicionario == 1:
    print(adicionar_aluno())
elif dicionario == 2:
    print(editar_aluno())
elif dicionario == 3:
    print(remover_aluno())
elif dicionario == 0:
    print("Confita a Lista de Alunos")
    print(alunos_notas)
else:
    print("NÃO ENTENDI\nESCREVA APENAS --> 0 - 1 - 2 - 3")

    