""" 
.sort():
    ordena a lista de forma permanente
    é um método de listas. Modifica a lista original.

.sorted(): 
    é uma função embutida
    Retorna uma nova lista ordenada, sem alterar o original.

Ambos métodos funcionam com qualquer tipo de dado comparável, como:
    números (int, float)
    strings
    listas de tuplas (se os elementos forem comparáveis entre si)
"""

# Exemplo de uso do método .sort():
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars_2 = ['bmw', 'audi', 'toyota', 'subaru']
cars_2.sort(reverse=True)  # Ordena em ordem decrescente
print(cars_2)

# Exemplo de uso da função sorted():
