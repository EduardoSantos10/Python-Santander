# TUPLAS

"""
Uma tupla é uma estrutura de dados imutável e ordenada que permite armazenar uma coleção de elementos. 
Os elementos de uma tupla são encerrados entre parênteses (), separados por vírgulas.

"""

# Criação e Acesso

numeros = (4, 5)

# Acessar os elementos

print(numeros[0]) # Imprimi o valor 4
print(numeros[1]) # 5


# MÉTODOS DE TUPLAS

minha_tupla = (1, 1, 2, 3, 4, 1)


# COUNT(elemento) -> O número de vezes que um elemento aparece na tupla
print(minha_tupla.count(1))


# INDEX(elemento) -> Devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca.
print(minha_tupla.index(1))
print(minha_tupla.index(1, 1))
print(minha_tupla.index(1, 1, 3))

# LEN(tupla) -> Está função devolve o comprimento da tupla, ou seja, quantos numeros tem a tupla citada
tamanho = len(minha_tupla) # Criei uma variavél para receber o tamanho da minha tupla
print(tamanho) # 6