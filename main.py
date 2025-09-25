from utils import server
from utils.config import textwrap_booksfound, textwrap_booktitle, textwrap_title, textwrap_subtitle, textwrap_authors, textwrap_description
from random import randint
from utils.library import Book, User, Library

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
  
emojis = ['📗', '📓', '📕', '📙', '📔']
gen_emoji = ['👦', '👧']

def print_options():
  print()
  ran = randint(0, 4)
  emo = ' '.join(map(str, emojis[ran]))
  #print(f"{emo}")
  options = [
    f" [1] {emo} Books",
    " [2] Search Books",
    " [3] 📇 Library",
    " [4] Create User",
    " [5] 📚 Borrowed",
    " [6] Exit..."
  ]

  for i in range(0, len(options), 3):
    print("{:<15} {:<15} {:<15}".format(
      *options[i:i+3], *[''] * (3 -len(options[i:i+3]))
    ))

def main():
  library = Library()

  def create_user():
    name = input("\n Enter your name: ")
    user = User(name)
    library.register_user(user)

  data = []
  prices = []
  def searched_books():
    #google_search = 'El monje que vendio su ferari'
    print("" * 1, "-" * 53)
    google_search = input("\n Enter 📖 title: ")
    print()
    books = server.get_book(google_search)
    for idx, book in enumerate(books, start=1):
      # print(f"{idx:2} {book['volumeInfo']['title']}")
      data.append(book['volumeInfo'])
      prices.append(book['saleInfo'])
    for idx, book in enumerate(data, start=1):
      wrapped_lines = textwrap_booksfound(book['title'])
      print(f" [{idx:2}] {wrapped_lines[0].lstrip()}")
      for line in wrapped_lines[1:]:
        print(line)


  searched_books()

  def select_index(selection):
    if 1 <= selection <= len(data) or 1 <= selection <= len(prices):
      return selection - 1
    else:
      return None

  def book_info():
    while True:
      try:
        selection = int(input("\n Select book [#?]: "))
        selected_number = select_index(selection)
        if len(library.users) == 0:
          print(f"\n      You need to register and CREATE a USER\n")
          break

        else:
          if selected_number is None:
            print(" Invalid selection!!!..............")
            continue
          if isinstance(selected_number, int):
            get_title = data[selected_number]
            book = Book(get_title['title'])
            # library.books.append(book)
            library.book_number.append(selected_number+1)
            library.add_book(book)

            # print(f"selection: {selection}\nselected_number: {selected_number}\nlibrary.book_number: {library.book_number}\n")

            if library.book_number.count(selection) > 1 :
              print(f" This book has been recently added.....!\n\n")
              # print(f"LIBRARY.BOOKS: {library.books}")
              library.books.pop()
              library.book_number.pop()
              return

            get_book = data[selected_number]

            if 'publisher' in get_book:
              editorial = get_book['publisher']
            else:
              editorial = "Campeon"
            if 'subtitle' in get_book:
              subtitle = get_book['subtitle']
            else:
              subtitle = "Just Because"
            if 'description' in get_book:
              description = get_book['description']
            else:
              description = " Be happy"
            if 'authors' in get_book:
              authors = get_book['authors']
              author = ", ".join(map(str, authors))
            else:
              author = "Rigoberto Bruno Maldonado"
            if 'publishedDate' in get_book:
              publication = get_book['publishedDate']
            else:
              publication = "2024-07-24"
            
            spacing = " " * 34

            if selected_number is not None:
              if 'listPrice' in prices[selected_number]:
                for_sale = f"{prices[selected_number]['listPrice']['amount']} {prices[selected_number]['listPrice']['currencyCode']}"
              else:
                for_sale = "NOT FOR SALE"

            else:
              print("Invalid selection")

            print("" * 1, "-" * 54)
            print(f"{textwrap_title(get_book['title'])}")
            print(f"{textwrap_subtitle(subtitle)}")
            print(f"{textwrap_authors(author)}")
            print(f" Editorial: {editorial}")
            print(f" Publication Date: {publication}")
            print(f"\n{spacing} Price: {for_sale}")
            print("" * 1, "-" * 53)
            print()
            print(f"{textwrap_description(description)}\n\n")
            break

      except ValueError:
        print(" Invalid input, please enter a number.\n")
        continue

  book_info()

  def bookstore():
    while True:
      seen = set()
      unique_value = []
      for num in library.book_number:
        if num not in seen:
          unique_value.append(num)
          seen.add(num)

      book_set = set(library.book_number)
      selected_set = set(library.selected_number)
      if book_set & selected_set:
        available_books = len(book_set - selected_set)
        print(f"\n {available_books} books available to borrow.\n")
      else:
        print(f"\n {len(unique_value)} books available to borrow.\n")

      question = input(f" Do you need to borrow book? (y/n) ").strip().lower()
      if question == 'y':
        try:
          selection = int(input(f" Select book [{bcolors.OKBLUE}#{bcolors.ENDC}{bcolors.OKCYAN}?{bcolors.ENDC}]: "))

          if selection in library.book_number:
            index = library.book_number.index(selection)
            library.selected_number.append(selection)

            user = library.users[0]
            book = library.books[index]
            user.borrow_book(book)

            if library.selected_number.count(selection) > 1:
              print(f" This book has been recently borrowed.....!\n\n")
              library.selected_number.pop()

            library.show_available_books()

          else:
            print(" Invalid selection!!!.\n\n")
            library.show_available_books()
        except ValueError:
          print(" Invalid selection. Please enter a number!.\n\n")
          library.show_available_books()
      elif question == 'n':
        break
      else:
        print(" Please enter y/n")

  while True:
    print_options()
    try:
      option = int(input("\n Enter option: "))
      if option == 1:
        print()
        for idx, book in enumerate(data, start=1):
          wrapped_lines = textwrap_booksfound(book['title'])
          print(f" [{idx:2}] {wrapped_lines[0].lstrip()}")
          for line in wrapped_lines[1:]:
            print(line)
        book_info()
      elif option == 2:
        searched_books()
        book_info()
      elif option == 3:
        if len(library.users) == 0:
          user_name = "Bruno"
        else:
          user_name = library.users[0].name

        spacing = " " * 23
        print()
        print("" * 1, "-" * 53)
        print(f" {spacing}BOOKSTORE")
        print(f" User: {user_name}")
        print("" * 1, "-" * 53)
        print()

        if len(library.books) == 0:
          print("\n       You don't have books added to the library.\n\n")
        else:
          library.show_available_books()
          bookstore()

      elif option == 4:
        print(f"\n Create User")
        create_user()

      elif option == 5:
        if len(library.users) == 0:
          user_name = "Bruno"
        else:
          user_name = library.users[0].name

        spacing = " " * 21
        print()
        print("" * 1, "-" * 53)
        print(f" {spacing}BORROWED BOOKS")
        print(f" User: {user_name}")
        print("" * 1, "-" * 53)
        print()

        user = library.users[0]

        if len(user.borrowed_books) == 0:
          print("\n            You don't have borrowed books.\n\n")
          continue

        def list_borrowed_books():
          print(" List of Borrowed Books.\n")
          books = user.borrowed_books
          selected_unique = list(dict.fromkeys(library.selected_number))
          numbers = [item for item in selected_unique if item not in library.book_number_return]

          for idx, (number, book) in enumerate(zip(numbers, books), start=1):
            formatted_title = f"[{number:2}] {book.title}"
            print(textwrap_booktitle(idx, formatted_title))

        list_borrowed_books()

        while True:
          seen = set()
          unique_value = []
          for num in library.selected_number:
            if num not in seen:
              unique_value.append(num)
              seen.add(num)

          selected_set = set(library.selected_number)
          return_set = set(library.book_number_return)
          if selected_set & return_set:
            available_books = len(selected_set - return_set)
            print(f"\n {available_books} books available to return.")
          else:
            print(f"\n {len(unique_value)} books available to return.")

          question = input("\n Do you want to return the book? (y/n) ").strip().lower()
          if question == 'y':
            try:
              selection = int(input(f" Select book [{bcolors.OKGREEN}#{bcolors.ENDC}{bcolors.OKCYAN}?{bcolors.ENDC}]: "))

              if selection in library.selected_number:
                index_ = library.selected_number.index(selection)
                library.book_number_return.append(selection)

                user = library.users[0]
                book = user.borrowed_books[index_]
                user.return_book(book)
                # return borrowed books
                library.books.append(book)

                for num in library.book_number_return:
                  if num in library.selected_number:
                    library.selected_number.remove(num)

                list_borrowed_books()
              elif selection in library.book_number_return:
                index_ = library.book_number_return.index(selection)
                book = user.returned_books[index_]
                if index_ < len(user.returned_books):
                  book.return_book()
                  print(f"\n This book has been recently returned.....!\n\n")

                  list_borrowed_books()
              else:
                print(" Invalid selection!!!.\n\n")
                list_borrowed_books()
            except ValueError:
              print(" Invalid input, please enter a number.\n\n")
              list_borrowed_books()
              continue

          elif question == 'n':
            library.book_number_return.clear()
            user.returned_books.clear()
            break
          else:
            print(" Please enter y or n")

      elif option == 6:
        break
      else:
        print(" Please enter a number! between 1 and 6!")
        continue
    except ValueError:
      print(" Please enter a valid number!")
      continue

if __name__ == '__main__':
  main()
