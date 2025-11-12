# 1️ Criamos uma classe que representa um NÓ da lista
class Node:
    def __init__(self, data):
        self.data = data      # Guarda o valor (por exemplo: 10, 20, 30)
        self.next = None      # Guarda o endereço do próximo nó (começa sem nada)

# 2️ Criamos a classe da LISTA LIGADA
class LinkedList:
    def __init__(self):
        self.head = None  # O primeiro nó da lista (a "cabeça"). Começa vazia.

    # 3️ Adicionar um novo nó no final da lista
    def append(self, data):
        new_node = Node(data)  # Cria um novo nó com o valor passado

        # Se a lista está vazia, o novo nó vira o primeiro
        if self.head is None:
            self.head = new_node
            return

        # Caso contrário, percorre a lista até o último nó
        current = self.head
        while current.next:
            current = current.next

        # Quando achar o último nó, liga o novo nó a ele
        current.next = new_node

    # 4️ Mostrar os valores da lista
    def display(self):
        current = self.head

        # Se a lista estiver vazia
        if not current:
            print("A lista está vazia.")
            return

        # Percorre todos os nós e mostra os dados
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indica o fim da lista

    # 5️ Remover um nó pelo valor
    def remove(self, data):
        current = self.head
        previous = None

        # Se o primeiro nó for o que queremos remover
        if current and current.data == data:
            self.head = current.next  # O segundo nó vira o primeiro
            return

        # Percorre até encontrar o valor
        while current and current.data != data:
            previous = current
            current = current.next

        # Se não achou o valor
        if current is None:
            print("Valor não encontrado na lista.")
            return

        # "Pula" o nó a ser removido
        previous.next = current.next

# 6️ Testando tudo

lista = LinkedList()  # Criamos uma nova lista vazia

# Adicionamos alguns números
lista.append(10)
lista.append(20)
lista.append(30)

print("Lista atual:")
lista.display()

# Removendo um valor
lista.remove(20)

print("Após remover o número 20:")
lista.display()
