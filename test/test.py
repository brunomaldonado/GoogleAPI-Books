import textwrap

def textwrap_authors(title):
  prefix = " Authors: "
  max_width = 54 # límite de ancho
  return textwrap.fill(
    title,
    width=max_width,
    initial_indent=prefix,
    subsequent_indent=" " * len(prefix),
    break_long_words=True,
    break_on_hyphens=True
    )
  
def textwrap_message(title):
  max_width = 56 # límite de ancho
  wrapped_title = textwrap.fill(
    title,
    width=max_width,
    initial_indent=" ",      # la primera línea arranca con un espacio
    subsequent_indent=" "   # las demás líneas igual, alineadas a la izquierda
    )
  return wrapped_title

message1 = "Some of the Most Distinguished Psychologists of the World Reflect About the Future of their Discipline"

message2 = "The book of The Concise Corsini Encyclopedia of Psychology and Behavioral Science has been added into the bookstore."

message = "The book of A Practical Guide to Building Professional Competencies in School Psychology has been added into the bookstore."

subtitle = "..."

authors = "Krisstal D. Clayton, Gregory J. Privitera, Saul Kassin"

print(""*1,"-"*54)

#print(f"{textwrap_subtitle(subtitle)}")
print(f"{textwrap_authors(authors)}")
print(textwrap_message(message))

 
