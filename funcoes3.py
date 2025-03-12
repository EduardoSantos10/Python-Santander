# FUNÇÕES DEFINIDAS PELO USUÁRIO

"""
É uma boa prática documentar nossas funções utilizando docstrings. 
Os docstrings são cadeias de texto que descrevem o propósito, os parâmetros e o valor de retorno de uma função. 
São colocados imediatamente após a definição da função e são encerrados entre aspas duplas triplas.
"""

# -> DOCUMENTAÇÃO DE FUNÇÕES (docstrings)

def area_retangulo(base, altura):
    """Calcula a área de um retângulo

    Args:
        base (float): A base do retângulo
        altura (float): A altura do retângulo

    Returns:
        float: A área do retângulo.
    """

    return base * altura


# -> FUNÇÕES COM NÚMEROS VARIÁVEIS DE ARGUMENTOS

"""
Python permite definir funções que aceitem um número variável de argumentos(inserir diversos valores no parametro). 
Isso é feito utilizando o operador * antes do nome do parâmetro.
"""

def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(1, 2, 3))  # Ele irá imprimir 6.
print(soma_variavel(4, 5, 6, 7))  # Ele irá imprimir 22.

"""
As funções são uma ferramenta fundamental na programação e nos permitem estruturar e modularizar nosso código. 
Com a capacidade de definir funções personalizadas, podemos encapsular tarefas específicas e reutilizá-las em diferentes partes do nosso programa.

Além das funções definidas pelo usuário, Python também fornece uma ampla gama de funções incorporadas que podemos utilizar diretamente, como print(), len(), range(), entre outras.
"""