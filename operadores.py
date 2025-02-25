# Aritméticos

"""
+ (Soma)
- (Subtração)
* (Multiplicação)
/ (Divisão)
// (Divisão inteira, o resultado será um número inteiro, a parte decimal é descartada)
% (Devolve o resto da divisão)
** (Eleva o primeiro valor a potência do segundo)
"""

# Exemplos

a = 10
b = 2

soma = 10 + 2
subs = 10 - 2
multi = 10 * 2
div = 10 / 2
div_inteira = 10 // 2
modulo = 10 % 2
exponen = 10 ** 2

print(soma)


# Comparação

"""
== (Igual á, devolve True se ambos os valores são iguais)
!= (Diferente de, devolve True se os valores são diferentes)
> (Maior que, devolve True se o primeiro valor é maior que o segundo)
< Menor que, (devolve True se o primeiro valor é menor que o segundo)
>= (Maior ou igual á, devolve True se o primeiro valor é maior ou igual que o segundo)
<= (Menor ou igual á, devolve True se o primeiro valor é menor ou igual que o segundo)
"""

# Exemplos

c = 20
d = 4

igual = 20 == 4
dif = 20 != 4
maior = 20 > 4
menor = 20 < 47
maior_igual = 20 >= 4
menor_igual = 20 <= 4

print(menor_igual)


#Lógicos

"""
AND (and, devolve True se ambas as condições são verdadeiras)
OR (or, devolve True se ao menos uma das condições é verdadeira)
NOT (not, inverte o valor de uma condição, devolve True se a condição é falsa e False se a condição é verdadeira)
"""

# Exemplos

e = 40
f = 8

result_and = (e > 20) and (f < 20)
result_or = (e > 20) or (f < 19)
result_not = not (e > 39)

print(result_not)
