import textwrap

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

def textwrap_message(message):
  spacing_line = " " * 2
  max_width = 53
  wrapped_title = textwrap.wrap(message, max_width)
  # for line in wrapped_title:
  #   print(f"{spacing_line}{line}")

  return "\n".join([f"{spacing_line}{line}" for line in wrapped_title])

message = "The book of TRADING CRIPTO Y DIVISAS: Trading Institucional + Smart Money is not available, it has been previously loaned."

# textwrap_message(message)
print(f"\n{textwrap_message(message)}\n")
