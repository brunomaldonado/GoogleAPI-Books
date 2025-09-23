import time
import textwrap

def textwrap_title(title):
    spacing_line = " " * 6
    max_width = 48
    wrapped_title = textwrap.wrap(title, max_width)

    return [f"{spacing_line}{line}" for line in wrapped_title]

def textwrap_book(title):
  spacing_line = " " * 9
  max_width = 60
  wrapped_title = textwrap.wrap(title, max_width)

  return [f"{spacing_line}{line}" for line in wrapped_title]
  
def textwrap_message(title):
  max_width = 54 # límite de ancho
  wrapped_title = textwrap.fill(
    title,
    width=max_width,
    initial_indent=" ",      # la primera línea arranca con un espacio
    subsequent_indent=" "   # las demás líneas igual, alineadas a la izquierda
    )
  return wrapped_title

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

def indentation_title1(title, width=53, char_delay=0):
  # print(" " * 1, "-" * 53)
  first_line_prefix = " "
  current_line = first_line_prefix
  empty_line = " " * (len(first_line_prefix) - 2)
  title_lines = []
  spacing_line = " " * 6
  initial_spacing = " " * 1

  for word in title.split():
    if len(current_line) + len(word) + 1 > width:
      title_lines.append(current_line.strip())
      current_line = empty_line + word + " "
    else:
      current_line += word + " "

  title_lines.append(current_line.strip())
  print(initial_spacing, end="", flush=True)
  formatted_title = ""
  for i, line in enumerate(title_lines):
    if i == 0:
      formatted_title += line
    else:
      formatted_title += "\n" + spacing_line + line[len(empty_line):]

  return formatted_title

def indentation_title2(title, width=46, char_delay=0):
  # print(" " * 1, "-" * 53)
  first_line_prefix = "  "
  current_line = first_line_prefix
  empty_line = " " * (len(first_line_prefix) - 2)
  title_lines = []
  spacing_line = " " * 8

  for word in title.split():
    if len(current_line) + len(word) + 1 > width:
      title_lines.append(current_line.strip())
      current_line = empty_line + word + " "
    else:
      current_line += word + " "

  title_lines.append(current_line.strip())
  formatted_title = ""
  for i, line in enumerate(title_lines):
    if i == 0:
      formatted_title += line
    else:
      formatted_title += "\n" + spacing_line + line[len(empty_line):]

  return formatted_title

def indentation_title3(title, width=46, char_delay=0):
  first_line_prefix = "  "
  current_line = first_line_prefix
  empty_line = " " * (len(first_line_prefix) - 2)
  title_lines = []
  spacing_line = " " * 12
  for word in title.split():
    if len(current_line) + len(word) + 1 > width:
      title_lines.append(current_line.strip())
      current_line = empty_line + word + " "
    else:
      current_line += word + " "
  title_lines.append(current_line.strip())
  formatted_title = ""
  for i, line in enumerate(title_lines):
    if i == 0:
      formatted_title += line
    else:
      formatted_title += "\n" + spacing_line + line[len(empty_line):]
  return formatted_title

def indentation_title4(title, width=56, char_delay=0):
  first_line_prefix = "  "
  current_line = first_line_prefix
  empty_line = " " * (len(first_line_prefix) - 10)
  title_lines = []
  spacing_line = " " * 10
  initial_spacing = " " * 1

  for word in title.split():
    if len(current_line) + len(word) + 1 > width:
      title_lines.append(current_line.strip())
      current_line = empty_line + word + " "
    else:
      current_line += word + " "
  title_lines.append(current_line.strip())
  print(initial_spacing, end="", flush=True)
  formatted_title = ""
  for i, line in enumerate(title_lines):
    if i == 0:
      formatted_title += line
    else:
      formatted_title += "\n" + spacing_line + line[len(empty_line):]
  return formatted_title

def indentation_title5(title, width=58, char_delay=0):
  first_line_prefix = "  "
  current_line = first_line_prefix
  empty_line = " " * (len(first_line_prefix) - 2)
  title_lines = []
  initial_spacing = "" * 1
  spacing_line = "" * 1
  for word in title.split():
    if len(current_line) + len(word) + 1 > width:
      title_lines.append(current_line.strip())
      current_line = empty_line + word + " "
    else:
      current_line += word + " "

  title_lines.append(current_line.strip())
  print("\n", initial_spacing, end="", flush=True)

  #formatted_title = ""
  for i, line in enumerate(title_lines):
    if i == 0:
      #formatted_title += line
      for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    else:
      print("\n", spacing_line, end="", flush=True)
      #formatted_title += "\n" + spacing_line + line[len(empty_line):]

      for char in line[len(empty_line):]:
        print(char, end="", flush=True)
        time.sleep(char_delay)
  print("\n")
  #return formatted_title
  #return title_lines


def indentation_description(title, width=55, char_delay=0):
  first_line_prefix = " "
  current_line = first_line_prefix
  empty_line = " " * (len(first_line_prefix) - 2)
  title_lines = []
  spacing_line = "" * 1
  initial_spacing = " " * 1

  for word in title.split():
    if len(current_line) + len(word) + 1 > width:
      title_lines.append(current_line.strip())
      current_line = empty_line + word + " "
    else:
      current_line += word + " "

  title_lines.append(current_line.strip())
  print(initial_spacing, end="", flush=True)
  for i, line in enumerate(title_lines):
    if i == 0:
      for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    else:
      print("\n", spacing_line, end="", flush=True)

      for char in line[len(empty_line):]:
        print(char, end="", flush=True)
        time.sleep(char_delay)
  print("\n")

