
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

import textwrap


 
 
b = ["a", "l", "o"]
n = [6, 3, 9]
 
while True:
  selection = int(input("enter number: "))
  if selection in n:
    index_ = n.index(selection)
    if index_ < len(b):
      print(f" {b[index_]} is on index[{index_}]")
