"""
Criar uma variável que armazene o nome de uma pessoa:
a. exibir nome todas letras minúsculas
b. exibir nome todas letras maiúsculas
c. exibir primeiras letras maiúsculas e as demais minúsculas
"""

name_person = "Louise"
print(name_person) # This will print the name
exibe_name = name_person.upper()
print(exibe_name) # This will print the name in uppercase
exibe_name_2 = name_person[:3].upper()
exibe_name_3 = name_person[3:].lower()
print(exibe_name_2 + exibe_name_3) # This will print the name in uppercase