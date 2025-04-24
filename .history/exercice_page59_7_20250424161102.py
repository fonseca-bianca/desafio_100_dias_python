"""
Use variável pra representar nome pessoa e inclua caracterese de espaço em 
branco no início e no final do nome. Use combinação carcteres "\t" e \"n" 
ao menos uma vez. Exiba o nome uma vez pra q o espaço em branco ao redor do 
nome seja mostrado. Em seguida, printe o nome usando cada uma das 3 funções 
de remoção (lstrip(), rstrip() e strip()).
"""

name_person = "Anne Frank"
name_person = "\t\n" + name_person + "\t\n"
print(name_person)