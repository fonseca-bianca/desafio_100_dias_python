""" 
Escreva um programa que calcule a média de 3 notas informadas pelo usuário.
"""

grade1 = float(input("Digite a 1ª nota: "))
grade2 = float(input("Digite a 2ª nota: "))
grade3 = float(input("Digite a 3ª nota: "))

media_grades = (grade1 + grade2 + grade3) / 3
print(f"A média das 3 notas é: {media_grades:.2f}")