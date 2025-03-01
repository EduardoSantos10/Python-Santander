# BREAK -> Sair prematuramente de um loop

contador = 0 # Inicio o contador em 0

while True: # Condição para o contador
    print(contador) # Printar o valor atual na tela
    contador += 1 # Realiza a incrementação de +1

    if contador == 6: # Condição para verificar se ele é igual a 6
        break # Instrução BREAK automaticamente para o loop e a condição, e passa para o próximo bloco




# CONTINUE -> pular o restante do bloco

for i in range(10): # For vai iterar sobre números de 0 a 9, e range() é utilizado para percorrer sobre esses números
    if i % 2 == 0:  # Caso número seja par, ele será divisivél por 2, será executado a operação, fazendo com que ele pule o resultado e a próxima iteração seja executada
        continue # Caso número seja divisivel por 2, ele irá pular
    print(i) # Printar o resultado




# PASS

for i in range(5):
    pass # Instrução PASS, não possui funcionalidade nenhuma, serve apenas para marcar o bloco de código