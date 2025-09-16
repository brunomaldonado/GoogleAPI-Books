import time
import textwrap

def textwrap_title(title):
    spacing_line = " " * 6
    max_width = 49
    wrapped_title = textwrap.wrap(title, max_width)

    return [f"{spacing_line}{line}" for line in wrapped_title]

def textwrap_book(title):
  spacing_line = " " * 9
  max_width = 60
  wrapped_title = textwrap.wrap(title, max_width)

  return [f"{spacing_line}{line}" for line in wrapped_title]

def textwrap_message(message):
  spacing_line = " " * 1
  max_width = 53
  wrapped_title = textwrap.wrap(message, max_width)
  # first format
  # for line in wrapped_title:
  #   print(f"{spacing_line}{line}")

  # second format
  return "\n".join([f"{spacing_line}{line}" for line in wrapped_title])

def textwrap_authors(author):
  spacing_line = " " * 10
  max_width = 48
  wrapped_title = textwrap.wrap(author, max_width)
  
  lines = [wrapped_title[0]]
  lines.extend(f"{spacing_line}{line}" for line in wrapped_title[1:])
  
  return "\n".join(lines)

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

