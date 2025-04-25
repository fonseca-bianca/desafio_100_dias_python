"""
Escreva um programa que solicite ao usuário dois números e exiba:
soma, subtração, multiplicação e divisão entre eles.
"""

# recebe os números do usuário e os converte para float q aceita tanto
# inteiros quanto decimais:
number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))

# soma números recebidos:
sum_numbers = number1 + number2
print(f"A soma dos números é: {sum_numbers}")

# subtrai números recebidos:
subtraction_numbers = number1 - number2
print(f"A subtração dos números é: {subtraction_numbers}")

# multiplica números recebidos:
multiplication_numbers = number1 * number2
print(f"A multiplicação dos números é: {multiplication_numbers}")

# divide números recebidos:
# primeiro vai verificar se o 2º número é != de 0, pois não podem em divisão
if number2 == 0:
    print("Não é possível dividir um número por zero.")
else:
    division_numbers = number1 / number2
    print(f"A divisão dos números é: {division_numbers}")