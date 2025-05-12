"""
MAIS CONVIDADOS:
Você encontrou uma mesa maior pro jantar, agora pode convidar mais pessoas.
Convide mais 3 pessoas.
Comece o programa com base no exercício anterior. Ao final, adicione um print()
informando que encontrou uma mesa maior.
Use:
    .insert() pra adcionar novo convidado no início da lista;
    .insert() pra adcionar novo convidado no meio da lista;
    .append() pra adcionar novo convidado no final da lista.
Ao final, exiba novo conjunto de mensagens do convite um pra cada pessoa da 
nova lista.  
"""

invited = ['Anna', 'John', 'Lucy']
message = "Do you want to have dinner at my house this friday night,"

invited.append('Ozzy') 

print(f"{message} {invited[0]}?")
print(f"{message} {invited[1]}?")
print(f"{message} {invited[2]}?")
print(f"{message} {invited[3]}?")
print(f"{invited[0]} will not attend.")

print(20*"-")
invited[0] = 'Anthony'

print(f"{message} {invited[0]}?")
print(f"{message} {invited[1]}?")
print(f"{message} {invited[2]}?")
print(f"{message} {invited[3]}?")
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

#     .insert() pra adcionar novo convidado no início da lista;
#     .insert() pra adcionar novo convidado no meio da lista;
#     .append() pra adcionar novo convidado no final da lista.
# Ao final, exiba novo conjunto de mensagens do convite um pra cada pessoa da 
# nova lista.  
