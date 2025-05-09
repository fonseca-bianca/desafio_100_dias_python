"""
Pense no seu meio de transporte favorito. Crie uma lista com 
diferentes tipos. Faça diferentes declarações com essa lista.
"""

vehicle_brands = ['citroen', 'volvo', 'kia']
message1 = "Seus carros têm design diferentes."
message2 = "Seus carros são seguros e potentes."
message3 = "Seus carros são perfeitos pra famílias."

print(f"{vehicle_brands[0].title()}: {message1}")
print(f"{vehicle_brands[1].title()}: {message2}")
print(f"{vehicle_brands[2].title()}: {message3}")

# Print q seria válido como parte de um código maior:
# print(
#     f"Os carros da {vehicle_brands[1].title()}" 
#     " são seguros e pontentes."
# )