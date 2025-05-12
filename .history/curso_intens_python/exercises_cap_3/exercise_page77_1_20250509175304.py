"""
LISTA DE CONVIDADOS:
se pudesse convidar qualquer pessoa, viva ou morta, pra um jantar, quem
você convidaria?
Crie uma lista com mín 3 pessoas e, após, use a lista pra exibir uma 
mensagem pra cada pessoa, convidando-a pro jantar
"""

invited = ['Anna', 'John', 'Lucy']
message = "Do you want to have dinner at my house this friday night,"

invited.append('Ozzy') # inclusão ao final do lista

print(f"{message} {invited[0]}?")
print(f"{message} {invited[1]}?")
print(f"{message} {invited[2]}?")
print(f"{message} {invited[3]}?")

# ao invés de tantos prints, poderia escrever assim tbm:
# for person in invited:
#     print(f"{message} {person}?")