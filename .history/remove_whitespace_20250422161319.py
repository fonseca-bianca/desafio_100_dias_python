favorite_language = "Python "
print(favorite_language)

print(20 * "-")

favorite_language_2 = "Python "
# remove definitivo quando associada ao nome da variável
favorite_language_2 = favorite_language_2.rstrip() 
print(favorite_language_2) # This will remove the trailing whitespace
not_favorite_language = "JS"
print(not_favorite_language)

print(20 * "-")

programming_language = "' Python '"
print(programming_language.rstrip("'")) # pra mostrar q removeu o espaço
# em branco ao lado da aspa direita
print(programming_language.lstrip("'")) # pra mostrar q removeu o espaço
# em branco ao lado da aspa esquerda