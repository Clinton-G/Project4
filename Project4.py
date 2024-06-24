class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category


class Book:
    def __init__(self, title, author, isbn, publication_date, availability_status="Available", genre=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability_status = availability_status
        self.genre = genre


class User:
    def __init__(self, name, library_id, credit_card):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []
        self.credit_card = credit_card

    def borrow_book(self, book):
        if book.availability_status == "Available":
            self.borrowed_books.append(book)
            book.availability_status = "Borrowed"
            print(self.name, 'has borrowd', book.title)
        else:
            print(book.title, 'is not available')

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.availability_status = "Available"
            print(self.name, 'has returned', book.title)
        else:
            print(self.name, 'has not returnd', book.title)


class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography


class LibraryManagementSystem:
    def __init__(self):
        self.book_library = []
        self.user_library = []
        self.author_library = []
        self.genre_library = []

    def display_menu(self):
        print('''
            Main Menu:
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Genre Operations
        5. Quit
        ''')

    def book_operations(self):
        print('''
        Book Operations:
        1. Add a New Book
        2. Borrow a Book
        3. Return a Book
        4. Search For a Book
        5. Display All Books
        ''')
        choice = input('Select an Option: ')
        if choice == '1':
            self.add_new_book()
        elif choice == '2':
            self.borrow_book()
        elif choice == '3':
            self.return_book()
        elif choice == '4':
            self.search_book()
        elif choice == '5':
            self.display_all_books()
        else:
            handle_invalid_input()

    def add_new_book(self):
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        isbn = input("Enter ISBN: ")
        publication_date = input("Enter Publication Date: ")
        availability_status = "Available"
        genre_name = input("Enter Genre: ")
        genre_description = input("Enter Genre Description: ")
        genre_category = input("Enter Genre Categorie: ")

        genre = Genre(genre_name, genre_description, genre_category)
        new_book = Book(title, author, isbn, publication_date, availability_status, genre)
        self.book_library.append(new_book)
        print(new_book.title, 'hs been added')

    def borrow_book(self):
        user_id = input("Enter User Library ID: ")
        isbn = input("Enter Book ISBN: ")

        user = next((user for user in self.user_library if user.library_id == user_id), None)
        book = next((book for book in self.book_library if book.isbn == isbn), None)

        if user and book:
            user.borrow_book(book)
        else:
            print("User/Book not found.")

    def return_book(self):
        user_id = input("Enter User Library ID: ")
        isbn = input("Enter Book ISBN: ")

        user = next((user for user in self.user_library if user.library_id == user_id), None)
        book = next((book for book in self.book_library if book.isbn == isbn), None)

        if user and book:
            user.return_book(book)
        else:
            print("User/Book not found.")

    def search_book(self):
        isbn = input("Enter Book ISBN: ")
        book = next((book for book in self.book_library if book.isbn == isbn), None)

        if book:
            print(book.title, book.author, book.genre.name, book.availability_Status)
        else:
            print("Book Not Found.")

    def display_all_books(self):
        for book in self.book_library:
            print(book.title, book.author, book.isbn, book.genre.name, book.availability_status)

    def user_operations(self):
        print('''
        User Operations:
        1. Add a New User
        2. View User Details
        3. Display All Users
        ''')

        choice = input('Select an Option: ')
        if choice == '1':
            self.add_new_user()
        elif choice == '2':
            self.view_user_details()
        elif choice == '3':
            self.display_all_users()
        else:
            handle_invalid_input()


    def add_new_user(self):
        name = input("Enter Name: ")
        library_id = input("Enter Library ID: ")
        credit_card = input("Enter Credit Card: ")
        new_user = User(name, library_id, credit_card)
        self.user_library.append(new_user)
        print(new_user.name, 'has been added')


    def view_user_details(self):
        library_id = input("Enter Library ID: ")
        user = next((user for user in self.user_library if user.library_id == library_id), None)
        if user:
            print(user.name, user.library_id, [book.title for book in user.borrowed_books])
        else:
            print("User Not Found.")


    def display_all_users(self):
        for user in self.user_library:
            print(user.name, user.library_id)


    def author_operations(self):
        print('''
        Author Operations:
        1. Add a New Author
        2. View Author Details
        3. Display All Authors
        ''')
        choice = input('Select an Option: ')
        if choice == '1':
            self.add_new_author()
        elif choice == '2':
            self.view_author_details()
        elif choice == '3':
            self.display_all_authors()
        else:
            handle_invalid_input()

    def add_new_author(self):
        name = input("Enter Name: ")
        biography = input("Enter Biography: ")
        new_author = Author(name, biography)
        self.author_library.append(new_author)
        print(new_author.name, 'has been added')

    def view_author_details(self):
        name = input("Enter Author Name: ")
        author = next((author for author in self.author_library if author.name == name), None)
        if author:
            print(author.name, author.biography)
        else:
            print("Author Not Found.")

    def display_all_authors(self):
        for author in self.author_library:
            print(author.name)

    def genre_operations(self):
        print('''
        Genre Operations:
        1. Add a New Genre
        2. View Genre Details
        3. Display All Genres
        ''')
        choice = input('Select an Option: ')
        if choice == '1':
            self.add_new_genre()
        elif choice == '2':
            self.view_genre_details()
        elif choice == '3':
            self.display_all_genres()
        else:
            handle_invalid_input()

    def add_new_genre(self):
        name = input("Enter Genre Name: ")
        description = input("Enter Genre Description: ")
        category = input("Enter Genre Category: ")
        new_genre = Genre(name, description, category)
        self.genre_library.append(new_genre)
        print(new_genre.name, 'has been added')

    def view_genre_details(self):
        name = input("Enter Genre Name: ")
        genre = next((genre for genre in self.genre_library if genre.name == name), None)
        if genre:
            print(genre.name, genre.discription, genre.catagory)
        else:
            print("Genre Not Found.")

    def display_all_genres(self):
        for genre in self.genre_library:
            print(genre.name, genre.description, genre.category)

    def run(self):
        while True:
            self.display_menu()
            menuinput = input('Select an Option: ')

            if menuinput == '1':
                self.book_operations()
            elif menuinput == '2':
                self.user_operations()
            elif menuinput == '3':
                self.author_operations()
            elif menuinput == '4':
                self.genre_operations()
            elif menuinput == '5':
                print('Have a Good Day')
                break
            else:
                handle_invalid_input()


def handle_invalid_input():
    print("Invalid Inpit, Please Try Again.")


if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.run()
