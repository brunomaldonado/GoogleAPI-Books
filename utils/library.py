import threading
import time
from utils.config import indentation_title4, indentation_title5

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

class Book:
  def __init__(self, title):
    self.title = title
    # self.author = author
    self.available = True

  def borrow(self):
    if self.available:
      self.available = False
      # print(f"\nThe book of {self.title} has been borrowed\n")
      message = f"\n{bcolors.OKBLUE}The book of {self.title}, has been borrowed.{bcolors.ENDC}\n"
      indentation_title5(message)
      #print(, flush=True)
    else:
      print(f"{self.title} is not available")

  def return_book(self):
    self.available = True
   # print(f"\nThe book of {self.title} has been returned")
    message = f"\n{bcolors.OKGREEN}The book of {self.title}, has been returned.{bcolors.ENDC}"
    indentation_title5(message)


class User:
  def __init__(self, name):
    self.name = name
    # self.user_id = user_id
    self.borrowed_books = []

  def borrow_book(self, book):
    if book.available:
      book.borrow()
      self.borrowed_books.append(book)
    else:
      # print(f"\nThe book of {book.title}, is not available...\n")
      message = f"\n{bcolors.FAIL}The book of {book.title} is not available, it has been previously loaned.{bcolors.ENDC}\n"
      indentation_title5(message)

  def return_book(self, book):
    if book in self.borrowed_books:
      book.return_book()
      self.borrowed_books.remove(book)
    else:
      message = f"\n{bcolors.FAIL}The book of {book.title} has not been on the borrowed.{bcolors.ENDC}"
      indentation_title5(message)
      #print()

class Library:
  def __init__(self):
    self.books = []
    self.users = []
    self.book_number = []
    self.selected_number = []
    self.book_number_return = []

  def add_book(self, book):
    # if book == "":
    #   book.remove(book)
    self.books.append(book)
    message = f"{bcolors.OKCYAN}The book of {book.title} has been added into the bookstore.{bcolors.ENDC}\n"
    indentation_title5(message)
    #print(f"{bcolors.OKCYAN}The book of {indentation_title5(book.title)} has been added into the bookstore...{bcolors.ENDC}\n", end="", flush=True)

  def register_user(self, user):
    self.users.append(user)
    print(f"\n               👩‍🎤 {user.name} has been register.\n")

  def show_available_books(self):
    # if not any(book.available for book in self.books):
    print(" Books Available.\n")

    print(f"\nBOOK NUMBER: {self.book_number}\nSELECTED NUMBER: {self.selected_number}\n")
    unique_numbers = []
    formatted_titles = []

    for num in self.book_number:
      if num not in unique_numbers:
        unique_numbers.append(num)

    print(f"LEN: {len(self.books)}\n")

    self.books = list(dict.fromkeys(self.books))  # Remove duplicates while preserving order

    # for book in self.books:
    #   if book.available:
    #     print(f"BOOK TITLE: {book.title} - AVAILABLE: {book.available}")
    # print("\n")

    for idx, (number, book) in enumerate(zip(unique_numbers,self.books), start=1):
      if book.available:
        formatted_titles.append(f"[{bcolors.OKBLUE}{number:2}{bcolors.ENDC}] {book.title}")
      # else:
      #   formatted_titles.append(f"[{bcolors.FAIL}{number:2}{bcolors.ENDC}] {book.title}")

    for idx, formatted_title in enumerate(formatted_titles, start=1):
      title_format = f"{bcolors.OKCYAN}{idx:2}{bcolors.ENDC} {formatted_title}"
      print(indentation_title4(title_format))

# book1 = Book("El Monje Que Vendio Su Ferrari")
# book2 = Book("1984")

# user1 = User("Donna")

# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.register_user(user1)

# library.show_available_books()

# user1.borrow_book(book1)

# library.show_available_books()

# user1.return_book(book1)
