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
import textwrap

def textwrap_message(message):
  spacing_line = " " * 2
  max_width = 53
  wrapped_title = textwrap.wrap(message, max_width)
  # for line in wrapped_title:
  #   print(f"{spacing_line}{line}")

<<<<<<< HEAD
def textwrap_authors(author):
  spacing_line = " " * 10
  max_width = 43
  wrapped_title = textwrap.wrap(author, max_width)
  
  lines = [wrapped_title[0]]
  lines.extend(f"{spacing_line}{line}" for line in wrapped_title[1:])
  return "\n".join(lines)

authors = "Douglas A. Bernstein, Julie Ann Pooley, Lynne Cohen, Steve Provost, Jacquelyn Cranney, Bethanie Gouldthorp, Neil Drew"

#print("Authors: ")
print(f" Authors: {textwrap_authors(authors)}")

 
=======
  return "\n".join([f"{spacing_line}{line}" for line in wrapped_title])

message = "The book of TRADING CRIPTO Y DIVISAS: Trading Institucional + Smart Money is not available, it has been previously loaned."

# textwrap_message(message)
print(f"\n{textwrap_message(message)}\n")
>>>>>>> 7f11870db6ce56037ca9c7ad323588e1ee678db7
