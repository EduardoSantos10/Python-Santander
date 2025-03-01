# IF, IF-ELSE, IF-ELIF-ELSE

# Exemplo IF (Bloco é executado caso a condição seja verdadeira)

idade = 22

if idade >= 18:
    print("Você pode dirigir")


# IF-ELSE

if idade >= 25:
    print("Você é um adulto formado") # Executa o bloco de código caso ele seja verdadeiro
else:
    print("Você ainda não é adulto") # Executa o bloco de código caso ele seja falso



# IF-ELIF-ELSE

nota = 100

if nota >= 90:
    print("Parabens")

elif nota >= 80:
    print("Muito Bom") # ELIF é acionado quando ha mais de uma condição no nosso código, ele surge como alternativas

elif nota >= 70:
    print("Você passou, porém mais atenção")

else:
    print("Reprovado") # Caso nenhuma das opções acima seja verdadeira, ele será executado nesse bloco


# OBS: Pelo menos uma dessas condições será executadas