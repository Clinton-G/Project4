import mysql.connector


connection = mysql.connector.connect(
    host='localhost',
    user='clintongoin',
    password='password123',
    database='database'
)

if connection.is_connected():
    print('Connected')
else:
    print('Not Connected')




book_library = []


#   ----------------------------------------------------------------------------------------------------


class Book:
    def __init__(self, title, author, isbn, genre, publication_date, availability_status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.availability_status = availability_status

    def get_availability_status(self):
        return self.__availability_status

    def set_availability_status(self, status):
        self.__availability_status = status

    def add_new_book(self, book_library):
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        isbn = input("Enter ISBN: ")
        genre = input("Enter Genre: ")
        publication_date = input("Enter Publication Date: ")
        availability_status = "Available"

        new_book_info = Book(title, author, isbn, genre, publication_date, availability_status)
        book_library.append(new_book_info)
        print(new_book_info, 'has been added' )


#   ----------------------------------------------------------------------------------------------------


class User:
    def __init__(self, name, library_id, books, credit_card):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = books
        self.credit_card = credit_card

    def get_credit_card(self):
        return self.__credit_card
    
    def set_credit_card(self, card_purchases):
        self.__credit_card = card_purchases

    def borrow_book(self, book):
        if book.get_availability_status() == "Available":
            self.borrowed_books.append(book)
            book.set_availability_status("Not Available")
            print(self.name, 'has borrowed', book.title)
        else:
            print("Sorry,", book.title, 'is not available')

    def return_book(self, book):
        if book in self.borrowed_books and book.availability_status == 'Not Available':
            self.borrowed_books.remove(book)
            book.set_availability_status("Available")
            print(self.name, 'has returned', book.title)
            
            
        else:
            print(self.name, 'has not borrowed', book.title)

    def add_new_user(name, email):
        print("User added successfully!")


#   ----------------------------------------------------------------------------------------------------


print('''
    Main Menu:

    1. Book Operations
    2. User Operations
    3. Quit
    ''')


while True:
    menuinput = input('Select an Option: ')


    if menuinput == '1':
        print('''
    
    Book Operations:

    1. Add a new book
    2. Borrow a book
    3. Return a book
    4. Search for a book
    5. Display all books
    
    ''')
    
        menuinput1 = input('Select an Option: ')
        
        if menuinput1 == '1':
            print("1. Add a new book")
            title = input("Enter title: ")
            author = input("Enter author: ")
            quantity = int(input("Enter quantity: "))




    elif menuinput == '2':
        print('''
    
    User Operations:

    1. Add a new user
    2. View user details
    3. Display all users
    
    ''')

        menuinput2 = input('Select an Option: ')




    elif menuinput == '3':
        print('Have a Good Day!')
        break




    else:
        print("Invalid Entry, Try Again")




#   ----------------------------------------------------------------------------------------------------
#   didnt finish in time