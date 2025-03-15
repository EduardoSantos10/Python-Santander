# ENTRADA DE DADOS DO USÚARIO

"""
Em Python, a entrada e saída de dados nos permite interagir com o usuário e manipular arquivos. 
Podemos solicitar informações ao usuário, mostrar resultados na tela e ler ou escrever dados em arquivos externos.

Para obter informações do usuário durante a execução do programa, podemos utilizar a função input(). 
Esta função mostra uma mensagem na tela e espera que o usuário insira um valor.
"""

nome = input("Insira o seu nome: ")
idade = input("Insira a sua idade: ")

print("Ola, " + nome + "!")
print("Você tem " + idade + " anos.")


# ATENÇÃO
"""
A função input() sempre retorna uma cadeia de texto. 
Se você deseja trabalhar com outros tipos de dados, como números inteiros ou flutuantes, deve realizar uma conversão explícita utilizando funções como int() ou float().
"""

idade = int(input("Insira sua idade: "))

if idade >= 18:
    print("Você é maior de idade e já pode dirigir")
else:
    print("Você é menor de idade e não pode dirigir")



# SAIDA DE DADOS DO USUÁRIO
"""
Para mostrar informações na tela, utilizamos a função print(). Esta função recebe um ou mais argumentos e os mostra no console.

Podemos utilizar a f-string (formatação de cadeias) para inserir variáveis diretamente dentro de uma cadeia de texto.
"""

nomes = "Eduardo"
idades = 22

print(f"Olá, meu nome é {nomes} e tenho {idades} anos")

# Neste caso, as variáveis são inseridas dentro da cadeia utilizando chaves {} e a cadeia é precedida pela letra f para indicar que é uma f-string.


