# Remover o prefixo de um endereço de site:

site_searched = "https://www.google.com"
site_searched_whithout_prefix = site_searched.removeprefix("https://")
print(site_searched_whithout_prefix) # This will remove the prefix "https://"

# tem q atribuir o NOVO resultado a uma NOVA variável (ou à mesma), pra q
# o novo valor apareça na tela pro usuário, visto q o método NÃO altera a
# string original e, tbm, pq no Python as strings são Imutáveis.