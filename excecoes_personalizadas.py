# EXCEÇÕES PERSONALIZADAS

"""
Além das exceções incorporadas no Python, você também pode criar suas próprias exceções personalizadas. 
Isso é útil quando deseja lidar com situações específicas do seu programa.

Para criar uma exceção personalizada, você deve criar uma classe que herde da classe base Exception ou de uma de suas subclasses.
"""

def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição de Erro")
    
try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")

# "RAISE" -> Lançara uma exceção automaticamente

"""
Neste exemplo, define-se uma função chamada funcao(). Dentro da função, verifica-se uma condição e, se for satisfeita, gera-se uma exceção utilizando a declaração raise. 
Em vez de criar uma classe personalizada, utiliza-se diretamente a classe base Exception para gerar a exceção.
"""

