# MÉTODOS DE LISTA

marcas = ["lg", "dell", "razer"]


# APPEND(elemento) -> Adiciona um elemento ao final da lista

marcas.append("nvidia")
print(marcas)


# INSERT(indice, elemento) -> Insere um elemento em determinado local da lista
marcas.insert(1, "apple")
print(marcas)


# REMOVE(elemento) -> Remove um determinado elemento da lista
marcas.remove("lg")
print(marcas)


# POP(indice) -> Remove e retorna um elemento em determinado local da lista
marca_removida = marcas.pop(1) # Estou mostrando o indice que estou removendo
print(marcas) # Imprimo a lista atual com a indice removido
print(marca_removida) # Imprimo o indice removido fora da lista


# SORT(vazio) -> Dependento da ordem que ele estiver (alfabeto ou numero), vai ser do maior para o menor
marcas.sort()
print(marcas)


# REVERSE(vazio) -> Inverte a ordem dos elementos da lista
marcas.reverse()
print(marcas)
