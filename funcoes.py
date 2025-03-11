# FUNÇÕES

"""
As funções são blocos de código reutilizáveis que nos permitem encapsular tarefas específicas e executá-las quando necessário.
"""

def mensagem(): # Função definida
    print("Salve Rapaziada") # Mensagem a ser transmitida

mensagem() # Para chamar uma função, simplesmente escrevemos o nome da função seguido de parênteses.

# Para definirmos uma função, utilizamos a palavra-chave "DEF", seguida do nome da função e parentêses, podemos especificar parâmetros dentro dos parênteses



# PARÂMETROS E ARGUMENTOS

"""
As funções podem aceitar parâmetros, que são valores que são passados para a função quando ela é chamada. 
Os parâmetros são especificados dentro dos parênteses na definição da função.
"""

def saudacao(nome): # parâmetro dentro de parênteses
    print(f"Boa Noite, {nome}") # "f" -> Quando insere uma variável dentro de uma string

# Ao chamar a função, fornecemos os argumentos correspondentes aos parâmetros

saudacao("Eduardo") # Através do argumento "nome", e da junção de "f" para inserir variável em string, você consegue juntar a VAR com a string.




# VALORES DE RETORNO

"""
As funções podem retornar valores usando a palavra-chave return. O valor de retorno pode ser usado pelo código que chama a função.
"""

def subtracao(a, b): # Defini uma função com "a", "b" de parâmetros
    return a - b # Estou utilizando return para retornar um resultado

resultado = subtracao(10, 5) # Criei a Var "resultado" para receber a subtração de 10 - 5 = 5, nesse caso, os parâmetros
print(resultado) # Exibo em tela o resultado