# FUNÇÕES E CLASSES DE MODULO PADRÃO

"""
MATH: Fornece funções matemáticas, como sqrt() (raiz quadrada), sin() (seno), cos() (cosseno), entre outras.

RANDOM: Oferece funções para gerar números aleatórios, como random() (número aleatório entre 0 e 1), randint() (número inteiro aleatório em um intervalo), entre outras.

DATETIME: Permite trabalhar com datas e horas, como datetime.now() (data e hora atual), datetime.date() (data), datetime.time() (hora), entre outras.
""" 


import random
import datetime


aleatorio = random.randint(59, 68) # IMPRIME UM NUMERO INTEIRO ALEATÓRIO ENTRE 59 E 68
print(aleatorio)


data = datetime.datetime.now()
print(data) # IMPRIME A DATA E HORÁRIO ATUAL
