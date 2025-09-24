import textwrap

class bcolors:
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKCYAN = '\033[96m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'

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

def textwrap_title(title):
  prefix = " Title: "
  max_width = 56 # límite de ancho
  return textwrap.fill(
    title,
    width=max_width,
    initial_indent=prefix,
    subsequent_indent=" " * len(prefix),
    break_long_words=True,
    break_on_hyphens=True
    )
    
title = "Foundations of the Psychological Intervention Guide to Building Professional Competencies in School Psychology"

print(f"{textwrap_title(title)}\n\n")

def textwrap_booktitle(idx, title):
  prefix = f" {idx:2} "
  max_width = 55 # límite de ancho
  return textwrap.fill(
    title,
    width=max_width,
    initial_indent=prefix,
    subsequent_indent=" " * 9,
    )
    
    
formatted_titles = ["[19] Place Branding. La gastronomía como valor de marca y factor de atracción turística: el caso de España", "[ 9] TRADING CRIPTO Y DIVISAS: Trading Institucional + Smart Money", "[18] ¿Dónde va tu dinero? (Where Does Your Money Go?) 6-Pack"]

for idx, formatted_title in enumerate(formatted_titles, start=1):
  print(textwrap_booktitle(idx, formatted_title))
  
