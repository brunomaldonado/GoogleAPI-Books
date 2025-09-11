# book_number = [2, 10, 8, 1]
# selected_number = [8, 8]

# # Convertimos a sets para trabajar con únicos
# book_set = set(book_number)
# selected_set = set(selected_number)

# # Si hay intersección, quitamos esos elementos de book_set
# if book_set & selected_set:
#     resultado = len(book_set - selected_set)
#     print("Resultado:", resultado)
# else:
#     print("No hay coincidencias")


selected_number = [9, 5, 9, 5]
book_return = [5]

set_number = set(selected_number)
set_return = set(book_return)

print(f"\nselected_number {set_number}\nset_return {set_return}\n")
