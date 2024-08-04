from utils import server
from utils.config import indentation_title1, indentation_title2, indentation_title3, indentation_title4, indentation_description
from random import randint
from utils.library import Book, User, Library

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
      print(f"[{idx:2}] {indentation_title1(book['title'])}")

  seeker()

  def select_index(selection):
    if 1 <= selection <= len(data) or 1 <= selection <= len(prices):
      return selection - 1
    else:
      return None
     
  def book_info():
    selection = int(input("\n Select book #: "))
    option_book = select_index(selection)
    book_num = option_book + 1
    # print(f"option book: {option_book + 1}")
    if len(library.users) == 0:
      print(f"\n      You need to register and CREATE a USER\n")
     
    else:
      if isinstance(option_book, int):
        get_title = data[option_book]
        book = Book(get_title['title'])
        library.add_book(book)
        library.book_number.append(book_num)

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
        print(f" Authors: {author}")
        print(f" Editorial: {editorial}")
        print(f" Publication Date : {publication}")
        print(f"\n{spacing} Price: {for_sale}")
        print("" * 1, "-" * 53)
        print()
        #print(f"{description}")
        indentation_description(description)

  book_info()

  while True:
    print_options()
    option = int(input("\n Enter option: "))
    if option == 1:
      print()
      for idx, book in enumerate(data, start=1):
        print(f"[{idx:2}] {indentation_title1(book['title'])}")
      book_info()
    elif option == 2:
      seeker()
      book_info()
    elif option == 3:
      if len(library.users) == 0:
        user_name = "Bruno"
      else:
        user_name = library.users[0].name
     
      spacing = " " * 20
      print()
      print("" * 1, "-" * 53)
      print(f" BOOKSTORE {spacing}User: 🧑🏼‍⚖️ {user_name}")
      print("" * 1, "-" * 53)
      print()

      library.show_available_books()

      seen = set()
      unique_book_number = []
      for book_num in library.book_number:
        if book_num not in seen:
          seen.add(book_num)
          unique_book_number.append(book_num)
        else:
          if unique_book_number.count(book_num) < 1:
            unique_book_number.append(book_num)

      while True:
        question = input(f"\n Do you need to borrow book? (y/n) ").strip().lower()
        if question == 'y':
          try:
            selection = int(input(" Select book #: "))
            # borrowed_book = select_index(selection)
            # print(borrowed_book)
            if selection in unique_book_number:
              index = unique_book_number.index(selection)
              # print(f"book number {selection} {library.books[index]}")
              library.selected_number.append(selection)
            else:
              print(" Invalid selection, try again")
          except ValueError:
            print(" Invalid input. Please enter a number.")
            break
          except KeyboardInterrupt:
            break
         
          if len(library.users) == 0:
            print(" You need to register")
            break
          else:
            book = library.books[index]
            # book = library.books[borrowed_book]
            #print(book)
            user = library.users[0]
           
            #add borrowed books
            user.borrow_book(book)

            library.borrowed_books.append(book)
            library.show_available_books()

        elif question == 'n':
          break
        else:
          print(" Please enter y or n")

    elif option == 4:
      print(f"\n Create User")
      create_user()
    elif option == 5:
      if len(library.users) == 0:
        user_name = "Bruno"
      else:
        user_name = library.users[0].name
     
      spacing = " " * 15
      print()
      print("" * 1, "-" * 53)
      print(f" BORROWED BOOKS {spacing}User: 🤵🏻‍♀️ {user_name}")
      print("" * 1, "-" * 53)
      print()

      user = library.users[0]
      # library.select_book_number_return = []
      books = user.borrowed_books
     
      def list_borrowed_books():
        if len(books) == 0:
          print("\n            You don't have borrowed books.\n")
        else:
          print(" List of Borrowed Books.\n")
          formatted_titles = []
         
          #print(f"library.selected_number {library.selected_number}\n")
          #print(f"library.select_book_number_return {library.select_book_number_return}\n")

          seen = set()
          select_number = []

          for num in library.selected_number:
            if num not in seen:
              seen.add(num)
              select_number.append(num)
            else:
              if select_number.count(num) < 1:
                select_number.append(num)

          numbers = [item for item in select_number if item not in library.select_book_number_return]
          # print(f"\nnumbers {numbers}\n")

          for i, (number, book) in enumerate(zip(numbers, books), start=1):
            formatted_titles.append(f"[{number}] {book.title}")
          # print(numbers)
         
          for idx, formatted_title in enumerate(formatted_titles, start=1):
            if idx < 10:
              spacing_line = " "
              print(spacing_line, end="", flush=True)
              title_format = f"{idx}.- {formatted_title}"
            else:
              title_format = f"{idx}.- {formatted_title}"
             
            print(indentation_title4(title_format))


          #for formatted_title in formatted_titles:
            #print(indentation_title4(formatted_title))

      list_borrowed_books()

      while True:
        question = input("\n Do you want to return the book? (y/n) ").strip().lower()
        if question == 'y':
          try:
            selection = int(input(" Return book #: "))
            if selection in library.selected_number:
              index = library.selected_number.index(selection)
              library.select_book_number_return.append(selection)
              # borrowed_book_number = selection
              # print(f"borrowed_book_number {borrowed_book_number}\n")
            else:
              print(" Invalid selection, try again.")
          except ValueError:
            print(" Invalid input, please enter a number.")
            break
          # selection = int(input("Return book #: "))
          # borrowed = select_index(selection)
          # print(borrowed)

          book = library.borrowed_books[index]
          user.return_book(book)
          # print()
          list_borrowed_books()
        elif question == 'n':
          library.selected_number = [number for number in library.selected_number if number not in library.select_book_number_return]
          # print(f"cyle while -> library.selected_number {library.selected_number}")
          library.select_book_number_return.clear()
          break
        else:
          print(" Please enter y or n")
    elif option == 6:
      break

if __name__ == '__main__':
  main()
