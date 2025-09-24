import time
import textwrap

def textwrap_booksfound(title):
    spacing_line = " " * 6
    max_width = 48
    wrapped_title = textwrap.wrap(title, max_width)

    return [f"{spacing_line}{line}" for line in wrapped_title]

def textwrap_booktitle(idx, title):
  prefix = f" {idx:2} "
  max_width = 55 # límite de ancho
  return textwrap.fill(
    title,
    width=max_width,
    initial_indent=prefix,
    subsequent_indent=" " * 9,
    )
  
def textwrap_message(title):
  max_width = 54 # límite de ancho
  wrapped_title = textwrap.fill(
    title,
    width=max_width,
    initial_indent=" ",      # la primera línea arranca con un espacio
    subsequent_indent=" "   # las demás líneas igual, alineadas a la izquierda
    )
  return wrapped_title

def textwrap_title(title):
  prefix = " Title: "
  max_width = 54
  return textwrap.fill(
    title,
    width=max_width,
    initial_indent=prefix,
    subsequent_indent=" " * len(prefix),
    break_long_words=True,
    break_on_hyphens=True
    )
    
def textwrap_subtitle(subtitle):
  prefix = " Sub Title: "
  max_width = 54

  return textwrap.fill(
    subtitle,
    width=max_width,
    initial_indent=prefix,
    subsequent_indent=" " * len(prefix),
    break_long_words=True,       # permite cortar palabras largas
    break_on_hyphens=True        # permite dividir con guiones
  )

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

def textwrap_description(description):
  spacing_line = " " * 1
  max_width = 53
  wrapped_lines = textwrap.wrap(description, max_width)

  justified_lines = []
  for i, line in enumerate(wrapped_lines):
    if i == len(wrapped_lines) - 1:
      # última línea → alineada a la izquierda
      justified_lines.append(spacing_line + line)
    else:
      words = line.split()
      if len(words) == 1:
        # si hay solo una palabra, no se puede justificar
        justified_lines.append(spacing_line + line)
      else:
        total_spaces = max_width - sum(len(word) for word in words)
        gaps = len(words) - 1
        space_between, extra = divmod(total_spaces, gaps)

        # repartir espacios entre palabras
        justified_line = ""
        for j, word in enumerate(words):
          justified_line += word
          if j < gaps:
              justified_line += " " * (space_between + (1 if j < extra else 0))
        justified_lines.append(spacing_line + justified_line)

  return "\n".join(justified_lines)

