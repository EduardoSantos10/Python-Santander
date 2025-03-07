# DICIONÁRIOS

"""
Um dicionário é uma estrutura de dados mutável e não ordenada que permite armazenar pares de chave-valor. 
Cada elemento em um dicionário consiste em uma chave única e seu valor correspondente. 
Os dicionários são delimitados por chaves {}, e os pares chave-valor são separados por vírgulas.
"""

# CRIAÇÃO

pessoa = {"nome":"Eduardo","idade":22,"cidade":"São Bernardo"}

# COMO IMPRIMIR UM VALOR

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])


# MÉTODOS DE DICIONÁRIOS


# KEYS() -> retorna uma visualização de todas as chaves do dicionário.
print(pessoa.keys())

# VALUES() -> retorna uma visualização de todos os valores do dicionário.
print(pessoa.values())

# ITEMS() -> retorna uma visualização de todos os pares chave-valor do dicionário.
print(pessoa.items())

# UPDATE(OUTRO_DICIONÁRIO -> atualiza o dicionário com os pares chave-valor de outro dicionário.
pessoa.update({"profissao": "Engenheiro de Software"})
print(pessoa)