from utils import server
from utils.config import indentation_title1, indentation_title2, indentation_title3, indentation_title4, indentation_description, textwrap_title, textwrap_book, textwrap_authors, textwrap_message, textwrap_description
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

def print_options():
  print()
  ran = randint(0, 4)
  emo = ' '.join(map(str, emojis[ran]))
  #print(f"{emo}")
  options = [
    f" [1] {emo} Books",
    " [2] Search Books",
    " [3] 📇 Library",
    " [4] Create 🤵🏽🤵🏻‍♀️",
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
  def seeker():
    #google_search = 'El monje que vendio su ferari'
    print("" * 1, "-" * 53)
    google_search = input("\n Enter 📖 title: ")
    print()
    books = server.search_book(google_search)
    # print(f"books: {books}\nlen: {len(books)}")

    for idx, book in enumerate(books, start=1):
      # print(f"{idx:2} {book['volumeInfo']['title']}")
      data.append(book['volumeInfo'])
      prices.append(book['saleInfo'])
    for idx, book in enumerate(data, start=1):
      # print(f"[{idx:2}] {indentation_title1(book['title'])}")
      wrapped_lines = textwrap_title(book['title'])
      print(f" [{idx:2}] {wrapped_lines[0].lstrip()}")
      for line in wrapped_lines[1:]:
        print(line)


  seeker()

  def select_index(selection):
    if 1 <= selection <= len(data) or 1 <= selection <= len(prices):
      return selection - 1
    else:
      return None

  def book_info():
    # while True:
    #   try:
    selection = int(input("\n Select book [#?]: "))
    option_book = select_index(selection)
    # print(f"===OPTION BOOK: {option_book}")
    book_num = option_book + 1

    # print(f"\noption_book: {option_book}\nbook_num: {book_num}\n")

    if len(library.users) == 0:
      print(f"\n      You need to register and CREATE a USER\n")
      # break

    else:
      if isinstance(option_book, int):
        get_title = data[option_book]
        book = Book(get_title['title'])
        library.book_number.append(book_num)
        library.add_book(book)

        if library.book_number.count(book_num) > 1 :
          print(f" This book has been recently added.....!\n\n")
          # print(f"LIBRARY.BOOKS: {library.books}")
          library.books.pop()
          library.book_number.pop()
          return

        get_book = data[option_book]

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
        authors = get_book['authors']
        author = ", ".join(map(str, authors))
        spacing = " " * 34

        if option_book is not None:
          if 'listPrice' in prices[option_book]:
            for_sale = f"{prices[option_book]['listPrice']['amount']} {prices[option_book]['listPrice']['currencyCode']}"
          else:
            for_sale = "NOT FOR SALE"

        else:
          print("Invalid selection")

        print("" * 1, "-" * 53)
        print(f" Title: {indentation_title2(get_book['title'])}")
        print(f" Sub Title: {indentation_title3(subtitle)}")
        print(f" Authors: {textwrap_authors(author)}")
        print(f" Editorial: {editorial}")
        print(f" Publication Date : {publication}")
        print(f"\n{spacing} Price: {for_sale}")
        print("" * 1, "-" * 53)
        print()
        print(f"{textwrap_description(description)}\n\n")
        #indentation_description(description)
      # except ValueError:
      #   print(" Please enter book number!")
      #   continue

  book_info()

  def bookstore():
    while True:
      seen = set()
      unique_value = []
      for num in library.book_number:
        if num not in seen:
          unique_value.append(num)
          seen.add(num)
      # print(f"unique_value {unique_value}")

      book_set = set(library.book_number)
      selected_set = set(library.selected_number)
      # print(f"book_set{book_set} --- selected_Set{selected_set}")
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
            # add borrowed books
            # print(f"BOOK {book}")
            # print(f"\n You have selected the book number: {selection}\n {book.title}\n INDEX: {index}\n")
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
        # for idx, book in enumerate(data, start=1):
        #   print(f"[{idx:2}] {indentation_title1(book['title'])}")
        for idx, book in enumerate(data, start=1):
          # print(f"[{idx:2}] {indentation_title1(book['title'])}")
          wrapped_lines = textwrap_title(book['title'])
          print(f" [{idx:2}] {wrapped_lines[0].lstrip()}")
          for line in wrapped_lines[1:]:
            print(line)
        book_info()
      elif option == 2:
        seeker()
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
        print(f" User: 🤵🏻‍♀️ {user_name}")
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

          # print(f"\nSELECTED NUMBER: {selected_unique}\nBOOOK NUMBER RETURN: {library.book_number_return}\n")

          numbers = [item for item in selected_unique if item not in library.book_number_return]

          for idx, (number, book) in enumerate(zip(numbers, books), start=1):
            # print(f"{bcolors.OKCYAN}{idx:2}{bcolors.ENDC} [{bcolors.OKGREEN}{number:2}{bcolors.ENDC}] {book.title}")
            formatted_title = f"[{bcolors.OKGREEN}{number:2}{bcolors.ENDC}] {book.title}"
            wrapped_lines = textwrap_book(formatted_title)
            print(f" {bcolors.OKCYAN}{idx:2}{bcolors.ENDC} {wrapped_lines[0].lstrip()}")
            for line in wrapped_lines[1:]:
              print(line)
              
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
                # print(f"INDEX: {index_}")
                library.book_number_return.append(selection)

                user = library.users[0]
                book = user.borrowed_books[index_]
                # print(f"BOOK {book}")
                # print(f"\n You have selected the book number: {selection}\n {book.title}\n INDEX: {index_}\n")
                user.return_book(book)
                # return borrowed books
                library.books.append(book)

                for num in library.book_number_return:
                  if num in library.selected_number:
                    library.selected_number.remove(num)

                # if library.book_number_return.count(selection) > 1 :
                #   print(f" This book has been recently returned.....!\n\n")
                #   library.book_number_return.pop()

                list_borrowed_books()
              elif selection in library.book_number_return:
                index_ = library.book_number_return.index(selection)
                book = user.returned_books[index_]
                if index_ < len(user.returned_books):
                  #print(f"The {book.title} is on books index[{index_}]")
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
