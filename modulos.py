# IMPORTAÇÃO E CRIAÇÃO DE MODULOS

#IMPORTAR MODULOS

"""
Para utilizar um módulo em nosso programa, devemos importá-lo utilizando a declaração import. 
Podemos importar um módulo completo ou funções específicas de um módulo.
"""

import math # Para utilizar um modulo no nosso programa, importamos com a declaração "import"

resultado = math.sqrt(35)
print(resultado)

"""
Neste exemplo, importa-se o módulo math utilizando a declaração import. 
Em seguida, utiliza-se a função sqrt() do módulo math para calcular a raiz quadrada de 25.
"""


# Exemplo utilizando importações especificas

from math import sqrt # Estaremos importando apenas a função "sqrt", sem ter que precede-lá a o nome de modulo

resultados = sqrt(25)
print(resultados)