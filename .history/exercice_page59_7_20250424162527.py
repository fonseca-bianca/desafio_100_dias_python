"""
Use variável pra representar nome pessoa e inclua caracterese de espaço em 
branco no início e no final do nome. Use combinação carcteres "\t" e \"n" 
ao menos uma vez. Exiba o nome uma vez pra q o espaço em branco ao redor do 
nome seja mostrado. Em seguida, printe o nome usando cada uma das 3 funções 
de remoção (lstrip(), rstrip() e strip()).
"""

name_person = "#   \tAnne Frank\n  #"
print(f"Nome original: {name_person}")
print(f"Nome usando lstrip(): {name_person.lstrip()}")
print(f"Nome usando rstrip(): {name_person.rstrip()}")
print(f"Nome usando strip(): {name_person.strip()}")
