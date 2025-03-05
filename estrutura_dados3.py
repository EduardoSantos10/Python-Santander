# LISTAS DE COMPREENSÃO

# nova_lista = [expressão FOR elemento IN sequencia IF condição]

numeros = [2, 4, 6, 8, 10, 11] # Criei uma lista de numeros

quadrados = [x ** 2 for x in numeros if x % 2 == 0] # 
print(quadrados)

"""
Neste exemplo, é criada uma nova lista chamada numeros, que contém os quadrados dos números pares da lista números. 
A expressão x ** 2 eleva cada elemento ao quadrado, e a condição if x % 2 == 0 filtra apenas os números pares.
"""