# FUNÇÕES ANONIMAS (LAMBDA)

"""
Funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas.
"""

numero = lambda x: x ** 2 # Elevar um numero ao quadrado (x ** 2)
print(numero(10)) # Aqui ele irá printar o resultado da variavél número elevado ao quadrado.



# ESCOPOS DAS VARIAVÉIS (LOCAL vs. GLOBAL)

"""
As variáveis definidas dentro de uma função têm um escopo local, o que significa que só são acessíveis dentro da função. 
Por outro lado, as variáveis definidas fora de qualquer função têm um escopo global e podem ser acessadas de qualquer parte do programa.
"""

# VAR LOCAL: ela só pode ser chamada dentro da função.

# VAR GLOBAL: ela pode ser chamada de qualquer parte do programa.

def funcao():
    var_local = 10 # Essa VAR só pode ser acessivél dentro da função
    print(var_local)

var_global = 20

def funcao2():
    print(var_global) # Essa VAR pode ser acessivél de qualquer lugar do código

funcao()
funcao2()

print(var_global) # Continua a imprimir 20
# print(var_local) -> Vai gerar um erro, pois a VAR está definida apenas em escopo local