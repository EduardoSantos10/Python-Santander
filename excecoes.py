# MANEJO DE EXEÇÕES

"""
O manejo de exceções nos permite capturar e lidar com erros de maneira controlada utilizando as declarações try, except e opcionalmente finally.
"""


# TRY
"""
O bloco try contém o código que pode gerar uma exceção. Se ocorrer uma exceção dentro do bloco try, o fluxo de execução é transferido para o bloco except correspondente.
"""

try:
    # Codigo que pode gerar uma exceção

    resultado = 10 / 0 # Divisão por zero
    print(resultado) # Nesse caso vai ocorrer um SyntaxError(erro de sintaxe)
except ZeroDivisionError:
    print("Erro: Divisão por zero")




# EXCEPT
"""
O bloco except especifica o tipo de exceção que se deseja capturar e lidar. Você pode ter múltiplos blocos except para lidar com diferentes tipos de exceções.
"""

try:
    # Código que pode gerar uma exceção
    resultados = 10 / 0 # Divisão por zero
    print(resultados)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")

# Blocos "except" são alternativas para lhe dar com o meu erro



# FINALLY
"""
O bloco finally é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não. 
É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos.
"""

try:
    # Código que pode gerar um exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close() # Fecha o arquivo sempre, mesmo se ocorrer uma exceção
