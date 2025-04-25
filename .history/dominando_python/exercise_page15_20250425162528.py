""" 
Calcule a média aritmética de 2 números.
"""

number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))

# especificar a ordem das operações (ordem de precedentes). 
# Entre parênteses, o cálculo é feito antes:
media_numbers = (number1 + number2) / 2
print(f"A média dos números é: {media_numbers}")