"""
Você descobriu que a mesa não chegará a tempo.
a. Comece o programa com base no exercício anterior.
b. Use .pop() pra remover cada convidado da lista, um por um, até que restem
apenas dois nomes na lista.
c. Exiba uma mensagem pra cada convidado que ainda está na lista.
d. Use del pra remover os dois últimos convidados pra que a lista fique vazia.
"""
invited = ['Anna', 'John', 'Lucy']
message = "Do you want to have dinner at my house this friday night,"
 

print(f"{message} {invited[0]}?")
print(f"{message} {invited[1]}?")
print(f"{message} {invited[2]}?")

print(f"{invited[0]} will not attend.")

print(20*"-")
invited[0] = 'Anthony'

print(f"{message} {invited[0]}?")
print(f"{message} {invited[1]}?")
print(f"{message} {invited[2]}?")

print("We will invite more people as we have more tables available.")

print(20*"-")

invited.pop(0, 3)

print(f"{message} {invited[0]}?")
print(f"{message} {invited[1]}?")
print(f"{message} {invited[2]}?")
print(f"{message} {invited[3]}?")
print(f"{message} {invited[4]}?")
print(f"{message} {invited[5]}?")
