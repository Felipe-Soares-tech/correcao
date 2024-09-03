from cgitb import reset
from unittest import result


resultado = int()

for i in range(1,6):
    numero = int(input(f'informe o numero {i}: '))
    resultado += numero


print(resultado)
