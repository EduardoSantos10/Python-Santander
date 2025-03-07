# CONJUNTOS

"""
Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. 
Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().
"""

# CRIAÇÃO E OPERAÇÕES

# TEMOS DUAS MANEIRAS DE CRIAR, CONJUNTOS.
# COM CHAVES {} E ATRAVÉS DA FUNÇÃO SET()

marcas = {"nike", "adidas", "puma", "decathlon"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {2, 4, 6}
conjunto2 = {6, 8, 10}


# UNIÃO -> uni os conjuntos
uniao = conjunto1 | conjunto2
print(uniao)

# INTERSEÇÃO -> parte onde ocorre o encontro de duas linhas
intersecao = conjunto1 & conjunto2
print(intersecao)

# DIFERENÇA -> retorna os elementos que estão em conjunto, mas não no outro (A, B)
diferenca = conjunto1 - conjunto2
print(diferenca)

# DIFERENÇA ASSIMETRICA -> exibe os elementos que não são iguais
diferenca_assimetrica = conjunto1 ^ conjunto2
print(diferenca_assimetrica)


# MÉTODOS DE CONJUNTOS

marcas = {"dell", "asus", "tecent", "google"}

# ADD(ELEMENTO) -> adiciona um elemento ao conjunto.
marcas.add("riot")
print(marcas)

# REMOVE(ELEMENTO) -> remove um elemento do conjunto. Se o elemento não existir, gera um erro.
marcas.remove("riot")
print(marcas)

# DISCARD(ELEMENTO) -> remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
marcas.discard("dell")
print(marcas)

# CLEAR(VAZIO): remove todos os elementos do conjunto.
marcas.clear()
print(marcas)