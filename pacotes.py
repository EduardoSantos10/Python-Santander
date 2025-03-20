
"""
Um pacote é uma forma de organizar módulos relacionados em uma estrutura hierárquica de diretórios. 
Os pacotes nos permitem agrupar módulos relacionados e evitar conflitos de nomes entre módulos.
"""

# CRIAR E UTILIZAR PACOTES

"""
Para criar um pacote, criamos um diretório com o nome desejado e adicionamos um arquivo especial chamado __init__.py dentro do diretório. 
Este arquivo pode estar vazio ou conter código de inicialização do pacote.
"""

# EXEMPLOS:

"""
meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py
"""

"""
from meu_pacote import modulo1, modulo2

modulo1.funcao1()
modulo2.funcao2()
"""
