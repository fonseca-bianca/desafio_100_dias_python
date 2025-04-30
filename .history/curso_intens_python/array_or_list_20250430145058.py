"""

"""

# declarando var sem precisar declarar tipo
a = 3
b = 2
v = [6, 7, 8, 9] # lista/array (0 -> 6, 1 -> 7 etc.)

a = (v[2] - v[0]) + a
d = a * v[b]

print(f"A saída é: {d} {v[1]} {a+2}")

# Output: 40 7 7, pq:
    # a * v[b] --> onde v[b] corresponde ao v[2], logo, o valor é 8
    # na saída, d = 40, v[1] = 7, a+2 é a = 5 (novo valor) + 2 = 7