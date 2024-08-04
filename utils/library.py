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
    #print(, flush=True)


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
      message = f"\n{bcolors.FAIL}The book of {book.title}, is not available.{bcolors.ENDC}\n"
      indentation_title5(message)
      #print(, flush=True)


  def return_book(self, book):
    if book in self.borrowed_books:
      book.return_book()
      self.borrowed_books.remove(book)
    else:
      message = f"\n{bcolors.HEADER}The book of {book.title} has not been on the borrowed.{bcolors.ENDC}"
      indentation_title5(message)
      #print()

class Library:
  def __init__(self):
    self.books = []
    self.users = []
    self.book_number = []
    self.selected_number = []
    self.borrowed_books = []
    self.select_book_number_return = []
    self.test_add_books = []

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
    # print(f"\nbooks {self.books}\n")

    if len(self.books) == 0:
      print("\n       You don't have books added to the library.\n")
    else:
      print(" Books Available.\n")
      formatted_titles = []

      seen = set()
      result = []
      for num in self.book_number:
        if num not in seen:
          seen.add(num)
          result.append(num)
        else:
          if result.count(num) < 1:
            result.append(num)

     
      for idx, (number, book) in enumerate(zip(result, self.books), start=1):
        if book.available:
          formatted_titles.append(f"{[number]} {book.title}")

      for idx, formatted_title in enumerate(formatted_titles, start=1):
        if idx < 10:
          spacing_line = " "
          print(spacing_line, end="", flush=True)
          title_format = f"{idx}.- {formatted_title}"
        else:
          title_format = f"{idx}.- {formatted_title}"
        print(indentation_title4(title_format))

book1 = Book("El Monje Que Vendio Su Ferrari")
book2 = Book("1984")

user1 = User("Donna")

# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.register_user(user1)

# library.show_available_books()

# user1.borrow_book(book1)

# library.show_available_books()

# user1.return_book(book1)
