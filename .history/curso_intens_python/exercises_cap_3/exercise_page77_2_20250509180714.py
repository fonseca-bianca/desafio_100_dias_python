""" 
MUDANDO A LISTA DE CONVIDADOS:
Um dos convidados não poderá comparecer ao jantar. Você deverá enviar
um novo conjunto de convites. Convide outra pessoa no lugar dele.
a. comece com o programa do exercício anterior.
Ao final, adicione print() informando o nome de quem NÃO comparecerá;
b. modifique sua lista substituindo o nome de quem não vai pelo nome
do novo convidado;
c. exiba um segundo conjunto de mensagens de convite uma pra cada pessoa
que ainda não consta na lista
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

