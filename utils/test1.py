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

 
