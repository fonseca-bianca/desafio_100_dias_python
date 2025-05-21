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

invited.insert(0, 'Louise')
invited.insert(2, 'Jack')
invited.append('Kate')

print(f"{message} {invited[0]}?")
print(f"{message} {invited[1]}?")
print(f"{message} {invited[2]}?")
print(f"{message} {invited[3]}?")
print(f"{message} {invited[4]}?")
print(f"{message} {invited[5]}?")


disinvitation_message = "I'm sorry, but I can't invite you to my house,"

print(f"{disinvitation_message} {invited.pop(5)}.")
print(f"{disinvitation_message} {invited.pop(4)}.")
print(f"{disinvitation_message} {invited.pop(3)}.")
print(f"{disinvitation_message} {invited.pop(2)}.")

# OBS.:
# ✅ Remover de trás para frente evita confusão com os índices que mudam a 
# cada remoção.

# ❌ Remover do início para o fim pode causar erros ou pular elementos.
#     nomes = ["Anna", "John", "Lucy", "Kate"]
# # Exemplo de erro:
#     # Suponha que você queira remover os 3 primeiros elementos:
#     nomes.pop(0)  # Remove "Anna" → agora a lista é ["John", "Lucy", "Kate"]
#     nomes.pop(1)  # Remove "Lucy", porque "John" 
#                       agora está no índice 0 → ["John", "Kate"]
#     nomes.pop(2)  # Erro! Só tem índices 0 e 1 agora.

print(f"{invited[0]}, your invitation remains open.")
print(f"{invited[1]}, your invitation remains open.")

del invited[0:2]
print(f"List of invited: {invited}")