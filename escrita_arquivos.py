# ESCRITA DE ARQUIVOS

"""
Para escrever dados em um arquivo, abrimos em modo de escrita ("w") utilizando a função open(). 
Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, seu conteúdo será sobrescrito.
"""

arquivo = open("dados.txt", "w")
arquivo.write("Salve, rapazaiada!")
arquivo.close()

"""
Neste exemplo, o arquivo "dados.txt" é aberto em modo de escrita utilizando open(). 
Depois, a string "Olá, mundo!" é escrita no arquivo utilizando o método write(). Finalmente, o arquivo é fechado utilizando o método close().
"""

# LEMBRE - SE, SEMPRE FECHE SEUS ARQUIVOS

"""
Você também pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática.
"""

with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

"""
Neste caso, o arquivo é aberto utilizando a declaração with e é fechado automaticamente uma vez que se sai do bloco with, mesmo se ocorrer uma exceção.
"""

