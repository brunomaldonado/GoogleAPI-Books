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

# def textwrap_authors(author):
#   spacing_line = " " * 10
#   max_width = 43
#   wrapped_title = textwrap.wrap(author, max_width)

#   lines = [wrapped_title[0]]
#   lines.extend(f"{spacing_line}{line}" for line in wrapped_title[1:])
#   return "\n".join(lines)

# authors = "Douglas A. Bernstein, Julie Ann Pooley, Lynne Cohen, Steve Provost, Jacquelyn Cranney, Bethanie Gouldthorp, Neil Drew"

# #print("Authors: ")
# print(f" Authors: {textwrap_authors(authors)}")


# books = ["A very long book title that might need wrapping", "Short Title", "Another Extremely Long Book Title That Exceeds The Usual Limits", "Medium Length Title"]
# book_return = ["Medium Length Title"]
# el book_return el index es 0, como hacer para que en el books no me imprima el index 0, sino que me imprima el valor que sea igual al valor del book_return?

# while True:
#   selection = input("Enter a book title to remove (or 'exit' to quit): ")
#   if selection.lower() == 'exit':
#     break
#   if selection in book_return:
#     if selection in books:
#       index_ = books.index(selection)
#       print(f"'{books[index_]}' is on the books[{index_}].")
#     else:
#       continue

books = ["A very long book title that might need wrapping", "Short Title", "Another Extremely Long Book Title That Exceeds The Usual Limits", "Medium Length Title"]
book_number_return = [9, 3, 17]

while True:
  selection = int(input("Enter number (or 'exit' to quit): "))
  if selection in book_number_return:
    index_ = book_number_return.index(selection)
    if index_ < len(books):
      print(f"'{books[index_]}' is on the books[{index_}].")
    else:
      print(f"No book found for the number {selection}.")
  else:
    print(f"The number {selection} is not book_number_return.")

# si el selection esta en book_number_return, buscar el index en book_number_return y con ese index buscar el libro en books y mostrarlo

# def textwrap_description(description):
#   spacing_line = " " * 1
#   max_width = 53
#   wrapped_lines = textwrap.wrap(description, max_width)

#   justified_lines = []
#   for i, line in enumerate(wrapped_lines):
#     if i == len(wrapped_lines) - 1:
#       # última línea → alineada a la izquierda
#       justified_lines.append(spacing_line + line)
#     else:
#       words = line.split()
#       if len(words) == 1:
#         # si hay solo una palabra, no se puede justificar
#         justified_lines.append(spacing_line + line)
#       else:
#         total_spaces = max_width - sum(len(word) for word in words)
#         gaps = len(words) - 1
#         space_between, extra = divmod(total_spaces, gaps)

#         # repartir espacios entre palabras
#         justified_line = ""
#         for j, word in enumerate(words):
#           justified_line += word
#           if j < gaps:
#               justified_line += " " * (space_between + (1 if j < extra else 0))
#         justified_lines.append(spacing_line + justified_line)

#   return "\n".join(justified_lines)


# description = " We all endeavor to satisfy our needs and ambitions and endlessly strive to move up the economic ladder to achieve these aims. Although this is undoubtedly extremely satisfying and earns us social kudos, these ultimate goals are far from easy to attain and we are in a permanent and anxious struggle to reach them. Are we aware of all this? What is money? What purpose does it serve? Could we live without money? Is money good or bad? Was it necessary to invent money? Is money the only way to accumulate power? What is the state of non-necessity? Can the subconscious do without sex but not the money that brings us power? Why do we work so hard to get it? Is there any connection between psychology and economics? And psychology and money? And psychology and power? Are there any other types of power than money? Is knowledge as powerful as money? All of these questions and more are answered in Power and Money but only you can answer this one: Why should I invest in this book?"

# print(textwrap_description(description))
