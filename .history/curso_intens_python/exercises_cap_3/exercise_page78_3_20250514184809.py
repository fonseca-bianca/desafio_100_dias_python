"""
Você descobriu que a mesa não chegará a tempo.
a. Comece o programa com base no exercício anterior.
b. Use .pop() pra remover cada convidado da lista, um por um, até que restem
apenas dois nomes na lista.
c. Exiba uma mensagem pra cada convidado que ainda está na lista.
d. Use del pra remover os dois últimos convidados pra que a lista fique vazia.
"""
invited = ['Anna', 'John', 'Lucy']
message_convite = "Do you want to have dinner at my house this friday night,"
 

print(f"{message_convite} {invited[0]}?")
print(f"{message_convite} {invited[1]}?")
print(f"{message_convite} {invited[2]}?")

print(f"{invited[0]} will not attend.")

print(20*"-")
invited[0] = 'Anthony'

print(f"{message_convite} {invited[0]}?")
print(f"{message_convite} {invited[1]}?")
print(f"{message_convite} {invited[2]}?")

print("We will invite more people as we have more tables available.")

print(20*"-")

invited.insert(0, 'Louise')
invited.insert(2, 'Jack')
invited.append('Kate')

invited_final = invited.copy()

print("Você só poderá convidar duas pessoas.")
print(20*"-")


# disinvitation_message = "I'm sorry, but I can't invite you to my house,"
# invited_final.pop(0)
# print(f"{disinvitation_message} {invited_final[0]}.")
# invited_final.pop(1)
# print(f"{disinvitation_message} {invited_final[1]}.")
# invited_final.pop(2)
# print(f"{disinvitation_message} {invited_final[2]}.")
# invited_final.pop(3)
# print(f"{disinvitation_message} {invited_final[3]}.")
